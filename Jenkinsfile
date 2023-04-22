pipeline {
	agent any
	triggers {
        githubPush()
    }
	environment {
        DOCKERHUB_CREDS  = credentials('DOCKERHUB_CREDS')
    }
  stages {
    stage('Cleanup') {
        steps {
            cleanWs()
        }
    }
    stage('SCM checkout') {
      steps {
        git url: 'https://github.com/matanmeshi1/devops_proj_3.git', branch: 'main'
      }
    }
    stage('Build version') {
      steps {
        sh 'docker build -t matanmeshi1/devops_proj3:${BUILD_NUMBER} ./'
        sh 'docker build -t matanmeshi1/devops_proj3:lts ./'
      }
    }
    stage('Publish') {
      steps {
        sh 'docker login -u $DOCKERHUB_CREDS_USR -p $DOCKERHUB_CREDS_PSW'
        sh 'docker push matanmeshi1/devops_proj3:${BUILD_NUMBER}'
        sh 'docker push matanmeshi1/devops_proj3:lts'
      }
    }
  }
}