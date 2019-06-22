pipeline {
  agent {
    docker {
      image 'python:3.7.3'
      args '--network=host'
    } 
  }

  environment {
    COVERALLS_REPO_TOKEN = credentials('SCHEDULE_DB_COVERALLS_REPO_TOKEN')
    CODACY_PROJECT_TOKEN = credentials('SCHEDULE_DB_CODACY_PROJECT_TOKEN')
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

    stage('coverage') {
      steps {
        sh 'coverage xml'
        sh 'coveralls'
        sh 'python-codacy-coverage'
      }
    }

    stage('flake8') {
      steps {
        sh 'flake8 src'
      }
    }
  }
}
