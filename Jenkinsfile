pipeline {
    agent any

    environment {
        DOCKER_USER = "2023bcs0008"
        IMAGE_BACKEND = "${DOCKER_USER}/2023bcs0008_backend"
        IMAGE_FRONTEND = "${DOCKER_USER}/2023bcs0008_frontend"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Pragatheesh-17/fullstack-devops'
            }
        }

        stage('Build Backend') {
            steps {
                sh 'docker build -t $IMAGE_BACKEND ./backend'
            }
        }

        stage('Build Frontend') {
            steps {
                sh 'docker build -t $IMAGE_FRONTEND ./frontend'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Backend') {
            steps {
                sh 'docker push $IMAGE_BACKEND'
            }
        }

        stage('Push Frontend') {
            steps {
                sh 'docker push $IMAGE_FRONTEND'
            }
        }
    }
}