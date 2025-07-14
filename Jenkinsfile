pipeline {
  agent any
  environment {
    IMAGE = 'flask-summarizer'
    DOCKERHUB_USER = 'your-dockerhub-username'  // 🔁 CHANGE THIS
  }

  stages {
    stage('Clone Code') {
      steps { checkout scm }
    }

    stage('Build Image') {
      steps {
        sh 'docker build -t $IMAGE .'
      }
    }

    stage('Run Tests') {
      steps {
        sh 'docker run --rm $IMAGE pytest -q'
      }
    }

    stage('Push to Docker Hub') {
      when { branch 'main' }
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh """
            echo "$PASS" | docker login -u "$USER" --password-stdin
            docker tag $IMAGE $USER/$IMAGE:latest
            docker push $USER/$IMAGE:latest
          """
        }
      }
    }

    stage('Run Container') {
      steps {
        sh 'docker rm -f summarizer || true'
        sh 'docker run -d --name summarizer -p 5000:5000 $IMAGE'
      }
    }
  }
}
