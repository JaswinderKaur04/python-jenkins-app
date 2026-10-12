pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                // Pulls code from your GitHub repository
                checkout scm
            }
        }
        stage('Test Python Syntax') {
            steps {
                // Validates that your Python script has no syntax errors
                sh 'python3 -m py_compile app.py'
            }
        }
        stage('Deploy Microservice') {
            steps {
                // Clears port 8000 and launches the microservice cleanly in the background
                sh '''
                fuser -k 8000/tcp || true
                nohup python3 app.py > server.log 2>&1 </dev/null &
                echo "Microservice deployed successfully!"
                '''
            }
        }
    }
}
