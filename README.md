# vishhhl library
This library makes it easy to create a beautiful visual menu in the console. Based on the VisualMenu library. <br/><br/>
![image](https://github.com/Sw3aty-Acc/vishhhl/assets/72179940/30a51dfc-c2e5-478f-8a08-d8ee8f82b6c3)

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
### Layer class (Parent: Event class)
#### Arguments
* title (type: str) - Instance name. Displayed on top of all elements.
* desc (type: str) - Description of the instance. Shown above the title.
* opt_list (type: list)
#### Functions
* changeTitle() - Changes the menu name.
* changeDesc() - Changes the menu description.
* addOption(*events, index) - Adds instances to the menu.
* delOption(*events) - Removes instances from the menu.
* delOptionByIndex(index) - Removes instances from a menu by index.
* update() - A function that runs in a loop.
* enable() - Activates the menu and creates a loop.
* disable() - Closes the menu loop.
#### Invisible functions
* mainLoop()
* decodeManager()
* printManager()
* fastInputManager()
* basicInputManager(pressedKey)
* basicInputManager(pressedKey)
* hookManager()

### Event class
#### Arguments
* text (type: str) Instance name.
* desc (type: str) - Description of the instance. Shown above the title. It is also displayed to the right of the submenu item. Initially None.
* func (type: object) - The function to call.
* args (type: list) - Arguments to pass to the function.
* color (type: colorama) - Color of the cursor in the menu.
#### Functions
* enable() - Activates the event.

### Menu class (Parent: Layer class)
#### Arguments
* title (type: str) - Instance name. Displayed on top of all elements.
* desc (type: str) - Description of the instance. Shown above the title.
* opt_list (type: list)

### Option class (Parent: Event class)
#### Arguments
* text (type: str) - Instance name.
* desc (type: str) - Description of the instance. Shown above the title. It is also displayed to the right of the submenu item. Initially None.
* obj_menu (type: object) - Menu object to call.
* color (type: colorama) - Color of the cursor in the menu.

## Information
Email - sw3atyspace@gmail.com \
YouTube - [Sw3aty](https://www.youtube.com/@sw3aty702) \
Discord Server - [swet-gaang](https://discord.gg/jchJKYqNmK)
