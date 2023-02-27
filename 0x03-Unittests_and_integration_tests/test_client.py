#!/usr/bin/env python3
"""
This module contains a class, TestGithubOrgClient
that tests methods from the module client
"""
import unittest
from unittest.mock import patch, PropertyMock, Mock, call
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from typing import Dict, Any

from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    The class definition of TestGithubOrgClient
    """

    @parameterized.expand(
        [
            ("google", {"google": True}),
            ("abc", {"abc": True})
        ]
    )
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """
        This method tests the org method returns the
        correct value
        Args:
            org(str):  org_name
            expected(dict): the expected value
            get_patch:
        Return:
             NoneType
        """
        get_patch.return_value = expected
        git_org_client = GithubOrgClient(org)
        self.assertEqual(git_org_client.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/" + org)

    def test_public_repos_url(self):
        """
        This method tests the _public_repos_url method
        returns the expected output based on a mocked
        payload
        Return:
            NoneType
        """
        expected = "www.myweb.com"
        payload = {"repos_url": expected}
        my_mock = "client.GithubOrgClient.org"
        with patch(my_mock, PropertyMock(return_value=payload)):
            org_client = GithubOrgClient("git_org_client")
            self.assertEqual(org_client._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json) -> None:
        """
        This method tests the public_repos method
        returns the expected output
        Args:
            mock_get_json: a mock of the get_json method
        Return:
             NoneType
        """
        tom = {'name': 'Tom', 'license': {'key': 't'}}
        john = {'name': 'John', 'license': {'key': 'j'}}
        chuck = {'name': 'Chuck', 'license': {'key': 'c'}}
        jimmy = {'name': 'Jimmy'}

        my_mock = 'client.GithubOrgClient._public_repos_url'
        mock_get_json.return_value = [tom, john, jimmy, chuck]

        with patch(my_mock, PropertyMock(return_value="www.myweb.com")) as p:
            org_client = GithubOrgClient("org_client")
            self.assertEqual(org_client.public_repos(),
                             ['Tom', 'John', 'Jimmy', 'Chuck'])
            self.assertEqual(org_client.public_repos("t"), ['Tom'])
            self.assertEqual(org_client.public_repos("c"), ['Chuck'])
            self.assertEqual(org_client.public_repos(400.2687), [])
            self.assertEqual(org_client.public_repos("d"), [])
            mock_get_json.assert_called_once_with("www.myweb.com")
            p.assert_called_once_with()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False)
        ]
    )
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, expected: bool):
        """
        This method tests the has_license method returns the
        expected output
        Args:
        repo (Dict): a repository
        license_key(str): the license key
        expected(bool): the expected return value
        Return:
            NoneType
        """
        self.assertEqual(GithubOrgClient.has_license(repo,
                                                     license_key), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        This method mocks requests.get to return
        example payloads found in the fixtures.
        Return:
             NoneType
        """
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        mock_org = Mock()
        mock_org.json = Mock(return_value=org)
        cls.org_mock = mock_org
        mock_repos = Mock()
        mock_repos.json = Mock(return_value=repos)
        cls.repos_mock = mock_repos

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload['repos_url']: mock_repos}
        cls.get.side_effect = lambda x: options.get(x, mock_org)

    @classmethod
    def tearDownClass(cls):
        """
        This method stops the patcher
        Return:
            NoneType
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        This method tests the public_repos method in an
        integration test
        Return:
             NoneType
        """
        org_client = GithubOrgClient("org_cli")
        self.assertEqual(org_client.org, self.org_payload)
        self.assertEqual(org_client.repos_payload, self.repos_payload)
        self.assertEqual(org_client.public_repos(), self.expected_repos)
        self.assertEqual(org_client.public_repos(""), [])
        self.get.assert_has_calls([call("https://api.github.com/orgs"
                                        "/org_cli"),
                                   call(self.org_payload['repos_url'])])

    def test_public_repos_with_license(self):
        """
        This method tests the public_repos with the argument
        license="apache-2.0" and matches the
        expected value from the fixtures.
        Return:
            NoneType
        """
        org_client = GithubOrgClient("org_cli")
        self.assertEqual(org_client.org, self.org_payload)
        self.assertEqual(org_client.repos_payload, self.repos_payload)
        self.assertEqual(org_client.public_repos(), self.expected_repos)
        self.assertEqual(org_client.public_repos(""), [])
        self.assertEqual(org_client.public_repos("apache-2.0"),
                         self.apache2_repos)
        self.get.assert_has_calls([call("https://api.github.com"
                                        "/orgs/org_cli"),
                                   call(self.org_payload['repos_url'])])
