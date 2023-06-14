from src.connection import trends_collection
from src.constants import BRAZIL_WOE_ID
from src.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from src.secrets import CONSUMER_KEY, CONSUMER_SECRET
from typing import List, Dict, Any
import tweepy


def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:
    """Get treending topics from Twitter API.
    Args:
        woe_id (int): Identifier of location.
    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    trends = api.trends_place(woe_id)

    return trends[0]["trends"]


def get_mongos_trends() -> List[Dict[str, Any]]:
    """Gat trending topcs
    Args:
        woe_id (int): Location Identifier
    Returns:
        List[Dict[str, any]]: Trends List
    """
    trends = trends_collection.find({})

    return list(trends)


def save_trends() -> None:
    """Get trends topics and save on MongoDB."""
    auth = tweepy.OAuth1UserHandler(consumer_key=CONSUMER_KEY,
                                    consumer_secret=CONSUMER_SECRET,
                                    access_token=ACCESS_TOKEN,
                                    access_token_secret=ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = _get_trends(woe_id=BRAZIL_WOE_ID, api=api)
    trends_collection.insert_many(trends)
