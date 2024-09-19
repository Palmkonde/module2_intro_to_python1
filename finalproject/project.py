"""
password manager

criteria:
    function 5
    features 3
    pep8

features:
    view
    Add
    update
    delete

    encrypt
    decrypt
"""

# Import part
import os
import json
from pathlib import Path
import subprocess

# Constant variable
OPTION = ["V", "D", "A", "Q",
          "VIEW", "ADD", "DELETE", "QUIT"
          ]

# folder
CURRENT_DIR = Path(__file__).parent
FOLDER_NAME = ".vetit"
PATH_TO_STORE = Path(CURRENT_DIR / FOLDER_NAME)
USER_OS = None
DATA = {}

# bool state
is_folder_created = False
is_login = False

# Command
CLEAR_SCREEN = ""


def welcome() -> None:
    os.system(CLEAR_SCREEN)
    print(r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣾⣷⣾⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠁⠁⠈⠁⠀⠀⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢹⣿⣿⡆⠀⠈⠥⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢽⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⡌⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡆⠀⣿⣾⣶⣆⠀⠀⢨⡄⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⡈⠛⢿⣿⣿⡄⠀⢸⢊⣀⠈⣿⣿⣶⣶⣤⣄⣀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⠀⠉⠁⠀⠀⠄⠀⠀⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀
    ⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡄⠲⠤⢤⣤⡄⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
    ⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣉⣀⣐⠒⠒⠠⠰⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠤⠤⠉⣉⣉⢸⣓⡲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠒⠒⠒⠠⠤⢼⣭⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣉⣙⠛⠒⢸⠶⣦⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
    ⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠤⠬⢍⣉⣹⣛⣓⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡒⠲⠶⠶⡿⣽⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣍⣙⣛⣏⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏
    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠦⠤⣬⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀
    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣙⣟⣿⣷⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
    ⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠙⠃
    ⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀
    ⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
    ⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠁⡇⠟⢿⣿⣿⣿⣿⣿⣿⣿⣧⡀""")

    print(r""" _   _ _______     _______ ____     ____ _____     _______
| \ | | ____\ \   / / ____|  _ \   / ___|_ _\ \   / / ____|
|  \| |  _|  \ \ / /|  _| | |_) | | |  _ | | \ \ / /|  _|
| |\  | |___  \ V / | |___|  _ <  | |_| || |  \ V / | |___
|_| \_|_____|  \_/__|_____|_|_\_\_ \____|___|__\_/  |_____|___  ____  ____
\ \ / / _ \| | | |  _ \  |  _ \ / \  / ___/ ___\ \      / / _ \|  _ \|  _ \
 \ V / | | | | | | |_) | | |_) / _ \ \___ \___ \\ \ /\ / / | | | |_) | | | |
  | || |_| | |_| |  _ <  |  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| |
  |_| \___/ \___/|_| \_\ |_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/ """)


def quit() -> None:
    os.system(CLEAR_SCREEN)
    print(r"""
 _____ _   _    _    _   _ _  __ __   _____  _   _ _ _ _
|_   _| | | |  / \  | \ | | |/ / \ \ / / _ \| | | | | | |
  | | | |_| | / _ \ |  \| | ' /   \ V / | | | | | | | | |
  | | |  _  |/ ___ \| |\  | . \    | || |_| | |_| |_|_|_|
  |_| |_| |_/_/   \_\_| \_|_|\_\   |_| \___/ \___/(_|_|_)

 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
""")
    exit()


def add_password() -> None:
    os.system(CLEAR_SCREEN)

    website = input("Please enter name of website: ")
    username = input("Please enter username: ")
    password = input("Please enter password: ")

    # TODO: collect data in JSON Format!?


def delete_password() -> None:
    pass


def view_password() -> None:
    # if there are not .vetit folder
    if not any(PATH_TO_STORE.iterdir()):
        os.system(CLEAR_SCREEN)
        print("There is notthing to show!!")
        return

    # table that will show your password
    def create_ascii_table(headers, rows) -> None:
        colum_width = []
        for i, col in enumerate(zip(headers, *rows)):
            maximum_width = -1

            for number, row in enumerate(col, 1):
                tmp_num = ""
                if i == 0:  # if it's a first column
                    tmp_num = str(number) + "."
                maximum_width = max(
                    len(str(row)) + len(tmp_num), maximum_width)

            colum_width.append(maximum_width)

        # top
        hon_line = "+".join(("-" * (col_w + 2) for col_w in colum_width))
        hon_line = "+" + hon_line + "+"
        print(hon_line)

        # Colum name
        for head, col_w in zip(headers, colum_width):
            col_name = "| " + f"{head:^{col_w}} "
            print(col_name, end="")
        print("|")
        print(hon_line)

        # each row
        for number, row in enumerate(rows, 1):
            for i, (data, col_w) in enumerate(zip(row, colum_width)):
                # if it is first colum
                if i == 0:
                    row_data = "| " + f"{number} {data:<{col_w-1}}"
                else:
                    row_data = "| " + f"{data:<{col_w}} "
                print(row_data, end="")
            print("|")

        # bot
        print(hon_line)

    os.system(CLEAR_SCREEN)

    # name of each column
    headers = ["Website", "Username", "Password"]

    # should create tabel like this
    row = [
        ["somefile", "username", "Hide"]
    ]

    create_ascii_table(headers, row)

    print(f"\nWhich password do you want to show?")
    select = input("Enter password name or number: ")

    # TODO: to select name to show password


def initial_data() -> None:
    global is_folder_created
    global USER_OS
    global CLEAR_SCREEN
    global DATA

    # inital_OS
    if os.name == "nt":
        USER_OS = "WINDOW"

    elif os.name == "posix":
        USER_OS = "UNIX"

    # Check whether is there folader yet?
    if PATH_TO_STORE.exists() and PATH_TO_STORE.is_dir():
        is_folder_created = True
        # print("DEBUG: Folder exists")
    else:
        # print("DEBUG: Folder does not exist")
        pass

    # Load data
    if (PATH_TO_STORE / "userpassword.json"):
        with open("userpassword.json", "r") as file:
            DATA = json.load(file)

    # initail command base on USER_OS
    if USER_OS == "WINDOW":
        CLEAR_SCREEN = "cls"

    if USER_OS == "UNIX":
        CLEAR_SCREEN = "clear"


def option() -> None:
    global is_folder_created
    global is_login

    # Create folder if user used for first time
    if not is_folder_created:
        print("It looks like your first time")
        print("Do you want to create Folder (y)es/(n)o")

        user_option = input().upper()

        if user_option == "Y" or user_option == "YES":
            user_password = input("Please create new password: ")
            again_password = input("Again please: ")

            if user_password != again_password:
                input("Wrong! Please try again")
                quit()
                return

            # user already signin, next step is create folder
            os.system("mkdir .vetit")

            # TODO:generate_key for decryption

            # for Window make folder hidden
            if USER_OS == "WINDOW":
                subprocess.run(["attrib", "+h", PATH_TO_STORE])

            # change state to true
            if PATH_TO_STORE.exists() and PATH_TO_STORE.is_dir():
                # print("DEBUG: Folder exists")
                is_folder_created = True

            # save user password
            user_newfile = PATH_TO_STORE / "userpassword.json"
            json_format = {
                "userpassword": user_password
            }
            with open(user_newfile, "w") as file:
                json.dump(json_format, file)

        else:
            user_option = input(
                "Sorry, We CANNOT start without initail folder")
            quit()

    if not is_login:
        user_password = input("Please login: ")
        login(user_password)
        is_login = True

    # Already have folder and already login
    while is_folder_created and is_login:

        print("\nWhat do you want to do?")
        print("""
                (V)iew passwords
                (A)dd new password
                (D)elete password
                (Q)uit""")

        user_option = input().upper()
        if not (user_option in OPTION):
            print("It is NOT in choices!!!")
            input("PLEASE TYPE ANYTHING TO CONTINUE")
            os.system(CLEAR_SCREEN)

        if (user_option == "V") or (user_option == "VIEW"):
            view_password()

        if (user_option == "A") or (user_option == "ADD"):
            add_password()

        if (user_option == "D") or (user_option == "DELETE"):
            delete_password()

        if (user_option == "Q") or (user_option == "QUIT"):
            quit()
            return


# TODO: Test encrypt and decrypt
def encrypt(plain) -> str:
    pass
    # TODO: implement this one
    # XOR first
    # ge it to realbase64
    # using กขคงจ


def decrypt(cipher) -> str:
    pass
    # TODO: implement this one


def login(password) -> None:
    # login second time check whether password is as same as before
    user_p = DATA["userpassword"]

    if password != user_p:
        os.system(CLEAR_SCREEN)
        print(r"""__        ______   ___  _   _  ____                
\ \      / /  _ \ / _ \| \ | |/ ___|               
 \ \ /\ / /| |_) | | | |  \| | |  _                
  \ V  V / |  _ <| |_| | |\  | |_| |               
 __\_/\_/__|_| \_\\___/|_| \_|\____|_   __ _   _ 
|_   _|  _ \ \ / /    / \  / ___|  / \  |_ _| \ | |
  | | | |_) \ V /    / _ \| |  _  / _ \  | ||  \| |
  | | |  _ < | |    / ___ \ |_| |/ ___ \ | || |\  |
  |_| |_| \_\|_|   /_/   \_\____/_/   \_\___|_| \_|""")

        input("Type any key to continue")
        exit()


if __name__ == "__main__":
    initial_data()
    welcome()
    option()
