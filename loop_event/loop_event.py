from waapi import WaapiClient
from pprint import pprint




def make_event():
    # Get user's selected object data in Wwise
    client = WaapiClient()

    args = {
        "parent": "\\Actor-Mixer Hierarchy\\Default Work Unit",
        "type": "Sound",
        "name": "Boom"
    }

    client.call("ak.wwise.core.object.create", args)

    client.disconnect()


if __name__ == '__main__':
    print(make_event())
    pass
