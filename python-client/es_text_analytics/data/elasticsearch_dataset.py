import re
import string
import tarfile

from es_text_analytics.data.dataset import Dataset
from elasticsearch.client import Elasticsearch
from elasticsearch.helpers import scan

"""
Elasticsearch as data source

"""


class ElasticsearchDataset(Dataset):
    """
    Class encapsulating using Elasticsearch as datasource. Uses scan/scroll API via the es-py helpers scan.
    """

    def __init__(self, read_index, read_doc_type, index='new_index', doc_type='doc', dataset_path=None):
        super(ElasticsearchDataset, self).__init__(index=index, doc_type=doc_type, dataset_path=dataset_path)
        self.dataset_fn = 'elastics'
        self.read_index = read_index
        self.read_doc_type = read_doc_type

    def _iterator(self):
        es = Elasticsearch(timeout=60)
        return scan(es, scroll=u'200m',
                    index=self.read_index, doc_type=self.read_doc_type)
