import boto3
client = boto3.client("emr")
response = client.list_clusters(
    ClusterStates=[
        'STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING', 'TERMINATING'
    ]
)
for cluster in response['Clusters']:
#    print(cluster['Name'])
    print(cluster['Id'])

