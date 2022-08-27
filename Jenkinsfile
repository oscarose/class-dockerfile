pipeline {
    agent {
        label 'Jenkins'
    }
    stages {
        stage('clone git repo') {
            steps {
                git branch: 'master',
                    credentialsId: 'git-cred',
                        url: 'https://github.com/oscarose/class-dockerfile.git'
            }            
        }
        stage('aws services') {
            steps {
                withAWS(credentials: 'aws-cred', region: 'us-east-1') {
                    sh """
                    aws s3 ls
                    """
                }
            }
        }
        /*stage('deploy cft') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-cred', accessKeyVariable: 'access_key_id', secretKeyVariable: 'secret_access_key']]) {
                    script {
                        sh '''
                        aws ls
                        aws cloudformation ls
                        //aws s3 ls
                        '''
                    }
                }
            }
        */}
    }
}
