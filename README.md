# **Machine_Learning_Project**

 Machine learning project started with MLOps and Deployment

## Software and account Requirement.
1) Github Account
2) Heroku Account
3) VS Code IDE
4) GIT cli
5) GIT Documentation

### Creating conda environment

```
conda create -p <env_name> python==3.9 -y
```
```
conda activate venv/
```
```
pip install -r requirements.txt
```
OR

```
pip install -r D:\Bhushan_Thorat\AI_ML\MLFlow\Cost_Prediction_New\Machine_Learning_Project\requiremets.txt
```
```
cd Machine_Learning_Project             #Used for setting current directory
```
#### Git Commands
```
git init                                #To Initialize a Git repository
git status                              #Helps to show untracked files (status)
git add.                                #Helps to add all untacked and modified files (.gitignore files not included)
git log                                 #To track versions
git commit -m "Description"             #Used to commit chnages on gitHub
<<<<<<< HEAD
git push origin main                    #To send version/changes to git hub
git remote -v                           #To get url of repo you are working in

```
#### To setup CI/CD Pipeline in heroku we need three information
```
1) Heroku mail.
2) Heroku API Key.
3) Heroku App Name.

```
#### Building docker Image
```
docker build -t my-flask-app .

    docker build — starts the build process.
    -t your-image-name — tags (names) the image for easier reference later.(name need to be in small letters always)
    . tells Docker to use the current directory as the build context (where your Dockerfile and app files are).

