// pipeline {
//     agent any
//     stages {
//         stage('Checkout Code') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/NarsingSandeep/jenkins.git'
//             }
//         }
//         stage('Build Docker Image') {
//             steps {
//                 sh 'docker build -t mypythonapp:latest .'
//             }
//         }
//         stage('Run Python Script in Docker') {
//             steps {
//                 sh 'docker run mypythonapp:latest'
//             }
//         }
//     }
// }

pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Webhook Triggered') {
            steps {
                echo "GitHub Webhook Triggered1!"
            }
        }
    }
}