#from os import walk
#from os import path
#from os import environ
import os 
import requests
import mimetypes
import argparse

def put_container(name):
    global fedora_admin_user, fedora_admin_password
    relative_path = name.replace(files_root,"")
    url = "{}{}".format(fedora_url, relative_path)
    r = requests.put(url, auth=(fedora_admin_user,fedora_admin_password)) 
    print("[{}] [C] {}" .format(r.status_code, url))
    return

def put_file(name):
    global fedora_admin_user, fedora_admin_password
    relative_path = name.replace(files_root,"")
    filename = path.basename(name)
    (mt, enc) = mimetypes.guess_type(relative_path)
    if mt == None:
        mt = 'application/octet-stream'
    headers = { 'Content-type' : mt, 'Slug' : filename }
    url = "{}{}".format(fedora_url, relative_path)
    r = requests.put(url, auth=(fedora_admin_user,fedora_admin_password), headers=headers, data=open(name, 'rb')) 
    print("[{}] [F] {} {}" .format(r.status_code, mt, url))
    return

argparser = argparse.ArgumentParser()
argparser.add_argument('-p', '--project', help='project code e.g. PRJ-2972')
argparser.add_argument('-f', '--file_root', help='file path of data on disk. e.g. /fedora_storage')
args = argparser.parse_args()

print(os.environ)

fedora_url = os.environ['FEDORA_URL']
fedora_admin_user = os.environ['FEDORA_ADMIN_USER']
fedora_admin_password = os.environ['FEDORA_ADMIN_PASSWORD']
project = args.project
files_root = args.file_root
w = walk(path.join(files_root, project))

for (root, dirs, files) in w:
    for name in files:
        put_file(path.join(root, name))
    for name in dirs:
        put_container(path.join(root, name))

