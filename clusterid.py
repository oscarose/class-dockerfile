import boto3
import sys
aws_region = sys.argv[1]
client = boto3.client("emr", aws_region)
response = client.list_clusters(
    ClusterStates=[
        'STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING', 'TERMINATING'
    ]
)
for cluster in response['Clusters']:
    print(cluster['Name'])
#    print(cluster['Name'])
    print(cluster['Id'])

