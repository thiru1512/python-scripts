import boto3

client = boto3.client("ec2")

response = client.describe_volumes()
print(response)

#for name in response["Volumes"]:
for name in response["Volumes"]:
    volume_id = name["VolumeId"]
    if not name["Attachments"]:
            response = client.delete_volume(VolumeId=volume_id)
            print(f"{volume_id} deleted")

        
        
