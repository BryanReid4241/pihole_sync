#! /user/bin/python3

import getpass
import argparse
import paramiko
import yaml

parser = argparse.ArgumentParser()

parser.add_argument('--config', dest='config', help='path to config where your dns servers are')
parser.add_argument('--password', dest='password')
parser.add_argument('--username', dest='username')
parser.add_argument('--hosts-file', dest='hostsfile')

args = parser.parse_args()

with open(args.config) as config_file:
    config = yaml.load(config_file, yaml.BaseLoader)

hostsfile = open(args.hostsfile)

if args.password:
    password = args.password
else:
    password = getpass.getpass()

for host in config['hosts']:
    print(f'Connecting to {host}')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username='root', password=password)

    sftp = ssh.open_sftp()
    sftp.put(args.hostsfile, '/etc/pihole/custom.list')
    sftp.close()
    ssh.close()