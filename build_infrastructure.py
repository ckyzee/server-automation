#!/usr/bin/env python3
import boto3
import xlrd

def create_instances():
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
    ImageId='ami-097834fcb3081f51a',
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.2xlarge')
    print (instance[0].id)
    instance_id = list_instances()
    if instance_id != None:
        continue
    else:
        create_instances()
    return instance_id


def list_instances():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        print (instance.id, instance.state)
    return (instance.id, instance.state)

def terminate_instances(instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    print (response)

def configure_credentials():
    file = xlrd.open_workbook("./accessKeys.csv.xlsx") 
    sheet = file.sheet_by_index(0) 
    sheet.cell_value(0, 0) 
    keys = sheet.row_values(1)
    region = raw_input("Enter the Region:")
    os.system('aws configure')
    os.system(keys[0])
    os.system(keys[1])
    os.system(region)
    os.system("text")

configure_credentials()
instance_id = create_instances()
        
# This doesn't work globally, figuring out ansible
os.system('pkg install git')
os.system('cd')
os.system('mkdir src')
os.system('cd src')
os.system('git clone https://github.com/_your_userid_/freebsd')
os.system('cd freebsd')
os.system('make -j8 buildworld buildkernel packages')
os.system('scp')

terminate_instances(instance_id)