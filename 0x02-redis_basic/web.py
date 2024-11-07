#!/usr/bin/env python3
'''Module for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''Redis instance for caching and tracking.
'''


def data_cacher(method: Callable) -> Callable:
    '''Caches the result of data fetching.
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''Wrapper function that caches the output.
        '''
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Fetches and caches the content of a URL.
    '''
    return requests.get(url).text
