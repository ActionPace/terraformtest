#from terraforminv import *
from terraforminvstruct import aws_instance

key="ansible_private_key_file=/home/ubuntu/.ssh/Ansible1.pem"

for i in aws_instance:
  print("["+i[0]+"]")
  for j in i[1]:
    print(j["host_id"]+" ansible_host="+j["public_ip"])
  print("")

for i in aws_instance:
  print("["+i[0]+":vars]")
  print("ansible_user=ubuntu")
  print("host_key_checking=false")
  print("ansible_ssh_common_args='-o StrictHostKeyChecking=no'")
  print("")
