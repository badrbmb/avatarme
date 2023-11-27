from pathlib import Path
from google.cloud.storage import Client, transfer_manager


class StorageClient:
    def __init__(self, client: Client | None = None) -> None:
        if client is None:
            client = Client()
        self.client = client

    def create_bucket(self, bucket_name: str):
        bucket = self.client.create_bucket(bucket_name)
        print(f"Bucket {bucket.name} created.")

    def upload_blob(
        self, bucket_name: str, source_file_name: str, destination_blob_name: str
    ):
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {destination_blob_name}.")

    def upload_directory(
        self,
        bucket_name: str,
        source_directory: Path,
        destination_directory: str,
        file_type: str = "*",
        workers: int = 8,
    ):
        bucket = self.client.bucket(bucket_name)

        file_paths = [
            path for path in source_directory.rglob(file_type) if path.is_file()
        ]
        string_paths = [str(path.relative_to(source_directory)) for path in file_paths]

        print(f"Found {len(string_paths)} files.")

        results = transfer_manager.upload_many_from_filenames(
            bucket,
            string_paths,
            source_directory=source_directory,
            blob_name_prefix=f"{destination_directory}/",
            max_workers=workers,
        )

        for name, result in zip(string_paths, results):
            if isinstance(result, Exception):
                print(f"Failed to upload {name} due to exception: {result}")
