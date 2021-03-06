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


    def clean_path(self, path_list):
        ''' Remove leading folders from path that change between users '''
        scriptPath = os.path.dirname(os.path.realpath(__file__)) + '/'

        result_list = []
        for path in path_list:
            if path.startswith(scriptPath):
                result_list.append(path.replace(scriptPath, '', 1))
            else:
                result_list.append(path)

        return result_list


    def test_repo_no_change(self):
        folder = "repo_no_change"
        path = self.ri_path + self.test_path + folder
        repo_list = self.ri.repoSearch(path)

        repo_list_clean = self.clean_path(repo_list)

        assert repo_list_clean == ['testdata/repo_no_change/.git']

