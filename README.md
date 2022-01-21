# VisualMenu
This library makes it easy to create a beautiful visual menu. <br/><br/>
![screen](https://user-images.githubusercontent.com/72179940/150559924-be17458d-64be-4336-a6f3-a9b94523ef0c.png)
## Installation
To use, download the archive, transfer the contents from the «VisualMenu-main» folder. The "readme.md" and "example.py" files can be deleted. You also need to install the [colorama](https://pypi.org/project/colorama/) library
## Documentation
### Import
To import a library write:
```
import VisualMenu
```
---
### Menu class
#### Arguments
* title (type: str) - The title of the instance. Shown on top of all tabbed items. Also displayed as a submenu item.
* description (type: str) - Description of the instance. Shown above the title. It is also displayed to the right of the submenu item. Initially None.
* display_descript (type: bool) - If False is passed, the submenu description will be hidden. Initially True.
* active (type: bool) - If False is passed, the submenu item will be disabled. Initially True.
* color (type: colorama) - The color of the cursor in the menu. Originally colorama.Fore.CYAN.
* events (type: list) - List of instances. Initially None.
#### Functions
* Enable() - Activates the menu and creates a loop.
* Disable() - Closes the menu loop.
* add_event(*events) - Adds instances to the menu.
* del_event(*events) - Removes instances from the menu.
---
### Event class
#### Arguments
* title (type: str) - The title of the instance. Shown on top of all tabbed items. Also displayed as a submenu item.
* description (type: str) - Description of the instance. Shown above the title. It is also displayed to the right of the submenu item. Initially None.
* display_descript (type: bool) - If False is passed, the submenu description will be hidden. Initially True.
* active (type: bool) - If False is passed, the submenu item will be disabled. Initially True.
* function (type: function) - The function to call.
* agrs (type: list) - Arguments to pass to the function. Initially None.
#### Functions
* Enable() - Activates the event.
## Information
If you need to contact me, this is my email - sw3atyspace@gmail.com. You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCkAldFCFSeFz1h61lHv4t6Q) and join my [Discord Server](https://discord.gg/jchJKYqNmK)
discord server -
