pipeline {
    agent {
        label 'Jenkins'
    }
    parameters {
        choice(name:'aws_region', choices: ['us-east-1', 'us-west-2'], description: 'aws region to deploy',)
        string(name: 'stack_name', defaultValue: '', description: 'name of cft stack',)
        string(name: 'cluster_name', defaultValue: '', description: 'emr cluster name',)
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
                    sh '''#!/bin/bash
                    aws s3 ls
                    python3 --version
                    clusterid=$(python3 ${WORKSPACE}/demoid.py ${aws_region} ${cluster_name} | grep j) 
                    echo $clusterid
                    python3 ${WORKSPACE}/demoip.py $clusterid ${aws_region}
                    '''
                }
            }
        }
    }
}
