"""
ETL-Query script
"""
import fire
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

class QueryCLI:
    def extract(self):
        """Extract data from source"""
        extract()

    def transform_load(self):
        """Transform and load data into target"""
        load()

    def query(self, limit=5):
        """Query the target database for the top N rows"""
        query(limit)

if __name__ == '__main__':
    fire.Fire(QueryCLI)