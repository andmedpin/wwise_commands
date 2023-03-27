from waapi import WaapiClient
from pprint import pprint


def selected_object_info(parameter):
    client = WaapiClient()
    selected_objects = client.call('ak.wwise.ui.getSelectedObjects')

    match parameter:
        case 'name':
            for wwise_object in selected_objects.get('objects'):
                fetched_info = str(wwise_object.get('name'))
                print(f'selected object name: {fetched_info}')
        case 'id':
            for wwise_object in selected_objects.get('objects'):
                fetched_info = str(wwise_object.get('id'))
                print(f'selected object id: {fetched_info}')
        case 'parent':
            for wwise_object in selected_objects.get('parent'):
                fetched_info = str(wwise_object.get('parent'))
                print(f'selected object id: {fetched_info}')

        case _:
            for wwise_object in selected_objects.get('objects'):
                fetched_info = str(wwise_object)
                print(f'selected object info: {fetched_info}')

    client.disconnect()
    return fetched_info


def make_event():
    # Get user's selected object data in Wwise

    args = {
        "parent": '\\Events\\Default Work Unit',
        "type": "Event",
        "name": selected_object_info('name')
    }

    client = WaapiClient()
    client.call("ak.wwise.core.object.create", args)

    client.disconnect()


if __name__ == '__main__':
    make_event()
    pass
