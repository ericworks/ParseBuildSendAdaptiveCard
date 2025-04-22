
import json
from PyinstallerUtils import resource_path


def build_action_button(enable_left_button:bool, enable_right_button: bool, has_icon_left: bool, has_icon_right: bool) -> list:

    if not enable_left_button and not enable_right_button:
        return []

    actionset = []
    with open(resource_path('ActionButtonTemplate.json'), 'r') as fp:
        actionset = json.load(fp)

    action_wide = actionset[0]
    action_narrow = actionset[1]

    if not has_icon_left:
        action_wide["actions"][0].pop("iconUrl")
        action_narrow["actions"][0].pop("iconUrl")
    if not has_icon_right:
        action_wide["actions"][1].pop("iconUrl")
        action_narrow["actions"][1].pop("iconUrl")        

    if not enable_right_button:
        action_wide["actions"].pop(1)
        action_narrow["actions"].pop(1)
    if not enable_left_button:
        action_wide["actions"].pop(0)
        action_narrow["actions"].pop(0)
    
    return [action_wide, action_narrow]

if __name__ == "__main__":
    print(build_action_button(True, False))