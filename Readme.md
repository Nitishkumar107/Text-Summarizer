
# End to End text summarization project.

## workflow to be followed by for any project

Workflows
creeate requirements
create logging
template.py
setup.py
update config.yaml
update params.yaml
update entity
update the conguration manager in src config
update the component
update the pipeline
update the main.py
update the app.py

------------------------------------How to run?-------------------------
STEP 01- Create a conda environment after opening the repository
1). conda create -n summary python=3.8 -y
2). conda activate summary

----------------------------------STEP 02- install the requirements---------------------
1). pip install -r requirements.txt
2). # Finally run the following command
python app.py
3). Now, open up you local host and port
Author: nitish kumar
Lead Data Scientist
Email: nitish10795gmail.com
-------------------------------------AWS-CICD-Deployment-with-Github-Actions------------------
1. Login to AWS console.
2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

---------------------------------step 3. Create ECR repo to store/save docker image----------------

- Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s

---------------------------------------step 4. Create EC2 machine (Ubuntu)----------------------------
---------------------------------------step 5. Open EC2 and Install docker in EC2 Machine:-----------
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
--------------------------------------------step 6. Configure EC2 as self-hosted runner:---------------

setting>actions>runner>new self hosted runner> choose os> then run command one by one

---------------------------------------------step 7. Setup github secrets:----------------
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app







































