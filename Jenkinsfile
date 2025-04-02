pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/NarsingSandeep/jenkins.git'

            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp:latest .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8083:80 myapp:latest'
            }
        }
    }
}
