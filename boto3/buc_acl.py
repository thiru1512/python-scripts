import boto3

client = boto3.client("s3")

response = client.get_bucket_acl(
    Bucket = "thiru-devops-1989-1512"

)

print(response)