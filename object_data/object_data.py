from waapi import WaapiClient
from pprint import pprint
import ctypes


def selected_object_id():
    # Get user's selected object data in Wwise
    client = WaapiClient()
    selected_object = client.call('ak.wwise.ui.getSelectedObjects')

    info = str(selected_object.get('objects')[0].get('id'))

    client.disconnect()
    return info


def get_object_info(object_id):
    string_id = object_id
    client = WaapiClient()

    args = {
        "from": {"id": [string_id]}
    }

    options = {
        "return": ['id', 'name', 'type', 'notes']
        #"return": ['id', 'path', 'parent', 'name', 'type', 'notes']
    }

    object_data = client.call("ak.wwise.core.object.get", args, options=options)

    client.disconnect()

    return object_data.get('return')[0]


if __name__ == '__main__':
    info = get_object_info(selected_object_id())
    pprint(str(info))
    #ctypes.windll.user32.MessageBoxW(0, str(info), "Object Info", 0)
    pass
