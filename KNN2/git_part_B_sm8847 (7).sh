#!/bin/bash

#(i) initialise and create the git repository, 

cd \Users\admin\final_repository  #set working directory to where my quiz_knn_answer_key.py file is 
git init  # git directory initiated 
git add quiz_knn_answer_key.py   # my quiz_knn_answer_key.py file added to the git directory so it will be tracked now 
git commit -m "This is the original unmodified version"

#(ii) at least two example commits, 
git add quiz_knn_answer_key.py
git commit -m "I have imported the python pdb function to use the debugger, and added a docstring explaining the knn_predict function and its parameters"

git add quiz_knn_answer_key.py
git commit -m "My function is complete at this point but some bugs present"

git add quiz_knn_answer_key.py
git commit "My code seems to be working, I used Jupyter lab previously to see if the code works because was having trouble rrunning it in my text editor"

git add quiz_knn_answer_key.py
git commit -m "indentation errors rectified, code finally working"

#(iii) the tagging operation, 
git log --oneline
git tag END_TERM_EXAM_2019 3d8614f

#3d8614f (HEAD -> master, tag: END_TERM_EXAM_2019) Final version, almost ready to upload

#(iv) reverting to the first commit (see checkout in git), 

git checkout 6ce789d

#Note: switching to '6ce789d'.

#You are in 'detached HEAD' state. You can look around, make experimental
#changes and commit them, and you can discard any commits you make in this
#state without impacting any branches by switching back to a branch.

#If you want to create a new branch to retain commits you create, you may
#do so (now or later) by using -c with the switch command. Example:

# git switch -c <new-branch-name>

#Or undo this operation with:

 # git switch -

#Turn off this advice by setting config variable advice.detachedHead to false

#HEAD is now at 6ce789d This is the original unmodified version



#(v) reverting back to the last commit (HEAD).

git revert HEAD 


#Revert "This is the original unmodified version"               
                                                               
This reverts commit 6ce789d5f8f5bc4513978741c0fa137a69ad64c0.  
                                                               
# Please enter the commit message for your changes. Lines star>
# with '#' will be ignored, and an empty message aborts the co>
#                                                              
# HEAD detached at 6ce789d                                     
# Changes to be committed:                                     
#       deleted:    quiz_knn_answer_key.py                     
#                                                              
                                                               
                                                               
                                                               
                                                               
                                                               

