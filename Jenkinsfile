pipeline {
    agent any
    
    environment {
        FLASK_IMAGE = "flask-app-image"
        DJANGO_IMAGE = "django-app-image"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/SRCEM-AIML/C68_VaibhavsinghMohane_FA.git'
            }
        }

        stage('Build Flask Image') {
            steps {
                script {
                    sh 'docker build -t $FLASK_IMAGE ./Flask_app'
                }
            }
        }

        stage('Build Django Image') {
            steps {
                script {
                    sh 'docker build -t $DJANGO_IMAGE ./Django_app'
                }
            }
        }

        stage('Run Containers') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Push Images to Docker Hub') {
            steps {
                script {
                    sh 'docker tag $FLASK_IMAGE raven2678/$FLASK_IMAGE:latest'
                    sh 'docker tag $DJANGO_IMAGE raven2678/$DJANGO_IMAGE:latest'
                    sh 'docker push raven2678/$FLASK_IMAGE:latest'
                    sh 'docker push raven2678/$DJANGO_IMAGE:latest'
                }
            }
        }
        
        
    }
    
}
