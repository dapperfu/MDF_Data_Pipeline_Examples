pipeline {
    agent any
    stages {
        stage('venv') {
            steps {
                sh 'make venv'
            }
        }
        stage('Data') {
            steps {
                sh 'make Data'
            }
        }
		stage('Index') {
            steps {
                sh 'make mdf_index.sqlite'
            }
		}
    }
}
