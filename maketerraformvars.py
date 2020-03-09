#from terraforminv import *
from terraforminvstruct import aws_instance

for i in aws_instance:
  print("variable \""+i[0]+"_host\" {")
  print("type = list(string)")
  print("default = [")
  for j in i[1]:
    print("\""+j["host_id"]+"\",")
  print("]")
  print("}")
  print("")
  print("variable \""+i[0]+"_ip\" {")
  print("type = list(string)")
  print("default = [")
  for j in i[1]:
    print("\""+j["private_ip"]+"\",")
  print("]")
  print("}")

