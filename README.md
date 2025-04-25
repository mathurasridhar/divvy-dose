The information can be obtained from the website http://msridhar.pythonanywhere.com/repos/git=<reponame>&bb=<reponame>

You can get the consolidate github + bitbucket stats from the above URL. You just have to replace <your_repo_name> with repo names like mailchimp as given below

Example: http://msridhar.pythonanywhere.com/repos/git=mailchimp&bb=mailchimp

For testing failed URL, you can check http://msridhar.pythonanywhere.com/repos/git=mailchimp&bb=mailchi

#Code Running

VS Code Editor is a must to be install
In https://github.com/mathurasridhar/divvy-dose go to "<>Code" a green button and download the code as a zip.
Unzip the folder
Import the folder to VSCode. Navigation => File -> Open Folder
Check whether python is running: In VSCode, go to "Terminal" and execute the following command => python3 --version. The successful execution of the command is must
check "pip" command is working. In "Terminal" of VSCode just type -> pip.
If the above is successful, then execute the following: pip install -r requirements.txt
In Terminal run => python3 api.py. It should give the link http://127.0.0.1:5000
To test the endpoint use -> http://127.0.0.1:5000/repos/git=mailchimp&bb=mailchimp the template is http://127.0.0.1:5000/repos/git=<reponame>&bb=<reponame>
#Running test cases Steps 1 to 7b in the above must be followed

To run tests, run the below commands in VSCODE terminal: 
python -m pytest test_unit.py 
python -m pytest test_integration.py