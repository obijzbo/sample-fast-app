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
                checkout scm
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("$APP_IMAGE_NAME:$BUILD_VERSION")
                    docker.withRegistry('https://registry.hub.docker.com', 'Docker-Hub-Auth') {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    deployToKubernetes()
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    cleanUp()
                }
            }
        }
    }

    post {
        always {
            cleanUp()
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}


def deployToKubernetes() {
    kubeconfig(credentialsId: env.KUBE_CONFIG_ID, serverUrl: '192.168.56.20') {
    	        sh "sed -i 's/APP_VERSION/${version}/g' sample-fast-app.yml" // Replace version placeholder in YAML

        sh "/usr/local/bin/kubectl apply -f sample-fast-app.yml --record=true --record deployment"
    }
}

def cleanUp() {
    dockerRemoveImage("$APP_IMAGE_NAME:$BUILD_VERSION")
    deleteDir()
}
