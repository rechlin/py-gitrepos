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


    # common code
    def getList(self, fileName):
        listFile = self.ri_path + self.test_path + fileName
        list = self.ri.repoListFromFile(listFile)

        if self.debug:
            print('list content = ', list)

        return(list)


    # tests
    def test_listfile_one_entry(self):
        list = self.getList("one-repo_no_change.txt")

        assert list == ['testdata/repo_no_change']


    def test_listfile_two_entries(self):
        list = self.getList("two_repos.txt")

        assert list == ['testdata/repo_no_change', 'test-data/one_change']


    def test_bad_listfile(self):
        with pytest.raises(SystemExit):
            list = self.getList("no_file_here.txt")


    def test_blank_lines(self):
        list = self.getList("repoList_with_spaces.txt")

        assert list == ['testdata/repo_no_change', 'test-data/one_change']

    def test_blank_lines_comments(self):
        list = self.getList("repoList_with_spaces_comments.txt")

        assert list == ['testdata/repo_no_change', 'test-data/one_change']


class TestRepoSearch:
    """ Test repoSearch """

    def setup_class(self):
        self.ri = lib_git_repo.repoInfo()
        self.ri_path = os.path.dirname(inspect.getfile(lib_git_repo))
        self.debug = True
        self.test_path = "/testdata/"

    def test_repo_no_change(self):
        folder = "repo_no_change"
        path = self.ri_path + self.test_path + folder
        repo_list = self.ri.repoSearch(path)

        assert repo_list == ['/home/rob/projects/python-one/repo-report/testdata/repo_no_change/.git']

