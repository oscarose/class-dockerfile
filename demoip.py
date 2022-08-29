import boto3
import json
import sys

#clusterId = "$clusterid"
#n = sys.argv[1]
#clusterid = sys.argv[1]
clusterid = sys.argv[1]
aws_region = sys.argv[2]

boto_client_emr = boto3.client("emr")
#cluster_id = "j-2HKXRXB0RI02U"
cluster_id = clusterid

def get_emr_master_pub_ip(boto_client_emr, cluster_id, aws_region):
    emr_list_instance_rep = boto_client_emr.list_instances(
        ClusterId=cluster_id,
        InstanceGroupTypes=[
            'MASTER',
        ],
        InstanceStates=[
            'RUNNING',
        ]
    )

    return emr_list_instance_rep["Instances"][0]["PublicIpAddress"]
emr_master_ip = get_emr_master_pub_ip(boto_client_emr, cluster_id)
print("EMR master public IP is" + " " + emr_master_ip)


def get_emr_master_pvt_ip(boto_client_emr, cluster_id):
    emr_list_instance_rep = boto_client_emr.list_instances(
        ClusterId=cluster_id,
        InstanceGroupTypes=[
            'MASTER',
        ],
        InstanceStates=[
            'RUNNING',
        ]
    )

    return emr_list_instance_rep["Instances"][0]["PrivateIpAddress"]
emr_master_ip = get_emr_master_pvt_ip(boto_client_emr, cluster_id)
print("EMR master private IP is" + " " + emr_master_ip)
