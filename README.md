# vishhhl library
This library makes it easy to create a beautiful visual menu in the console. Based on the VisualMenu library. <br/><br/>
![image](https://github.com/Sw3aty-Acc/vishhhl/assets/72179940/3c6019a4-fa13-4ba6-98ca-51caa3e58027)

## Documentation
### Installation
To use, download and unzip the archive. Then move the «vishhhl» folder to your project
#### Required libraries:
* [colorama](https://pypi.org/project/colorama/) library.

### Import
To import a library write:
```
import vishhhl
```
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
Email - sw3atyspace@gmail.com \
YouTube - [Sw3aty](https://www.youtube.com/@sw3aty702) \
Discord Server - [swet-gaang](https://discord.gg/jchJKYqNmK)
