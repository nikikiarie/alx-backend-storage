#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    # get number of documents in collection
    num_docs = logs.count_documents({})
    num_get = logs.count_documents({'method': 'GET'})
    post_num = logs.count_documents({'method': 'POST'})
    put_num = logs.count_documents({'method': 'PUT'})
    patch_num = logs.count_documents({'method': 'PATCH'})
    delete_num = logs.count_documents({'method': 'DELETE'})
    get_status = logs.count_documents({'method': 'GET',
                                             'path': '/status'})
    print("{} logs".format(num_docs))
    print("Methods:")
    print("\tmethod GET: {}".format(num_get))
    print("\tmethod POST: {}".format(post_num))
    print("\tmethod PUT: {}".format(put_num))
    print("\tmethod PATCH: {}".format(patch_num))
    print("\tmethod DELETE: {}".format(delete_num))
    print("{} status check".format(get_status))
