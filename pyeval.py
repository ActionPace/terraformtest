x="""[
  {
    "host_id" : "slave00",
    "private_ip" : "172.30.0.87",
    "public_ip" : "34.228.27.164"
  },
  {
    "host_id" : "slave01",
    "private_ip" : "172.30.0.134",
    "public_ip" : "18.205.17.31"
  },
]"""

aws_instance=eval(x)

print(aws_instance[1]["host_id"])
