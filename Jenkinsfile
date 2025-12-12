pipeline {

    agent { label 'ubuntu-agent' }

    environment {
        REGISTRY = '<REGISTRY>'       // Example: docker.io
        REPO     = '<REPO>'           // Example: your-dockerhub-username
        IMAGE    = "${env.REGISTRY}/${env.REPO}/sample-web:latest"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $IMAGE'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh "sed -i 's|<REGISTRY>/<REPO>/sample-web:latest|'$IMAGE'|g' k8s/deployment.yaml || true"
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service-nodeport.yaml'
            }
        }
    }
}
  