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
            #print(f'selected object name: {fetched_info}')
            #ctypes.windll.user32.MessageBoxW(0, str(fetched_info), "Object Info", 0)
    if param_str == 'id':
        for wwise_object in selected_objects.get('objects'):
            fetched_info = str(wwise_object.get('id'))
            #print(f'selected object id: {fetched_info}')
            #ctypes.windll.user32.MessageBoxW(0, str(fetched_info), "Object Info", 0)
    if param_str == 'parent':
        for wwise_object in selected_objects.get('parent'):
            fetched_info = str(wwise_object.get('parent'))
            #print(f'selected object id: {fetched_info}')

    client.disconnect()
    return fetched_info


def make_event():

    args = {
        "parent": "\\Events\\Default Work Unit",
        "type": "Folder",
        "name": "_ampCommands",
        "onNameConflict": "merge",
        "children": [
            {
                "type": "Event",
                "name": f"{selected_object_info('name')}_loop",
                "children": [
                    {
                        "name": "Play",
                        "type": "Action",
                        "@ActionType": 1,
                        "@Target": selected_object_info("id")

                    },
                    {
                        "name": "Seek",
                        "type": "Action",
                        "@ActionType": 36,
                        "@Target": selected_object_info("id"),

                    }

                ]
            }
        ]
    }

    client = WaapiClient()
    new_object = client.call("ak.wwise.core.object.create", args)
    client.disconnect()

    # set randomizer for seek

    # event id new_object.get("children")[0].get("id")
    # property SeekPercent
    # platform new_object.get("children")[0].get("children")[1].get("id")
    #pprint(new_object)
    rand_args = {
        "object": new_object.get("children")[0].get("children")[1].get("id"),
        "property": "SeekPercent",
        "enabled": True,
        "min": 0,
        "max": 100

    }
    print(rand_args.get("object"))
    client = WaapiClient()
    client.call("ak.wwise.core.object.setRandomizer", rand_args)
    client.disconnect()




# get selected container
# make an event with the name of the object + _loop ✅
# make another event with the name of the object + _loop_stop
# play event should have these actions: play for the container, seek for the container w/ seek % at 100 random offset
# stop event should have the stop action
# fades for both play and stop

if __name__ == '__main__':
    #info = selected_object_info("id")
    make_event()