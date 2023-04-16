if __name__ != '__main__':
    print(f'error: {__file__} should not be imported, aborting script')
    exit(1)

# this is a third-party lib
import pyperclip
# a simple function that returns arguments in argv as list
# note the use of a relative import because there's a 'helpers' submodule
from helpers import get_selected_guids_list

guids = get_selected_guids_list()
pyperclip.copy(' '.join(guids))