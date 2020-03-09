#from terraforminv import *
from terraforminvstruct import aws_instance

for i in aws_instance:
  print(i[0]+":")
  print("  "+i[0]+"s:")
  for j in i[1]:
    print("    - "+j["host_id"])
  for j in i[1]:
    print("  "+j["host_id"]+":")
    print("    "+"public_ip"+": "+j["public_ip"])
    print("    "+"private_ip"+": "+j["private_ip"])

