pipeline {
    agent {
        label 'Jenkins'
    }
    parameters {
        choice(name:'aws_region', choices: ['us-east-1', 'us-west-2'], description: 'aws region to deploy',)
        string(name: 'stack_name', defaultValue: '', description: 'name of cft stack',)
        choice(name:'state', choices: ['present', 'absent'], description: 'cft build or teardown condition',)
        choice(name:'environment', choices: ['QA', 'DEV'], description: 'cft deploy environment',)
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
                withAWS(credentials: 'aws-cred') {
                //withAWS(credentials: 'aws-cred', region: '${aws_region}') {
                    sh """
                    aws s3 ls
                    """
                }
            }
        }
    }
}
