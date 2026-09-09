pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/hibahtaj/jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }
    }
}