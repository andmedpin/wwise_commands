from waapi import WaapiClient
from pprint import pprint
import ctypes


def selected_object_info(parameter):
    param_str = parameter
    client = WaapiClient()
    selected_objects = client.call('ak.wwise.ui.getSelectedObjects')

    if param_str == 'name':
        for wwise_object in selected_objects.get('objects'):
            fetched_info = wwise_object.get('name')
            print(f'selected object name: {fetched_info}')
            ctypes.windll.user32.MessageBoxW(0, str(fetched_info), "Object Info", 0)
    if param_str == 'id':
        for wwise_object in selected_objects.get('objects'):
            fetched_info = str(wwise_object.get('id'))
            print(f'selected object id: {fetched_info}')
    if param_str == 'parent':
        for wwise_object in selected_objects.get('parent'):
            fetched_info = str(wwise_object.get('parent'))
            print(f'selected object id: {fetched_info}')

    client.disconnect()
    return fetched_info


if __name__ == '__main__':
    info = selected_object_info("name")