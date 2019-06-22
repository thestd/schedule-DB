pipeline {
  agent {
    docker {
      image 'python:3.7.3'
      args '--network=host'
    } 
  }

  stages {
    stage('install') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('test') {
      steps {
        sh 'nosetests --with-coverage'
      }
    }

    stage('flake8') {
      steps {
        sh 'flake8 src'
      }
    }
  }
}
