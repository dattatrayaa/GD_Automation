# GD_Automation
This is Project repositary for Grovo Automation Framework

## Installation steps
- Install Python 2.7.14  You can download latest version from https://www.python.org/getit/
- To install Robot Framework, Download [installer.sh](Setup/installer.sh) from Setup folder, and run in Terminal/Command line
- Download [TeamCity](https://www.jetbrains.com/teamcity/download/) latest version for MAC
- Untar downloaded file in specific folder by using command 
'''
tar xvf TeamCity-9.1.6.tar
'''
after untar type
'''
cd TeamCity/bin
'''
and to start TeamCity in browser window
'''
./runAll.sh start
'''
- After starting set up an Admin Username and Password for future login
- Create a New Project, Set Project Name, Project ID and click on Create
- This leads to the “Project Settings” page where we need to create a new build configuration, Give name, id and click on Create
- Version Control Settings (VCS) leads you to connect TeamCity to Github follow these [Steps](https://confluence.jetbrains.com/display/TCD10/Integrating+TeamCity+with+VCS+Hosting+Services)
- Now in Build steps we can add our Robot suite command : ./Test_Suite/startSuite.sh
- The suite will run based on robot triggers in startSuite.sh
