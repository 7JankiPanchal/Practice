pipeline {
    agent any

    stages {
        stage('Clone Practice Repo') {
            steps {
                git 'https://github.com/7JankiPanchal/Practice.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t 7JankiPanchal/practice-notes:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push 7JankiPanchal/practice-notes:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s.yaml'
            }
        }
    }
}
