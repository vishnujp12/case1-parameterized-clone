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
                sh "python3 gitstats.py"  // Replace with your actual build command
            }
        }


        // Add more stages as needed
    }

    post {
        success {
            // Your success post-build steps here
            echo 'Build and tests passed!'
        }

        failure {
            // Your failure post-build steps here
            echo 'Build or tests failed!'
        }

        // Add more post-build conditions as needed
    }
}
