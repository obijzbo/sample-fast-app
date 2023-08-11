pipeline {
    agent any

    environment {
        APP_IMAGE_NAME = "nahiyanswe/simple-fast-app"
        KUBE_CONFIG_ID = "Kube-Config"
        BUILD_VERSION = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'Git-Hub-Auth', url: 'https://github.com/obijzbo/sample-fast-app'
            }
        }
        
        
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Linting') {
            steps {
                script {
                    sh "pylint main.py"
                }
            }
        }

        stage('Unit Tests') {
            steps {
                script {
                    try {
                        sh "python3 -m pytest test_main.py"
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker images
                    dockerBuildImage("$APP_IMAGE_NAME:$BUILD_VERSION")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Push Docker images to Docker Hub
                    dockerPushImage("$APP_IMAGE_NAME:$BUILD_VERSION")
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Deploy to Kubernetes
                    deployToKubernetes()
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    // Remove Docker images
                    dockerRemoveImage("$APP_IMAGE_NAME:$BUILD_VERSION")
                    deleteDir()
                }
            }
        }
    }
}

// Custom functions for improved readability and reusability

def dockerBuildImage(imageName) {
    def image = docker.build imageName
}

def dockerPushImage(imageName) {
    docker.withRegistry('https://registry.hub.docker.com', 'Docker-Hub-Auth') {
        def image = docker.image(imageName)
        image.push()
    }
}

def dockerRemoveImage(imageName) {
    sh "docker rmi $imageName"
}

def deployToKubernetes() {
    kubeconfig(credentialsId: env.KUBE_CONFIG_ID, serverUrl: '192.168.56.20') {
       sh "sed -i 's#APP_IMAGE_NAME:BUILD_VERSION#${APP_IMAGE_NAME}:${BUILD_VERSION}#g' sample-fast-app.yml"
        sh '/usr/local/bin/kubectl apply -f sample-fast-app.yml'
    }
}
