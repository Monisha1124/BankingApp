pipeline {
    agent any
    
    environment {
        DOCKER_USER = 'monisha1124'
        IMAGE_NAME  = 'bankingapp'
        APP_TAG     = 'v1'
    }
    
    stages {
      
        stage('Continuous Integration') {
            steps {
                echo 'Running automated test assertions...'
                sh 'python3 -m unittest test_app.py'
            }
        }
        
        
        stage('Determine Target Version') {
            steps {
                script {
                   
                    def hasWithdraw = sh(script: "grep -q 'def withdraw' app.py", returnStatus: true) == 0
                    if (hasWithdraw) {
                        APP_TAG = 'v2'
                    }
                    echo "Application Tag detected: ${APP_TAG}"
                }
            }
        }
        
        
        stage('Build and Push') {
            steps {
              
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    echo 'Logging into Docker Hub Registry...'
                    sh "echo \$PASS | docker login -u \$USER --password-stdin"
                    
                    echo "Compiling container image tag: ${APP_TAG}"
                    sh "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:${APP_TAG} ."
                    sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:${APP_TAG}"
                }
            }
        }
        

        stage('Deployment') {
            steps {
               
                withConfigFile([configFileId: 'kubeconfig-file', variable: 'KUBECONFIG']) {
                    echo 'Updating target image version tag in manifest...'
                    sh "sed -i 's|DOCKERHUB_TAG_PLACEHOLDER|${DOCKER_USER}/${IMAGE_NAME}:${APP_TAG}|g' k8s/deployment.yaml"
                    
                    echo 'Applying resource states onto cluster namespace...'
                    sh "kubectl --kubeconfig=\$KUBECONFIG apply -f k8s/deployment.yaml"
                    sh "kubectl --kubeconfig=\$KUBECONFIG apply -f k8s/service.yaml"
                }
            }
        }
    }
}