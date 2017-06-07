#!/usr/bin/python3

import pytest
import os.path
import os
import inspect

# from lib_git_repo import repoInfo
import lib_git_repo

class TestRepoListFromFile:
    """ Test repoListFromFile """

    def setup_class(self):
        self.ri = lib_git_repo.repoInfo()
        self.ri_path = os.path.dirname(inspect.getfile(lib_git_repo))
        self.debug = True
        self.test_path = "/testdata/"

    # list file with no changes
    def test_listfile_one_entry(self):
        fileName = "one-repo_no_change.txt"
        listFile = self.ri_path + self.test_path + fileName
        list = self.ri.repoListFromFile(listFile)

        if self.debug:
            print('listFile location: ', listFile)

        assert list == ['testdata/repo_no_change']

    def test_listfile_two_entries(self):
        fileName = "two_repos.txt"

        listFile = self.ri_path + self.test_path + fileName
        list = self.ri.repoListFromFile(listFile)

        if self.debug:
            print('listFile location = ', list)

        assert list == ['testdata/repo_no_change', 'test-data/one_change']

    def test_bad_listfile(self):
        fileName = "no_file_here.txt"

        listFile = self.ri_path + self.test_path + fileName

        with pytest.raises(SystemExit):
            list = self.ri.repoListFromFile(listFile)

    def test_blank_lines(self):
        fileName = "repoList_with_spaces.txt"

        listFile = self.ri_path + self.test_path + fileName
        list = self.ri.repoListFromFile(listFile)

        if self.debug:
            print('listFile location = ', list)

        assert list == ['testdata/repo_no_change', 'test-data/one_change']

    def test_blank_lines_comments(self):
        fileName = "repoList_with_spaces_comments.txt"

        listFile = self.ri_path + self.test_path + fileName
        list = self.ri.repoListFromFile(listFile)

        if self.debug:
            print('listFile location = ', list)

        assert list == ['testdata/repo_no_change', 'test-data/one_change']
