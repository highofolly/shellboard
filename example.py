from vishhhl import Menu, colorama, Event

volume = 100

def set_volume():
    global volume
    volume = input("\nEnter music volume: ")
    setting_music.description = f"Current {volume}"


menu = Menu("Menu", description=f"This is the {colorama.Fore.MAGENTA}vishhhl{colorama.Style.RESET_ALL} of version 0.2!")

start = Menu(title="Start", description="Function not active", active=False)

setting = Menu(title="Setting")
setting_music = Event("Music volume", set_volume, description=f"Current {volume}")
setting.add_event(setting_music)

information = Event(title="Information", function=input, args=["\nIf you need to contact me, this is my email - sw3atyspace@gmail.com.\nYou can also subscribe to my YouTube (https://www.youtube.com/channel/UCkAldFCFSeFz1h61lHv4t6Q)\nand join my Discord Server (https://discord.gg/jchJKYqNmK)"])

menu.add_event(start, setting, information)

while True:
    menu.Enable()
    ans = input("\nDo you really want to go out (Y/n) ").upper()
    if ans == "Y":
        break
