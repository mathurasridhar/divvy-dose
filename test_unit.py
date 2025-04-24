from api import getPublicRepos
import unittest
import json
from unittest.mock import patch, MagicMock
import pytest

@pytest.mark.parametrize("reponame",['mailchimp'])
@patch("api.requests") 
def test_getpublicrepos_err_msg_check(mock_requests, reponame):  # New
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_requests.get.return_value = mock_response

    result = getPublicRepos(reponame)
    print(result)
    assert result == json.dumps({'Error':'Failed to retrieve public repositories'})

@pytest.mark.parametrize("reponame",['mailchimp'])
@patch("api.requests") 
def test_getpublicrepos_success_payload_check(mock_requests, reponame):  # New
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.get.return_value = mock_response

    result = getPublicRepos(reponame)
    print(result)
    assert result != None
    assert result != json.dumps({'Error':'Failed to retrieve public repositories'})

