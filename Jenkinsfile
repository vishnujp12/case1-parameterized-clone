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
                // Your build steps here
                dir('/app') {
                    // Run the Python file gitstats.py
                    sh "python3 gitstats.py"  // Replace with your actual build command
                }
            }
        }
    }
}

