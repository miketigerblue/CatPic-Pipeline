pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'tigerblue/catpicapp'
        // Optionally set up Slack webhook or other tokens here
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'git@github.com:miketigerblue/CatPicApp.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install --user -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_REGISTRY}:${env.BUILD_ID} ."
                }
            }
        }

        stage('Push to Docker Registry') {
            steps {
                script {
                    // Log in to DockerHub (make sure Jenkins credentials are set)
                    sh "echo ${DOCKERHUB_PWD} | docker login -u ${DOCKERHUB_USER} --password-stdin"
                    sh "docker push ${DOCKER_REGISTRY}:${env.BUILD_ID}"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Example: run container locally for demo
                    // For advanced use, integrate Kubernetes or AWS ECS/EKS.
                    sh "docker run -d -p 5000:5000 --name catpicapp ${DOCKER_REGISTRY}:${env.BUILD_ID}"
                }
            }
        }
    }

    post {
        success {
            // Slack or email notifications
            // Let's do Slack with a cat GIF included
            slackSend channel: '#devops',
                      message: "Build #${env.BUILD_ID} succeeded! :cat2:",
                      attachments: '[ {"fallback": "Meow!", "image_url": "https://cataas.com/cat/gif"} ]'
        }
        failure {
            slackSend channel: '#devops',
                      message: "Build #${env.BUILD_ID} failed! :x:"
        }
    }
}
