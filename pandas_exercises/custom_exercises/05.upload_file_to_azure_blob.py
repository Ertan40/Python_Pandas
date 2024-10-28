## How to upload file to Azure Blob
# Installing required package: pip install azure-storage-blob
# Go to Azure and create storage account with the desired name

import os
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError

# Environment variables for sensitive information
storage_account_name = os.getenv('AZURE_STORAGE_ACCOUNT_NAME', 'your_account_name')
storage_account_key = os.getenv('AZURE_STORAGE_ACCOUNT_KEY', 'your_account_key')
connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING', "your_connection_string")


# Create a container in Azure Blob Storage.
def create_container(container_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.create_container(container_name)
        print(f"Successfully created a container: {container_name}")
    except ResourceExistsError:
        print(f"Container '{container_name}' already exists.")
    except Exception as e:
        print(f"Failed to create container: {e}")


# Upload a file to Azure Blob Storage.
def upload_file_to_blob(file_path, file_name, container_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print(f"Uploaded a file with the name: {file_name} to container: {container_name}")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except ResourceNotFoundError:
        print(f"The container '{container_name}' does not exist.")
    except Exception as e:
        print(f"Failed to upload file: {e}")


# Usage
container_name = 'fileholder'
create_container(container_name)
upload_file_to_blob('C:\\Users\\ertan\\Downloads\\beekeeper.jpg', 'beekeeperImage.jpg', container_name)





