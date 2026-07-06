pipeline {
    agent any

    stages{
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Enviroment Check") {
            steps {
                sh "python3 -m venv .venv"
                sh ". .venv/bin/activate && python3 --version"
                sh ". .venv/bin/activate && pip --version"
                sh "git --version"
            }
        }

        stage("Install Dependencies") {
            steps {
                sh ". .venv/bin/activate && pip install -r requirements.txt"
            }
        }

        stage("Running") {
            steps {
                sh ". .venv/bin/activate && pytest -v --junitxml=test-results.xml"
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: "test-results.xml"
            echo "Pipeline execution completed"
        }
        success {
            echo "Build passed. OOP solution and test are valid."
        }
        failure {
            echo "Build failed. Review console output, pytest failures, and your implementation"
          }
    }
}
