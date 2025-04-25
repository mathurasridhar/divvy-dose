from api import getPublicRepos
import unittest
import json
from unittest.mock import patch, MagicMock
import pytest



@pytest.mark.parametrize("reponame, bbrepo",[("mailchimp","mailchimp")])
@patch("api.requests") 
def test_getpublicrepos_success_payload_check(mock_requests, reponame, bbrepo):  # New
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.get.return_value = mock_response

    result = getPublicRepos(reponame,bbrepo)
    assert result != None
    assert result != "Error: Failed to connect"

@pytest.mark.parametrize("reponame, bbrepo",[("mailchimp","mailchimp")])
@patch("api.requests") 
def test_getpublicrepos_error_payload_check(mock_requests, reponame, bbrepo):  # New
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_requests.get.return_value = mock_response

    result = getPublicRepos(reponame,bbrepo)
    assert result != None
    assert result != "Error: Failed to connect"


@pytest.mark.parametrize("reponame, bbrepo",[("mailchimp", "mailchimp")])
@patch("api.requests") 
def test_getpublicrepos_success_payload_attributes_check(mock_requests, reponame,bbrepo):  # New
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.get.return_value = mock_response

    result = getPublicRepos(reponame, bbrepo)
    resdict = json.loads(result)
    dictkeys = resdict[0].keys()
    dictkeys = list(dictkeys)
    print('dictkeys:', dictkeys)
    assert result != None
    assert dictkeys == ['git_total_number_of_public_repos_unforked', 'git_total_number_of_public_repos_forked', 'bitbucket_public_repos_unforked', 'bitbucket_public_forked_repos', 'git_watchers_count', 'bitbkt_total_watchers', 'git_repo_languages', 'bitbucketlanguages', 'git_repo_topics']
    
