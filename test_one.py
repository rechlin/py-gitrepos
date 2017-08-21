#!/usr/bin/python3

import pytest
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


    # tests
    def test_listfile_one_entry(self):
        fileName = "one-repo_no_change.txt"
        listFile = self.ri_path + self.test_path + fileName
        list = self.ri.repoListFromFile(listFile)
        assert list == ['testdata/repo_no_change']


    def test_listfile_two_entries(self):
        fileName = "two_repos.txt"
        listFile = self.ri_path + self.test_path + fileName
        list = self.ri.repoListFromFile(listFile)
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

