#aws_instance = [
#  {
#    "host_id" : "slave00",
#    "private_ip" : "172.30.0.87",
#    "public_ip" : "34.228.27.164",
#  },
#  {
#    "host_id" : "slave01",
#    "private_ip" : "172.30.0.134",
#    "public_ip" : "18.205.17.31",
#  }
#]

#print(aws_instance[0]["host_id"])

x=0
with open("ansibleout.txt") as f:
  for line in f:
    line = line.replace("\n", "")
    if x:
      if ("=" in oldline) and (not "[" in oldline):
        oldline = oldline.replace("=", ":")
        if not "}," in line:
          oldline = oldline + ","
      print(oldline)  
    x=1
    oldline = line
  if not "aws_security_group" in line: 
    print(line)
