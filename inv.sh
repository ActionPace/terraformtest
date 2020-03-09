#!/usr/bin/env bash
terraform output > ./ansibleout.txt
python terraformformat.py > ./terraforminvstruct.py
python makeansibleinv.py > ../playbooks2/hosts
python makeansiblevars.py > ../playbooks2/ansiblevarsout.yml
python makeansiblevars2.py > ../playbooks2/ansiblevars2out.yml
