pipeline {
    agent any

    stages {
        stage('Clone Practice Repo') {
            steps {
                git 'https://github.com/YOUR_GITHUB_USERNAME/Practice.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t YOUR_DOCKERHUB_USERNAME/practice-notes:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push YOUR_DOCKERHUB_USERNAME/practice-notes:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s.yaml'
            }
        }
    }
}
