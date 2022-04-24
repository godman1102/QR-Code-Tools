from urllib.request import urlopen
from getpass import getuser
from colorama import Fore, init
from os import system
import qrcode, cv2

init()

class Data:
    version = "v1.0.0"
    user_ip = str(urlopen("https://api.ipify.org").read().decode().strip())
    pc_username = getuser()
    clear = "cls"
    fill_color = "black"
    bg_color = "white"

def pause(new_lines:int=None):
    lines = ""
    if not new_lines is None:
        for i in range(1, new_lines):
            lines += "\n"
    print(Fore.CYAN)
    system("pause")
    print(Fore.RESET)

def get_qr_data(file:str, mode:str="value"):
    d = cv2.QRCodeDetector()
    reval, points, s_qr = d.detectAndDecode(cv2.imread(str(file)))
    if mode.lower() == "value":
        return reval

    elif mode.lower() == "points":
        return points

    elif mode.lower() == "s":
        return s_qr

    else:
        return reval

def main_menu():
    system(Data.clear)
    title = '''█▀█ █▀█   ▀█▀ █▀█ █▀█ █░░ █▀
▀▀█ █▀▄   ░█░ █▄█ █▄█ █▄▄ ▄█'''
    print(f"{Fore.LIGHTRED_EX}{title}\n\n{Fore.YELLOW}Version: {Fore.CYAN}{Data.version}\n{Fore.YELLOW}IP: {Fore.CYAN}{Data.user_ip}\n{Fore.YELLOW}Desktop Name: {Fore.CYAN}{Data.pc_username}"+Fore.RESET)

def main():
    try:
        print(f"\n{Fore.LIGHTGREEN_EX}[1] {Fore.CYAN}Create QR Code"+Fore.RESET)
        print(f"{Fore.LIGHTGREEN_EX}[2] {Fore.CYAN}Read QR Code"+Fore.RESET)
        print(f"{Fore.LIGHTGREEN_EX}[3] {Fore.CYAN}Change QR Code Color"+Fore.RESET)
        print(f"{Fore.LIGHTGREEN_EX}[4] {Fore.CYAN}Exit"+Fore.RESET)
        tool_option = input(f"\n{Fore.CYAN}Enter Tool Number: "+Fore.RESET)
        if tool_option == "1":
            main_menu()
            content = input(f"\n{Fore.CYAN}Enter Content to be Encoded: "+Fore.RESET)
            file_name = input(f"{Fore.CYAN}Enter File Name: "+Fore.RESET)
            content = content.replace("  ", "\n")
            if not "." in str(file_name):
                file_name += ".jpg"
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(str(content))
            qr.make(True)
            img = qr.make_image(fill_color=Data.fill_color, back_color=Data.bg_color)
            img.save(file_name)
            main_menu()
            main()

        elif tool_option == "2":
            main_menu()
            print(f"\n{Fore.LIGHTGREEN_EX}[1] {Fore.CYAN}View Value"+Fore.RESET)
            print(f"{Fore.LIGHTGREEN_EX}[2] {Fore.CYAN}View Points"+Fore.RESET)
            print(f"{Fore.LIGHTGREEN_EX}[3] {Fore.CYAN}View SQR"+Fore.RESET)
            qr_read_tool = input(f"\n{Fore.CYAN}Enter Read Value: "+Fore.RESET)
            file = input(f"{Fore.CYAN}Enter QR File Location: "+Fore.RESET)
            if not "." in file:
                file += ".jpg"

            main_menu()
            if qr_read_tool == "1":
                print(f"{Fore.LIGHTGREEN_EX}Content: {Fore.CYAN}{get_qr_data(file, 'value')}"+Fore.RESET)
                
            elif qr_read_tool == "2":
                print(f"{Fore.LIGHTGREEN_EX}Points: {Fore.CYAN}\n{get_qr_data(file, 'points')}"+Fore.RESET)

            elif qr_read_tool == "3":
                print(f"{Fore.LIGHTGREEN_EX}SQR: {Fore.CYAN}\n{get_qr_data(file, 's')}"+Fore.RESET)

            else:
                main_menu()
                print(f"\n{Fore.RED}Error: {Fore.CYAN}Invalid QR read tool option '{qr_read_tool}'"+Fore.RESET)
                main()
                return

            pause(1)
            main_menu()
            main()

        elif tool_option == "3":
            main_menu()
            print(f"\n{Fore.LIGHTGREEN_EX}[1] {Fore.CYAN}RGB Fill Color"+Fore.RESET)
            print(f"{Fore.LIGHTGREEN_EX}[2] {Fore.CYAN}RGB Background Color"+Fore.RESET)
            rgb_tool = input(f"\n{Fore.CYAN}Enter Tool Number: "+Fore.RESET)
            if rgb_tool == "1":
                main_menu()
                red = input(f"\n{Fore.CYAN}Enter Red(R) Value: "+Fore.RESET)
                green = input(f"{Fore.CYAN}Enter Green(G) Value: "+Fore.RESET)
                blue = input(f"{Fore.CYAN}Enter Blue(B) Value: "+Fore.RESET)
                Data.fill_color = (int(red), int(green), int(blue))
                main_menu()
                fill_color_string = []
                for item in Data.fill_color:
                    fill_color_string.append(str(item))
                print(f"\n{Fore.LIGHTRED_EX}Changed Fill Color: {Fore.CYAN}Fill color is now {', '.join(fill_color_string)}"+Fore.RESET)
                main()

            elif rgb_tool == "2":
                main_menu()
                red = input(f"\n{Fore.CYAN}Enter Red(R) Value: "+Fore.RESET)
                green = input(f"{Fore.CYAN}Enter Green(G) Value: "+Fore.RESET)
                blue = input(f"{Fore.CYAN}Enter Blue(B) Value: "+Fore.RESET)
                Data.bg_color = (int(red), int(green), int(blue))
                main_menu()
                bg_color_string = []
                for item in Data.bg_color:
                    bg_color_string.append(str(item))
                print(f"\n{Fore.LIGHTRED_EX}Changed Background Color: {Fore.CYAN}Background color is not {', '.join(bg_color_string)}"+Fore.RESET)
                main()

            else:
                main_menu()
                print(f"\n{Fore.RED}Error: {Fore.CYAN}Invalid RGB tool option '{rgb_tool}'"+Fore.RESET)
                main()

        elif tool_option == "4":
            system("exit")
            exit()

        else:
            main_menu()
            print(f"\n{Fore.RED}Error: {Fore.CYAN}Failed to find tool '{tool_option}'"+Fore.RESET)
            main()
    except KeyboardInterrupt:
        main_menu()
        print(f"\n{Fore.LIGHTGREEN_EX}Returned"+Fore.RESET)
        main()

main_menu()
main()