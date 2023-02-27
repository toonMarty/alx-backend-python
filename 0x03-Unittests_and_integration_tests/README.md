# 0. Parameterize a unit test
A TestAccessNestedMap class that inherits from unittest.TestCase.
The class contains the implementation of the TestAccessNestedMap.test_access_nested_map method
to test that the method returns what it is supposed to.
The method has been decorated with @parameterized.expand to test the function for given inputs

# 1. Parameterize a unit test
Implementing TestAccessNestedMap.test_access_nested_map_exception that uses the assertRaises context
manager to test that a KeyError is raised for a given set of inputs

# 2. Mock HTTP calls
Implementing the TestGetJson.test_get_json method to test that utils.get_json returns the expected result.

# 3. Parameterize and patch
Implementing the test_memoizee method

# 4. Parameterize and patch as decorators
Implementing the test_org method.
This method tests that GithubOrgClient.org returns the correct value.

# 5. Mocking a property
Implementing the test_public_repos_url method to unit-test GithubOrgClient._public_repos_url.

# 6. More patching
Implementing TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.
We should test that the list of repos is what you expect from the chosen payload.
We should test that the mocked property and the mocked get_json is called once.

# 7. Parameterize
Implementing TestGithubOrgClient.test_has_license to unit-test GithubOrgClient.has_license.

# 8. Integration test: fixtures
Testing the GithubOrgClient.public_repos method in an integration test.

# 9. Integration tests
Implementing the test_public_repos method to test GithubOrgClient.public_repos
Implementing test_public_repos_with_license to test the public_repos with the argument license="apache-2.0"
