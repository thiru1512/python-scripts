import boto3
def create_bucket():
    client = boto3.client("s3")
    bucket_name = input("enter the bucket name:").split()
    for name in bucket_name:
        try:
                response = client.create_bucket(
                Bucket = name
                )
                print(f"Bucket '{name}' has been created successfully.")
        except Exception as e:
            print(f"{e}error in bucket name ")
            continue


create_bucket()

