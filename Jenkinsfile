pipeline {
    agent {
        docker {
            image 'buildcontainer:1.5'
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
                // Run the Python script without changing the directory
                sh "python3 /app/git_stats.py"
            }
        }
    }
}

