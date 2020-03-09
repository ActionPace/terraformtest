terraform {
  required_version = ">=0.12.0"
}

provider "aws" {
  version = "~> 2.0"
  region  = "us-east-1"
}

data "aws_security_group" "selected" {
  #id = "sg-de4fd9a5"
  name = "All Traffic Anywhere"
}

variable "name_counts" {
  type    = map(number)
  default = {
    "master" = 1
    "slave" = 2
  }
}

locals {
  expanded_names = {
    for name, count in var.name_counts : name => [
      for i in range(count) : format("%s%02d", name, i)
    ]
  }
}

#output "expanded_names" {
#  value = local.expanded_names["slave"]
#}

resource "aws_instance" "cluster1" {
  for_each = toset(local.expanded_names["slave"])
  ami = "ami-08bc77a2c7eb2b1da"
  instance_type = "t2.nano"
  #key_name = "Spark1"
  key_name = "Ansible1"
  #https://github.com/hashicorp/terraform/issues/575
  security_groups = ["${data.aws_security_group.selected.id}"]
  subnet_id = "subnet-29347a5f"
  tags = {
    Name = each.value
  }
  #provisioner "local-exec" {
  #command = "echo ${aws_instance.cluster[each.value].private_ip} >> private_ips.txt"
  #}

}

resource "aws_instance" "cluster" {
  for_each = toset(local.expanded_names["master"])
  ami = "ami-08bc77a2c7eb2b1da"
  instance_type = "t2.nano"
  #key_name = "Spark1"
  key_name = "Ansible1"
  #https://github.com/hashicorp/terraform/issues/575
  security_groups = ["${data.aws_security_group.selected.id}"]
  subnet_id = "subnet-29347a5f"
  tags = {
    Name = each.value
  }

}

#data "aws_security_group" "selected" {
#  #id = "sg-de4fd9a5"
#  name = "All Traffic Anywhere"
#}
#output "aws_security_group" {
#  #value = data.aws_security_group.selected.name
#  value = data.aws_security_group.selected.id
#}
output "aws_instance" {
  value = [for x in ["master","slave"]: [x,[for v in toset(local.expanded_names[x]):
     {"host_id" = "${v}"
     "private_ip" = "${x == "master" ? aws_instance.cluster[v].private_ip:aws_instance.cluster1[v].private_ip}"
    "public_ip" = "${x == "master" ? aws_instance.cluster[v].public_ip:aws_instance.cluster1[v].public_ip}"}
]]]
}
