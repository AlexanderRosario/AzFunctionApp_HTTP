# Load libraries
from azure.storage.blob import BlobClient
# Define parameters
connectionString = ""
containerName = ""
outputBlobName	= ""


def upload_blob(dataset):
    blob = BlobClient.from_connection_string(conn_str=connectionString, container_name=containerName, blob_name=outputBlobName)
    
    # with open(dataset, "rb") as data:
    blob.upload_blob(dataset)
    return True

