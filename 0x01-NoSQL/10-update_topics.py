#!/usr/bin/env python3
"""
change school topic
"""


def update_topics(mongo_collection, name, topics):
    """
    update many rows
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
