import boto3

bucket_name = input("enter the bucket name:").split()

client = boto3.client("s3")
try:
    for name in bucket_name:

        response = client.list_objects_v2(
                    Bucket = name
        )
        if "Contents" in response:
            for object in response["Contents"]:
                client.delete_object(
                    Bucket = name,
                    Key = object["Key"]
                )
        client.delete_bucket(
            Bucket = name

        )
        print(f"{name} deleted")

except Exception as e:
    print(f"error occured {e}")