# vishhhl library
This library makes it easy to create a beautiful visual menu in the console. Based on the VisualMenu library. <br/><br/>
![image](https://github.com/Sw3aty-Acc/vishhhl/assets/72179940/e2a6d311-35e3-4236-9444-b0110bdc90c0)

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
### Menu class (Parent: Event class)
#### Arguments
* title (type: str) - Instance name. Displayed on top of all elements.
* desc (type: str) - Description of the instance. Shown above the title.
#### Functions
* changeTitle() - Changes the menu name.
* changeDesc() - Changes the menu description.
* enable() - Activates the menu and creates a loop.
* disable() - Closes the menu loop.
* addEvent(*events, index) - Adds instances to the menu.
* delEvent(*events) - Removes instances from the menu.

### Option class (Parent: Event class)
#### Arguments
* text (type: str) Instance name.
* desc (type: str) - Description of the instance. Shown above the title. It is also displayed to the right of the submenu item. Initially None.
* obj_menu (type: object) - Menu object to call.
* color (type: colorama) - Color of the cursor in the menu.

### Event class
#### Arguments
* text (type: str) Instance name.
* desc (type: str) - Description of the instance. Shown above the title. It is also displayed to the right of the submenu item. Initially None.
* func (type: object) The function to call.
* args (type: list) Arguments to pass to the function.
#### Functions
* enable() - Activates the event.
## Information
Email - sw3atyspace@gmail.com \
YouTube - [Sw3aty](https://www.youtube.com/@sw3aty702) \
Discord Server - [swet-gaang](https://discord.gg/jchJKYqNmK)
