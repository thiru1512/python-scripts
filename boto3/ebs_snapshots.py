import boto3 

client = boto3.client("ec2")

response  = client.describe_snapshots(OwnerIds=["self"])

instance_response = client.describe_instances(Filters=[{'Name': 'instance-state-name','Values': ['running']}])

active_instance_ids = set()

#print(instance_response)
#print(response)

for reservations in instance_response["Reservations"]:
    for instances in reservations["Instances"]:
        #print(instances["InstanceId"])
        active_instance_ids.add(instances["InstanceId"])
        #print(active_instance_ids)

for snapshot in response["Snapshots"]:

    snapshot_id = snapshot["SnapshotId"]
    volume_id = snapshot["VolumeId"]
    if not volume_id:
        client.delete_snapshot(SnapshotId=snapshot_id)
        print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")

    else:
        try:
            volume_response = client.describe_volumes(VolumeIds=[volume_id])
            if not volume_response['Volumes'][0]['Attachments']:
                client.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
        except client.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    client.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")



