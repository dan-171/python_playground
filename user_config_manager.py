from msvcrt import getch

test_settings = {
    'Theme': 'Dark',
    'Fontsize': '16px'
}

def add_setting(settings: dict, new_setting: tuple) -> str:
    lowerTuple = (new_setting[0].lower(), new_setting[1].lower())
    if lowerTuple[0] in settings:
        return f"Setting '{lowerTuple[0]}' already exists! Cannot add a new setting with this name.\n"
    settings[lowerTuple[0]] = lowerTuple[1]
    return f"Setting '{lowerTuple[0]}' added with value '{lowerTuple[1]}' successfully!\n"

def update_setting(settings: dict, setting: tuple) -> str:
    lowerTuple = (setting[0].lower(), setting[1].lower())
    if lowerTuple[0] in settings:
        settings[lowerTuple[0]] = lowerTuple[1]    
        return f"Setting '{lowerTuple[0]}' updated to '{lowerTuple[1]}' successfully!\n"
    settings[lowerTuple[0]] = lowerTuple[1]
    return f"Setting '{lowerTuple[0]}' does not exist! Cannot update a non-existing setting.\n"

def delete_setting(settings: dict, setting_key: str) -> str:
    lowerKey = setting_key.lower()
    if lowerKey in settings:
        del settings[lowerKey]
        return f"Setting '{lowerKey}' deleted successfully!\n"
    return "Setting not found!\n"

def view_settings(settings: dict) -> str:
    if settings == {}:
        return "No settings available.\n"
    return f"Current User Settings:\n{"\n".join((f'{key.title()}: {value}' for key, value in settings.items()))}"

def main(settings: dict) -> None:
    while True:
        print("""
##User Configuation Manager##
Select an operation:
1: Add setting
2: Update setting
3: Delete setting
4: View setting
5: Quit
        """)
        op = input("Select an operation: ")
        if op == "1":
            newsetting = input("Setting name: ")
            newvalue = input("Setting value: ")     
            print(add_setting(test_settings, (newsetting, newvalue)))
        if op == "2":
            setting = input("Setting name: ")
            value = input("Setting value: ")     
            print(update_setting(test_settings, (setting, value)))
        if op == "3":
            setting = input("Setting name: ")
            print(delete_setting(test_settings, setting))
        if op == "4":
            print(view_settings(test_settings))
        if op == "5":
            print("Exiting user configuration manager...")
            return
        print("Press Enter to continue...")
        while getch() != b'\r':
            pass

main(test_settings)
