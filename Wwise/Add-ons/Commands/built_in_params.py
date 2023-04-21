from waapi import WaapiClient
from pprint import pprint
import ctypes


def make_wu():
    args = {
        "parent": "\\Game Parameters",
        "type": "WorkUnit",
        "name": "BuiltInParameters",
        "onNameConflict": "merge",
    }

    client = WaapiClient()
    client.call("ak.wwise.core.object.create", args)
    client.disconnect()


def setup_built_in_parameters():
    make_wu()

    parameters = [
        {"name": "distance_5000", "type": "1", "max": "5000"},
        {"name": "distance_10000", "type": "1", "max": "10000"},
        {"name": "distance_20000", "type": "1", "max": "20000"},
        {"name": "distance_50000", "type": "1", "max": "50000"},
        {"name": "azimuth", "type": "2"},
        {"name": "elevation", "type": "3"},
        {"name": "emitter_cone", "type": "4"},
        {"name": "obstruction", "type": "5"},
        {"name": "occlusion", "type": "6"},
        {"name": "listener_cone", "type": "7"},
    ]
    client = WaapiClient()
    for param in parameters:
        args = {
            "parent": "\\Game Parameters\\BuiltInParameters",
            "type": "GameParameter",
            "name": param.get("name"),
            "onNameConflict": "merge",
            "@BindToBuiltInParam": param.get("type"),
            "@Max": param.get("max"),

        }
        new_object = client.call("ak.wwise.core.object.create", args)
    client.disconnect()


if __name__ == '__main__':
    setup_built_in_parameters()
