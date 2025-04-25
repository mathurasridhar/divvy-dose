# divvy-dose
The information can be obtained from the website
https://msridhar.pythonanywhere.com/repos/<your_repo_name>

You can get the consolidate github + bitbucket stats from the above URL. You just have to replace <your_repo_name> with repo names like mailchimp as given below

Example: https://msridhar.pythonanywhere.com/repos/mailchimp

For testing failed URL, you can check  https://msridhar.pythonanywhere.com/repos/mailchi

#Code Running
1) VS Code Editor is a must to be install
2) In https://github.com/mathurasridhar/divvy-dose go to "<>Code" a green button and download the code
as a zip.
3) Unzip the folder
4) Import the folder to VSCode. Navigation => File -> Open Folder
5) Check whether python is running: In VSCode, go  to "Terminal" and execute the following command
=> python3 --version. The successful execution of the command is must
6) check "pip" command is working. In "Terminal" of VSCode just type -> pip.
7) If the above is successful, then execute the following: pip install -r requirements.txt
8) In Terminal run => python3 api.py. It should give the link http://127.0.0.1:5000
9) To test the endpoint use -> http://127.0.0.1:5000/repos/mailchimp
the template is http://127.0.0.1:5000/repos/<reponame>

#Running test cases
Steps 1 to 7b in the above must be followed

To run tests, run the below commands in VSCODE terminal:
python -m pytest test_unit.py
python -m pytest test_integration.py