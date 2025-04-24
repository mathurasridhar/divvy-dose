from flask import jsonify
import requests
import json
import pytest


@pytest.mark.parametrize("reponame",['mailchimp','pygame'])
def test_check_gitrepo_connectivity(reponame):
    url_git = f'https://api.github.com/orgs/{reponame}/repos'
    response = requests.get(url_git)
    assert response.status_code == 200

@pytest.mark.parametrize("reponame",['mailchimp', 'pygame'])
def test_check_bbrepo_connectivity(reponame):
    url_bitbucket = f'https://api.bitbucket.org/2.0/repositories/{reponame}'
    response = requests.get(url_bitbucket)
    assert response.status_code == 200