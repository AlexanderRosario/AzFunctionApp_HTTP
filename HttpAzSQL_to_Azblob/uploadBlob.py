# Load libraries
from azure.storage.blob import BlobClient
# import pandas as pd

# Define parameters
connectionString = ""
containerName = ""
outputBlobName	= ""

# Save the subset of the iris dataframe locally in task node
# df.to_csv(outputBlobName, index = False)

# with open(outputBlobName, "rb") as data:
#     blob.upload_blob(data)


def upload_blob(dataset):
    blob = BlobClient.from_connection_string(conn_str=connectionString, container_name=containerName, blob_name=outputBlobName)
    
    with open(dataset, "rb") as data:
        blob.upload_blob(data)
        return True