pipeline {
    agent any

    environment {
        APP_PORT = '8000'
        APP_SCRIPT = 'app.py'
    }

    stages {
        stage('Fetch SCM') {
            steps {
                echo 'Checking out latest commit from GitHub...'
                checkout scm
            }
        }

        stage('Pre-Flight & Dependency Check') {
            steps {
                sh '''
                    echo "[STATUS] Verifying host dependencies..."
                    python3 --version
                    which pkill || (sudo apt-get update && sudo apt-get install -y psmisc)
                '''
            }
        }

        stage('Deploy Microservice') {
            steps {
                sh '''
                    echo "[DEPLOY] Cycling previous service allocations..."
                    pkill -f "python3 ${APP_SCRIPT}" || true

                    echo "[DEPLOY] Spawning service with process persistence..."
                    export JENKINS_NODE_COOKIE=dontKillMe
                    nohup python3 ${APP_SCRIPT} > app.log 2>&1 &

                    sleep 2
                    echo "[VERIFY] Capturing boot logs:"
                    cat app.log
                '''
            }
        }
    }

    post {
        success {
            echo "================================================="
            echo " SUCCESS: Application successfully deployed!"
            echo " Endpoint: http://<AWS-EC2-PUBLIC-IP>:8000/"
            echo "================================================="
        }
        failure {
            echo " CRITICAL: Pipeline encountered an execution fault."
        }
    }
}