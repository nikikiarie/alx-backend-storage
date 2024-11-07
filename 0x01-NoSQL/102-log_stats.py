#!/usr/bin/env python3
'''Task 15's module.
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for i in methods:
        count = len(list(nginx_collection.find({'method': i})))
        print('\tmethod {}: {}'.format(i, count))
    checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(checks_count))


def print_top_ips(server_collection):
    '''Prints statistics about the top 10 HTTP IPs in a collection.
    '''
    print('IPs:')
    logs = server_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for i in logs:
        ip = i['_id']
        req_num = i['totalRequests']
        print('\t{}: {}'.format(ip, req_num))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    cli = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(cli.logs.nginx)
    print_top_ips(cli.logs.nginx)


if __name__ == '__main__':
    run()
