import boto3
import sys
aws_region = sys.argv[1]
cluster_name = sys.argv[2]
client = boto3.client("emr", aws_region)
response = client.list_clusters(
    ClusterStates=[
        'STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING', 'TERMINATING'
    ]
)
#for cluster in response['Clusters']:
#    print(cluster['Name'])
#    print(cluster['Id'])
matching_cluster_ids = list()

for cluster in response['Clusters']:
    if cluster_name == cluster['Name']:
        print(cluster['Id'])
      #  matching_cluster_ids.append(cluster['Id'])
