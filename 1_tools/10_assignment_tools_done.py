# TOOLS *********************************************************************
# content = assignment
#
# deliver = Upload the files to your git repository
#           and share it in the assignment submission form.
#
# date    = 2024-03-13
# email   = contact@alexanderrichtertd.com
#***************************************************************************
"""



NOTE: Give yourself the time to play around with the tools,
      make sure everything works properly and note down your questions for our Q&A.




#******************************************************************************
# 11. ADVANCED SCRIPT EDITOR
#******************************************************************************
Let's explore and advance in our use of the script editor:

    a) Install and try one unfamiliar but promising script editor
       that you will use through out the masterclass:

        * Sublime Text 3
        * Visual Studio Code
        * PyCharm
        * ATOM
        * VIM
        * ...


    b) Check out the settings and plugins and add these or more:
        * user settings
        * git
        * spell check
        * color theme
        * ...


    c) USE a few new shortcuts


    d) ADD one helpful snippet and use it through out the masterclass


    e) SHARE in the Discord/python-advanced group:

        * Which script editor did you use previously and what was your experience?
        * Which script editor you try for this masterclass?



NOTE: Nothing to upload in this task.









#******************************************************************************
# 12. SHELL
#******************************************************************************
1) Do the following steps only using a shell:

    a) Create the directory "shell_test"


    b) Create the file "test_print.py" with a simple print into the directory


    c) Rename the file to "new_test_print.py"


    d) List what is in the directory "shell_test" including their file permissions


    e) Execute the Python file and call the simple print


    f) Remove the directory "shell_test" with its content


    BONUS: Solve the tasks without looking them up.


a) mkdir "E:\Course\Tech_Art\TechArt_TD_Alex\Python_Advanced\Week 1&2\Assignment\shell_test"

b) echo "print("Hello Python") " > "E:\Course\Tech_Art\TechArt_TD_Alex\Python_Advanced\Week 1&2\Assignment\shell_test\test_print.py"
   
c) cat "E:\Course\Tech_Art\TechArt_TD_Alex\Python_Advanced\Week 1&2\Assignment\shell_test\test_print.py">> "E:\Course\Tech_Art\TechArt_TD_Alex\Python_Advanced\Week 1&2\Assignment\shell_test\new_test_print.py"
   rm "E:\Course\Tech_Art\TechArt_TD_Alex\Python_Advanced\Week 1&2\Assignment\shell_test\test_print.py"
   
d) ls "E:\Course\Tech_Art\TechArt_TD_Alex\Python_Advanced\Week 1&2\Assignment\shell_test"

e) python "E:\Course\Tech_Art\TechArt_TD_Alex\Python_Advanced\Week 1&2\Assignment\shell_test\new_test_print.py"

f) rm  "E:\Course\Tech_Art\TechArt_TD_Alex\Python_Advanced\Week 1&2\Assignment\shell_test"





2) CREATE a custom .bat or .sh that does the following:

    a) STARTS a DCC of your choice (Maya, 3ds Max, Nuke, Houdini, ...)


    b) ADDS custom script paths


    c) ADDITIONAL overwrites (paths, menus, ...)


    d) Make sure everything works as intended

@echo off

set "SCRIPT_PATH=C:/project/"

set "PYTHONPATH=%SCRIPT_PATH%;%PYTHONPATH%"

set "MAYA_PLUG_IN_PATH=%SCRIPT_PATH%plugin;%MAYA_PLUG_IN_PATH%"
set "MAYA_SHELF_PATH=%SCRIPT_PATH%shelf;%MAYA_SHELF_PATH%"

set "XBMLANGPATH=%SCRIPT_PATH%img;%XBMLANGPATH%"

set "MAYA_DISABLE_CIP=1"
set "MAYA_DISABLE_CER=1"

start "" "C:/Program Files/Autodesk/Maya2025/bin/maya.exe"

exit




#******************************************************************************
# 13. GIT
#******************************************************************************

1) STUDY git example
-----------------------------------------------------------
Before we start to work with git let's make sure to get familiar with the workflow
and how a git project should look like.
Browse through the folders and Wiki of my Open Source Pipeline Plex
which also serves as a code and documentation example throughout this masterclass:

    a) EXPLORE the Plex git repository and look into the code:
    https://github.com/alexanderrichtertd/plex


    b) READ the Wiki to understand the basics of the pipeline:
    https://github.com/alexanderrichtertd/plex/wiki





2) CREATE an assignment repository
-----------------------------------------------------------
All the upcoming assignments must be uploaded to your git repository.
Use the git shell for the following tasks:

    a) Create a new repository for the assignments on GitHub/GitLab/... with the sub folders:
        * 1_tools
        * 2_style
        * 3_advanced
        * 4_ui
        * 5_app (for your application) 

       NOTE: If you use sensitive (company) data make your repository private.
             Invite me using alexanderrichtertd@gmail.com (GitHub)
             (Keep the resources out of your repository.)


    b) ADD a README.mb file describing your application.


    c) ADD and fill out a .gitignore file (must ignore all .pyc files)


    d) ADD, commit and push your first application script(s) remote into "5_app" directory.

    IMPORTANT: In future assignments make sure to commit and push the original version
               before starting with the assignment so we have a before and after.
               The commit message must be: INIT 1_tools / 2_style / 3_advanced / 4_UI / 5_APP
               And: DONE 1_tools / 2_style / 3_advanced / 4_UI / 5_APP.


    e) MAKE changes, commit and push again


    f) CREATE a branch "develop", make small changes and push it remote


    g) MERGE your develop changes into master


    h) TEST and clone your remote repository into another directory (as if you are a user).



git init
mkdir 1_tools 2_style 3_advanced 4_ui 5_app && touch 1_tools/README.md 2_style/README.md 3_advanced/README.md 4_ui/README.md 5_app/README.md
git add .
git commit -m "first add folder github"
git branch -M main
git remote add origin  https://github.com/ThanhHaiii03/PYTHON_ADVANCED.git
git push -u origin main
git add 5_app
git commit -m "INIT 5_app"
git push -u origin main
git add 5_app
git commit -m "DONE 5_app"
git push -u origin main
git branch develop
git checkout develop
git add 5_app
git git commit -m :"New branch"
git push -u origin develop
git checkout main 
git merge develop 
git push -u origin main

h) git clone https://github.com/ThanhHaiii03/PYTHON_ADVANCED.git

3) SUBMIT ASSIGNMENT your git link here:
https://www.alexanderrichtertd.com/pa-tools
"""
