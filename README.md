# Fedora Ingest Tools

## Recursive Dumb Ingester
This tool will take a root directory and ingest all files and folders beneth it, maintaining the path structure as a hierachical container structure within Fedora 6

	usage: ingest.py [-h] [-p PROJECT] [-f FILE_ROOT]

	options:
	  -h, --help            show this help message and exit
	  -p PROJECT, --project PROJECT
				project code e.g. PRJ-2972
	  -f FILE_ROOT, --file_root FILE_ROOT
				file path of data on disk. e.g. /fedora_storage

## A Dockerfile is provided for convenience

### Secrets 
It requires 3 secrets to run. 
They can be added to your local container environment with:
	printf "mySecretHere" | sudo podman secret create fedora_admin_password -

They should be provided to the image as environment variables e.g.

	sudo podman run --secret fedora_admin_user,type=env,target=FEDORA_ADMIN_USER \
			--secret fedora_admin_password,type=env,target=FEDORA_ADMIN_PASSWORD \
			--secret fedora_url,type=env,target=FEDORA_URL \
			-it fedora_ingester \
			-p PRJ-2972 \
			-f /fedora_storage

Note podman is used here but docker could be used in its place with identical arguments
