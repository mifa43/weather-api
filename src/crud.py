from curses import flash
from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers
import time
from elasticsearch.exceptions import ConnectionError
from datetime import datetime
import csv
import json
import pyarrow.parquet as parquet
import pandas
import pyarrow as pa

#main class
class ElasticClass():
    def __init__(self) -> None:
        self.es = es = Elasticsearch(host="elastic_container", port= "9200", connection_class=RequestsHttpConnection, max_retries=30,
                       retry_on_timeout=True, request_timeout=30)
