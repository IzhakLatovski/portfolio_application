pipeline {
    agent any

    stages {
        stage('Pull') {
            steps {
                echo '=========================================== 1. Pulling latest repo ==========================================='
                sh 'rm -r *'
                checkout scm
                echo '=========================================== 1. END ==========================================================='
            }
        }
        
        stage('Build') {
            steps {
                echo '=========================================== 2. Building docker image ==========================================='
                sh """
                    docker build -t portfolio-app-image:"$BUILD_NUMBER" .
                """
                // script {
                //     dockerImage = docker.build "046432083464.dkr.ecr.eu-west-2.amazonaws.com/portfolio" + ":$BUILD_NUMBER"
                // }
                echo '=========================================== 2. END ============================================================='
            }
        }

        stage('Test') {
            steps {
                echo '=========================================== 3. Testing ==========================================='
                sh """
                    docker-compose up -d --build
                    echo "start of check !!!"
                    until [ "`docker inspect -f {{.State.Running}} nginx`"=="true" ]; do
                    sleep 0.1;
                    done;
                    echo "end of check !!!"
                    docker-compose down
                """
                echo '=========================================== 3. END ==============================================='
            }
        }

        // Tag the dockerImage

        stage('Deploy') {
            steps {
                echo '=========================================== 4. Deploying image to ECR ==========================================='
                // script{
                //     docker.withRegistry("https://" + "046432083464.dkr.ecr.eu-west-2.amazonaws.com/portfolio", "ecr:eu-west-2:" + "portfoliocredentials") {
                //         dockerImage.push()
                //     }
                // }
                echo '=========================================== 4. END =============================================================='
            }
        }

    }

    // post {
    //     always {
    //         sh 'docker-compose down'
    //     }
    // }
}