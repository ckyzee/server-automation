#!/usr/bin/env python3
import boto3
import xlrd 

def create_instances(ami_image_id, instance_type):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
    ImageId=ami_image_id,
    MinCount=1,
    MaxCount=1,
    InstanceType=instance_type)
    print (instance[0].id)

def list_instances():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
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

do {
    create_instances (ami-097834fcb3081f51a, t3.2xlarge)
    instance_id = list_instances()
} while ( list_instances() = None )

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