1- ## git is used to create a repository anjd then track the change of any file i changed 
so i commit the change into the repository and we can turn back into the original code  
if anything breaks or fails

2- docker is a software that lets use a specific image of something without the need 
of installing it lets say we want to use python software but we dont have it so we can create 
a container by a python image and it has its own files and libraries built in

3- docker file is the the file where it has instructions to pull the image from docker hub and to 
add code on top of it depending on our desire 
  
  the image is the result of following the instruction of the dockerfile 
  and the container is the place where the actual image runs and where the codes is executed

 4- gitignore is important because it is used when we dont want to commit certain files like .venv or logs 
 to the repositiory 

 5- volumes are important because it lets us store the result of output of the container so when it closes we
 have a place wheere the data is stored 


list of commands :

git init //
//git remote add origin https://github.com/NeGaT1Vee/git-docker-task2.git
//git branch -M main
//git push -u origin main
//git add - 
//git commit -m "text"
//git log --oneline
//git switch -c feature/add-validation
//git merge feature/add-validation , do after switching to main branch
//docker build -t sales-pipeline .
//docker images 
//docker run --name sales-job sales-pipeline
//docker ps -a 
//docker run --rm -v ${PWD}\data:/app/data sales-pipeline
//docker rm sales-job
//docker rmi sales-pipeline
 