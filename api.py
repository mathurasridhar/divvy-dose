from flask import Flask, abort
import requests
import json
import logging

app = Flask(__name__)

#API written to test the initial REST API response. Just a test API
@app.get('/')
def home():
    """Test home."""
    return '<h1>Flask REST API </h1>'

#API to return the following profile information from any github/bitbucket repo: total number of public repos(fork, unfork separated)
#watcher_count (github/bitbucket), list of language(github/bitbucket) , list of repo topics(feature available only for github)
#API link used in dev environment: http://127.0.0.1:5000/repos/<your reponame>
@app.route('/repos/git=<reponame>&bb=<bbrepo>', methods=['GET'])
def getPublicRepos(reponame, bbrepo):
    """Get public repos from github and bitbucket and return the statistics of the same."""
    logging.basicConfig(filename='app.log',level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
    url_git = f'https://api.github.com/orgs/{reponame}/repos'
    url_bitbucket = f'https://api.bitbucket.org/2.0/repositories/{bbrepo}'
    response = requests.get(url_git)
    res_bitbucket = requests.get(url_bitbucket)
    if response.status_code == 200 and res_bitbucket.status_code == 200:
        #repo_list = [{'name':repo['name'], 'url':repo['html_url']} for repo in repos]
        #return jsonify({'Success':'Could ping the link'})
        repos = response.json()
        git_repo_languages = []
        git_watchers_count = [repo['watchers_count'] for repo in repos if repo['visibility'] == 'public']
        git_repo_list_orig = [{'Name':repo['name'], 'PublicURL':repo['html_url'], 'isFork':repo['fork']} for repo in repos if repo['visibility'] == 'public' and repo['fork']==False]
        git_repo_list_forked = [{'Name':repo['name'], 'PublicURL':repo['html_url'], 'isFork':repo['fork']} for repo in repos if repo['visibility'] == 'public' and repo['fork']==True]
        git_repo_languages = [repo['language'] for repo in repos]
        git_repo_topics = []
        git_repo_topics_1 = [git_repo_topics.extend(repo['topics']) for repo in repos]


        bb_public_repos = res_bitbucket.json()
        bb_public_repos = bb_public_repos['values']
        bb_repos = []
        bb_forked = []
        bb_languages = []
        bb_watcher_cnt = 0
        for repo in bb_public_repos:
            if repo['is_private'] is False and repo['parent'] is None:
                bb_repos.append({'name':repo['name'], 'full_name':repo['full_name']})
                watchers = repo['links']['watchers']['href']
                bb_languages.append(repo['language'])
                wres = requests.get(watchers)
                wres = wres.json()
                bb_watcher_cnt += len(wres['values'])
            elif repo['is_private'] is False and repo['parent'] is not None:
                bb_forked.append({'name':repo['name'], 'full_name':repo['full_name']})
                watchers = repo['links']['watchers']['href']
                wres = requests.get(watchers)
                wres = wres.json()
                bb_watcher_cnt += len(wres['values'])
                bb_languages.append(repo['language'])
        res = [{'git_total_number_of_public_repos_unforked':len(git_repo_list_orig), 'git_total_number_of_public_repos_forked':len(git_repo_list_forked),'bitbucket_public_repos_unforked':len(bb_repos), 'bitbucket_public_forked_repos':len(bb_forked), 'git_watchers_count':sum(git_watchers_count), 'bitbkt_total_watchers':bb_watcher_cnt, 'git_repo_languages':list(set(git_repo_languages)), 'bitbucketlanguages':list(set(bb_languages)),'git_repo_topics':list(set(git_repo_topics))}]
        logging.info(res)
        repo_list1 = [{'Name':repo['name'], 'PublicURL':repo['html_url']} for repo in repos]
        return json.dumps(res, indent=4)
    else:
        # return jsonify({'Error':'Failed to retrieve public repositories'})
        logging.basicConfig(filename='app.log',level=logging.ERROR, format='%(asctime)s-%(levelname)s-%(message)s')
        logging.error('http error: 400 BAD REQUEST')
        abort(400, description="Error: Failed to connect")
        

if __name__ == '__main__':
    app.run(debug=True)