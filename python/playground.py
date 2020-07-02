class Point(object):
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long


def one_function(name):
    """
    >>> one_function('black')
    'received Black'
    """
    return "received {0}".format(name.title)


def locate(latitude: float, longitude: float) -> Point:
    """Find an object in the map by its coordinates"""


print(locate.__annotations__)


# Better documentation
def data_from_response(response: dict) -> dict:
    """If the response is OK, return itspayload.

    - response: A dict like:

    {
        "status" : 200 #<int>
        "timestamp": "...." # ISO format string of the current date time
        "payload" : { ... } # dict with the returned data
    }

    - Raises:
    - ValueError if the HTTP status is != 200
    """
    if response["status"] != 200:
        raise ValueError
    return {"data": response["payload"]}


print(help(data_from_response))
