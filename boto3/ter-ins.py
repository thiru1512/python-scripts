import boto3 

client = boto3.client("ec2")

response = client.describe_instances(Filters=[{'Name': 'instance-state-name','Values': ['stopped']}])

for reservations in response["Reservations"]:
    for instance in reservations["Instances"]:
        instance_id = instance["InstanceId"]
        response = client.terminate_instances(InstanceIds =[instance_id])
        print(f"{instance_id} deleted")


