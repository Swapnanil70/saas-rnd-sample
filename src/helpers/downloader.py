import requests
from pathlib import Path

def download_to_local(url: str, local_path: Path, parent_mkdir: bool = True):
    """
    Downloads a file from the given URL and saves it to the specified local path.
    
    Args:
        url (str): The URL of the file to download.
        local_path (Path): The local path where the file will be saved.
        
    Raises:
        Exception: If the download fails or the response is not successful.
    """
    if not isinstance(local_path, Path):
        raise ValueError("local_path must be a Path object")

    if parent_mkdir:
        # Ensure the parent directory exists
        local_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Write the file out in binary mode
        local_path.write_bytes(response.content)
        
        print(f"Downloaded {url} to {local_path}")
        return True
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return False