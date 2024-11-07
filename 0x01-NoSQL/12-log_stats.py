#!/usr/bin/env python3
'''Task 12's module.
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for i in methods:
        req_count = len(list(nginx_collection.find({'method': i})))
        print('\tmethod {}: {}'.format(i, req_count))
    checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(checks_count))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    cli = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(cli.logs.nginx)


if __name__ == '__main__':
    run()