import os

from conans import ConanFile, tools


class CpptqdmConan(ConanFile):
    name = "cpptqdm"
    version = "2020-03-28-04c733f"
    license = "LICENSE"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-cpptqdm"
    description = "(unofficial) tqdm-like single header c++ pretty progress bar"
    topics = ("progressbar", "tqdm")
    no_copy_source = True
    homepage = "https://github.com/aminnj/cpptqdm"
    # No settings/options are necessary, this is header only

    def source(self):
        git = tools.Git(folder="cpptqdm")
        commit_sha1 = self.version.split("-")[-1]
        git.clone(self.homepage)
        git.checkout(commit_sha1)

    def package(self):
        self.copy("tqdm.h", src="cpptqdm", dst="include")
        self.copy("LICENSE", src="cpptqdm")

    def package_id(self):
        self.info.header_only()
