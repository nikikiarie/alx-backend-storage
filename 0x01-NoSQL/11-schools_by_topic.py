#!/usr/bin/env python3
"""
find by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    find by topic
    """
    topics = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topics)]
