from filestack import Client

client = Client("AymSxZ6H6QvajbIPFI0HZz")

store_params = {
    "location": "s3",
    "path": "folder/subfolder/",
    "upload_tags": {"foo": "bar"},
}


def file_link(file):
    print("Link to your file here: ")
    filelink = client.upload(filepath=file, store_params=store_params)
    print(filelink.url)
