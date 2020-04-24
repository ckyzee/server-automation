#!/usr/bin/env python3
import boto3
import os

def create_instances():
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
    ImageId='ami-097834fcb3081f51a',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')
    print (instance[0].id)
    instance_id = list_instances()
    if instance_id == None:
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
    file = open("~/.aws-credentials", "r")
    access_key = file.readline()
    secret_key = file.readline()
    file.close()

    region = input("Enter the Region:")
    os.system('aws configure')
    os.system(access_key)
    os.system(secret_key)
    os.system(region)
    os.system("text")

configure_credentials()

instance_id = create_instances()