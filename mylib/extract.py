"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats 

"""
import requests


def extract(
    url="https://anlane611.github.io/ids702-fall23/DAA/listings.csv",
    file_path="dataset/listings.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
