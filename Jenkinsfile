pipeline {
  agent any

  triggers {
    // Check GitHub every 2 minutes
    pollSCM('H/2 * * * *')
  }

  stages {

    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/najlasadek/movie-app.git'
      }
    }

    stage('Build Docker Image in Minikube') {
      steps {
        bat '''
        call minikube docker-env --shell=cmd > docker_env.bat
        call docker_env.bat
        docker build -t movieapp:latest .
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat '''
        kubectl apply -f deployment.yaml
        kubectl apply -f service.yaml
        kubectl rollout status deployment/movieapp-deployment
        '''
      }
    }
  }
}
