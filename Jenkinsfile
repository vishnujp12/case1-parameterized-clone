pipeline {
    agent {
        docker {
            image 'buildcontainer:1.1'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code inside the Docker container
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh "python3 /app/gitstats.py"
                }
            
            }
        }
    }
}

