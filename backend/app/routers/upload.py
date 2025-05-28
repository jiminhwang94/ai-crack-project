# routers/upload.py
from fastapi import APIRouter, UploadFile, File
from azure.storage.blob import BlobServiceClient
import os, uuid

router = APIRouter()

@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_CONTAINER_NAME")

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=str(uuid.uuid4()) + "-" + file.filename)

    contents = await file.read()
    blob_client.upload_blob(contents, overwrite=True)

    blob_url = blob_client.url
    return {"url": blob_url}
