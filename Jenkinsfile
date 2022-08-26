pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('clone git repo') {
            steps {
                git branch: 'master',
                    credentialsId: 'git-cred',
                        url: 'https://github.com/oscarose/class-dockerfile.git'
            }            
        }
    }
}
