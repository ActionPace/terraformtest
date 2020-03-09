aws_instance = [
  [
    "master",
    [
      {
        "host_id" : "master00",
        "private_ip" : "172.30.0.129",
        "public_ip" : "54.85.158.86"
      },
    ],
  ],
  [
    "slave",
    [
      {
        "host_id" : "slave00",
        "private_ip" : "172.30.0.52",
        "public_ip" : "34.224.102.70"
      },
      {
        "host_id" : "slave01",
        "private_ip" : "172.30.0.25",
        "public_ip" : "100.26.23.135"
      },
    ],
  ],
]

#print(aws_instance[0][1][0]["host_id"])
for i in aws_instance:
  print("["+i[0]+"]")
  for j in i[1]:
    print(j["host_id"]+" ansible_host="+j["public_ip"])
