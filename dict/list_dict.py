instance_info = [
    {
        "instance_id" : "instance-001",
        "type" : "t2.micro"
    },
    {
        "instance_id" : "instance-002",
        "type" : "t2.large"

    },
    {
        "instance_id" : "instance-003",
        "type" : "t2.medium"

    }
]
instance_info[2]["instance_id"] = "22"


print(instance_info[2]["instance_id"])