import json
import argparse

from ActionButtonBuilder import build_action_button
from PyinstallerUtils import resource_path

default_platform_icon = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAZCAYAAADaILXQAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGnSURBVEhL1ZZNqwFhGIbfOT9t+BXKQikhZqWQjbWFlYWlrZSmfCxsFNnZKJb+gCgfIR89x/M+z5thzIyPnDpXaXKV657MjGhwQXyJHz5+hb+ND4dD+bpntVqJarUqzuczG29s8Xa7LdLptOj3+2yI6XQqyuWyyOfzzw/gBbWy2+0gmUyC3++HXq/HljBNE3Rdh0wmA6fTia0ztjiCA7FYzHPgeDyyfczDOLLdbj0HUqmU64BjHPl0wDWOfDLgGUfeHXgqjrwz8HQcwYFEIgE+nw8GgwFbol6vy4FcLscG4OXHHx+gy+fEfD5nQ2iaJo+z2UweJbThDZ51NBqVZ1csFtkSjUZD+kAgAJc42xcuqAqXSiW2hAoHg0FYLBZsCc+4NVypVNgSKhwKhWC5XLK94hq3hmu1GltChcPhMKzXa7a3OMatYbzVrKhwJBKBzWbD1s7DuDXcarXYEiocj8flD5wbtrgK473c6XTYEipsGAbs93u2ztjihUJBPoXdbpcNMZlMZDibzcLhcGDrji0+Go1gPB7zuyv4FTSbTdef2Hv+618LIX4BTJynSpugjsoAAAAASUVORK5CYII="


def make_card():
    parser = argparse.ArgumentParser(description="Parse UI customization parameters, " \
        "build adaptive card and send request to webhook")


    parser.add_argument('--webhook', default="")
    parser.add_argument('--project_name_breadcrumb_navbar', default="Build Pipeline")
    parser.add_argument('--project_url_breadcrumb_navbar', default="http://127.0.0.1")
    parser.add_argument('--text_headline_large', default="")
    parser.add_argument('--status_text_row_wide', default="")
    parser.add_argument('--status_text_row_narrow', default="")
    parser.add_argument('--date_time_string_wide', default="")
    parser.add_argument('--date_time_string_narrow', default="")
    parser.add_argument('--revision_number_string_wide', default="")
    parser.add_argument('--revision_number_string_narrow', default="")
    parser.add_argument('--optional_note_richtextblock', default="")
    parser.add_argument('--button_left_url', default="")
    parser.add_argument('--button_left_icon', default="")
    parser.add_argument('--button_left_text', default="")
    parser.add_argument('--button_right_icon', default="")
    parser.add_argument('--button_right_text', default="")
    parser.add_argument('--button_right_url', default="")
    parser.add_argument('--target_platform_string_wide', default="")
    parser.add_argument('--target_platform_string_narrow', default="")
    parser.add_argument('--target_platform_icon_url_wide', default=default_platform_icon)
    parser.add_argument('--target_platform_icon_url_narrow', default=default_platform_icon)

    args = parser.parse_args()

    bUseButtonLeft = True
    bUseButtonRight = True
    bUseButtonIconLeft = True
    bUseButtonIconRight = True

    if getattr(args, "button_left_url") == "" and \
        getattr(args, "button_left_text") == "" and \
        getattr(args, "button_left_icon") == "":
        bUseButtonLeft = False

    if getattr(args, "button_right_text") == "" and \
        getattr(args, "button_right_icon") == "" and \
        getattr(args, "button_right_url") == "":
        bUseButtonRight = False

    if getattr(args, "button_right_icon") == "":
        bUseButtonIconRight = False
    if getattr(args, "button_left_icon") == "":
        bUseButtonIconLeft = False

    # Example usage: print all parsed arguments
    for arg in vars(args):
        if arg in ["target_platform_icon_url_wide" , 
                   "target_platform_icon_url_narrow"] and \
            getattr(args, arg) == default_platform_icon:
            print(f"{arg}: [default_platform_icon]")
            continue
        print(f"{arg}: {getattr(args, arg)}")

    print(f"use buttom left: " + str(bUseButtonLeft) + 
          " , use buttom right: " + str(bUseButtonRight))

    if getattr(args, "webhook") == "":
        print("no webhook url provided, quitting....")
        exit(-1)

    webhook_url = getattr(args, "webhook")
    
    card_json = {}

    with open(resource_path('CardTemplate.json'), 'r') as fp:
        card_json_text = "\n".join(fp.readlines())
    

    # add action button template

    temp_card_json = json.loads(card_json_text)

    temp_card_json["body"].extend(build_action_button(bUseButtonLeft, bUseButtonRight, bUseButtonIconLeft, bUseButtonIconRight))

    card_json_text = json.dumps(temp_card_json)
    
    # start processing args


    args_dict = vars(args)
    placeholder_keys = [k for k in args_dict if k != "webhook"]
    replacements = {k.upper(): args_dict[k] for k in placeholder_keys}

    for key, value in replacements.items():
        placeholder = f"[{key.upper()}]"
        card_json_text = card_json_text.replace(placeholder, value)
    
    card_json = json.loads(card_json_text)



    return card_json , webhook_url


if __name__ == "__main__":
    print(make_card())