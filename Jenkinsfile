pipeline {
    environment {
        branch = "${GIT_BRANCH}"
    }

    agent any

    stages {
        stage('Pull') {
            steps {
                echo '=========================================== 1. Pulling latest repo ======================================================='
                sh 'rm -r *'
                checkout scm
                echo '=========================================== 1. END ======================================================================='
            }
        }
        
        stage('Build') {
            steps {
                echo '=========================================== 2. Building docker image ====================================================='
                script {
                    // dockerImage = docker.build "006262944085.dkr.ecr.eu-west-2.amazonaws.com/v2-ecr" + ":portfolio_v2_$BUILD_NUMBER"
                    dockerImage = docker.build "006262944085.dkr.ecr.eu-west-2.amazonaws.com/v2-ecr"
                }
                echo '=========================================== 2. END ======================================================================='
            }
        }

        // stage('Tag-main') {
        //     when {expression { branch == "main" }}
        //     steps {
        //         echo '=========================================== 3. Tagging image on main branch =============================================='
        //         script {
        //             docker tag dockerImage 006262944085.dkr.ecr.eu-west-2.amazonaws.com/v2-ecr:latest_izhak
        //         }
        //         echo '=========================================== 3. END ======================================================================='
        //     }
        // }

        // stage('Tag-feature') {
        //     when { branch "feature/*" }
        //     steps {
        //         echo '=========================================== 3. Tagging image on feature branch ==========================================='
        //         script{
        //             
        //         }
        //         echo '=========================================== 3. END ======================================================================='
        //     }
        // }

        stage('Test') {
            steps {
                echo '=========================================== 4. Testing ==================================================================='
                sh """
                    docker-compose up -d --build
                    until [ "`docker inspect -f {{.State.Running}} nginx`"=="true" ]; do
                    sleep 0.1;
                    done;
                    echo '============== Application is up and ready =============='
                    docker-compose down
                """
                echo '=========================================== 4. END ======================================================================='
            }
        }

        stage('Publish-feature') {
            when { branch "feature/*" }
            steps {
                echo '=========================================== 5. Publish image to ECR (feature) ===================================================='
                script{
                    docker.withRegistry("https://" + "006262944085.dkr.ecr.eu-west-2.amazonaws.com/v2-ecr", "ecr:eu-west-2:" + "portfoliocredentials") {
                        dockerImage.push("feature_${env.BUILD_NUMBER}")
                    }
                }
                echo '=========================================== 5. END ==============================================================================='
            }
        }

        stage('Publish-main') {
            when {expression { branch == "main" }}
            steps {
                echo '=========================================== 5. Publish image to ECR (main) ===================================================='
                script{
                    docker.withRegistry("https://" + "006262944085.dkr.ecr.eu-west-2.amazonaws.com/v2-ecr", "ecr:eu-west-2:" + "portfoliocredentials") {
                        dockerImage.push("release_1.${env.BUILD_NUMBER}")
                        dockerImage.push("latest")
                    }
                }
                echo '=========================================== 5. END ============================================================================'
            }
        }

        // Deploy
    }
}