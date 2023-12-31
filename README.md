# Sample FastAPI App

This is a sample FastAPI application to demonstrate CI/CD with Jenkins, Docker, and Kubernetes.

## Table of Contents

- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Infrastructure provisioning](#infrastructure_provisioning)
- [Pipeline](#pipeline)
- [Explanation](#explanation)

## Installation
To run the application locally
```
. shells/install.sh
```
This will install all the dependencies.
Then run main.py and the application can be accessed from the browser at 'http://0.0.0.0:8080'

## Prerequisites

To run this application, you need to have the following software installed:

- Linux distribution
- Python 3.9 or higher
- Jenkins
- Docker
- Kubernetes (for deployment)

## Infrastructure provisioning

![Project Architecture](diagram.jpg)

Assuming we are working on a Linux-based distribution, we'll need VMbox and Vagrant installed which will be needed for Kubernetes cluster setup.

For this project, we'll be using three VM. One ubuntu based, other two will be Alma Linux based. 

In our Ubuntu-based VM, we will set up Jenkins and Docker.

In our Alma-based VM, we will set up one Kubernetes cluster and one worker.

Here are the provisioning scripts https://drive.google.com/drive/folders/1CluibA2_btDltn2EEkqWp7LaYM6j_qP7?usp=drive_link

Run the ubuntu_conf.sh to set up Jenkins and Docker.

Run the Vagrantfile from the alma-cluster and alma-worker directory to provision the Kubernetes cluster and worker. 
After accessing Kubernetes worker, run the kubeadm join command saved inside join.sh file. Or copy it from the terminal of Kubernetes-cluster.

## Pipeline

Install necessary plugins in Jenkins for Docker and Kubernetes.  
Create credentials for github, docker-hub and kubernetes, ID as Git-Hub-Auth, Docker-Hub-Auth, and Kube-Config respectively. Or change the name in pipeline accordingly.  
Create a pipeline and run it, ensuring Kubernetes VMs are running.  
When the build is complete, site can be access from browser at 'http://192.168.56.20:30080'

## Explanation

There are a total of eight steps in the Jenkins pipeline.  
First, we will pull the git repository.   

Then we will install the project dependencies as they are required for performing Linting and unit testing

For linting, pylint is used here.

In the unit test, it checks if the web page output is as desired. So to the pass the test case, changes made to the main.py should be reflected on test_main.py

Then docker image is built.

In the next stage, it is pushed to docker hub. I've used my personal docker hub account 'https://hub.docker.com/u/nahiyanswe'. Please change it accordingly.

Then it is deployed to kubernetes. Make sure serverUrl matches the ip where kubernetes Cluster is running.
In the yml file, there's one deployment section and one service section. Nodeport is defined as 30080.

Finally, docker image is removed from the Jenkins machine's work directory.
