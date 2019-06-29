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
    stage('Install') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Build') {
      steps {
         parallel(
          tests: {
            sh 'nosetests --with-coverage'
            sh 'coverage xml'
          },
          flake8: { sh 'flake8 src' }
        )
      }
    }

    stage('Upload coverage') {
      steps {
        parallel(
          coveralls: { sh 'coveralls' },
          codacy: { sh 'python-codacy-coverage' }
        )
      }
    }
  }
}
