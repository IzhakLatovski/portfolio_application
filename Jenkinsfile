pipeline {
    environment {
        branch = "${GIT_BRANCH}"
    }

    agent any

    stages {
        // stage('main') {
        //     when {expression { branch == "main" }}
        //     steps {
        //         echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        //     }
        // }

        // stage('not-main') {
        //     when { branch "feature/*" }
        //     steps {
        //         echo "123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123"
        //     }
        // }

        stage('Pull') {
            steps {
                echo branch
                echo '=========================================== 1. Pulling latest repo ==========================================='
                sh 'rm -r *'
                checkout scm
                echo '=========================================== 1. END ==========================================================='
            }
        }
        
        // stage('Build') {
        //     steps {
        //         echo '=========================================== 2. Building docker image ==========================================='
        //         script {
        //             dockerImage = docker.build "006262944085.dkr.ecr.eu-west-2.amazonaws.com/v2-ecr" + ":release-$BUILD_NUMBER"
        //         }
        //         echo '=========================================== 2. END ============================================================='
        //     }
        // }

        // stage('Test') {
        //     steps {
        //         echo '=========================================== 3. Testing ==========================================='
        //         sh """
        //             docker-compose up -d --build
        //             until [ "`docker inspect -f {{.State.Running}} nginx`"=="true" ]; do
        //             sleep 0.1;
        //             done;
        //             echo '============== Application is up and ready =============='
        //             docker-compose down
        //         """
        //         echo '=========================================== 3. END ==============================================='
        //     }
        // }

        // stage('Deploy') {
        //     steps {
        //         echo '=========================================== 4. Deploying image to ECR ==========================================='
        //         script{
        //             docker.withRegistry("https://" + "006262944085.dkr.ecr.eu-west-2.amazonaws.com/v2-ecr", "ecr:eu-west-2:" + "portfoliocredentials") {
        //                 dockerImage.push()
        //             }
        //         }
        //         echo '=========================================== 4. END =============================================================='
        //     }
        // }

        // stage('Update K8S') {
        //     steps {
        //         echo '=========================================== 5. Updating image tag ==========================================='
        //         sh """
        //             echo "$BUILD_NUMBER" > build_number.txt
        //         """
        //         echo '=========================================== 5. END =============================================================='
        //     }
        // }
    }
}