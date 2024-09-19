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

# Constant variable
OPTION = ["V", "D", "A", "Q",
          "VIEW", "ADD", "DELETE", "QUIT"
          ]

# folder
CURRENT_DIR = os.getcwd()
FOLDER_NAME = ".vetit"
PATH_TO_STORE = CURRENT_DIR + "/" + FOLDER_NAME
PASSWORD_FILE = PATH_TO_STORE + "/.userpassword.json"
KEY_FILE = PATH_TO_STORE + "/.secret_key.key"

# OS
USER_OS = None

# DATA
DATA = {}
KEY = ""

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
    global DATA

    os.system(CLEAR_SCREEN)

    website = input("Please enter name of website: ").lower()
    username = input("Please enter username: ")
    password = input("Please enter password: ")

    data_injson = {
        website: {
            "username": username,
            "password": encrypt(password)
        },
    }
    DATA.update(data_injson)

    # TODO: in one website can contains many username and password


def delete_password() -> None:
    pass


def view_password() -> None:
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

    # TODO: show pass word and username from JSON files
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
    global KEY

    # inital_OS
    if os.name == "nt":
        USER_OS = "WINDOW"

    elif os.name == "posix":
        USER_OS = "UNIX"

    # Load data
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r", encoding="utf-8") as file:
            DATA = json.load(file)

    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as file:
            KEY = file.read()

    # initail command base on USER_OS
    if USER_OS == "WINDOW":
        CLEAR_SCREEN = "cls"

    if USER_OS == "UNIX":
        CLEAR_SCREEN = "clear"


def option() -> None:
    global is_login
    global is_folder_created

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
            update_json()
            quit()
            return


def first_time() -> None:
    global is_folder_created
    global is_login
    global DATA
    global KEY

    # Check whether is there folader yet?
    if os.path.exists(PATH_TO_STORE) and os.path.isdir(PATH_TO_STORE):
        is_folder_created = True
        # print("DEBUG: Folder exists")
    else:
        # print("DEBUG: Folder does not exist")
        pass

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

            # generate_key for decryption
            KEY = "vetuay" * 1000
            with open(KEY_FILE, "w") as file:
                file.write(KEY)

            # for Window make folder hidden
            if USER_OS == "WINDOW":
                os.system(f"attrib +h {PATH_TO_STORE}")

            # change state to true
            if os.path.exists(PATH_TO_STORE) and os.path.isdir(PATH_TO_STORE):
                # print("DEBUG: Folder exists")
                is_folder_created = True

            # save user password
            user_newfile = PASSWORD_FILE
            json_format = {
                "userpassword": encrypt(user_password)
            }
            with open(user_newfile, "w", encoding="utf-8") as file:
                json.dump(json_format, file, ensure_ascii=False)

        else:
            user_option = input(
                "Sorry, We CANNOT start without initail folder")
            quit()


# TODO: Test encrypt and decrypt
def encrypt(plain):
    global KEY
    # TODO: implement this one
    # secret !!!
    cipher = ""
    alphabet = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ"

    for i in range(len(plain)):
        cipher += chr(ord(plain[i]) ^ ord(KEY[i]))

    cipher = "".join([str(hex(ord(i))[2:]) for i in cipher])
    cipher = int(cipher, 16)

    result = ""
    alphabet_l = len(alphabet)
    while cipher != 0:
        result += alphabet[cipher % alphabet_l]
        cipher //= alphabet_l
    result = result[::-1]
    result += "=="

    return result


def decrypt(cipher) -> str:
    global KEY
    # TODO: implement this one
    plain = ""
    alphabet = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ"
    alphabet_l = len(alphabet)
    cipher = cipher[::-1]
    cipher = cipher[2:]

    tmp = 0
    for i in range(len(cipher)):
        tmp += (alphabet_l ** i) * alphabet.index(cipher[i])
    tmp = hex(tmp)[2:]

    fake_plain = ""
    for i in range(0, len(tmp), 2):
        fake_plain += chr(int(tmp[0 + i:2 + i], 16))

    for i in range(len(fake_plain)):
        plain += chr(ord(fake_plain[i]) ^ ord(KEY[i]))

    return plain


def login(password) -> None:
    # login second time check whether password is as same as before
    user_p = decrypt(DATA["userpassword"])

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


def update_json():
    with open(PASSWORD_FILE, "w", encoding="utf-8") as file:
        json.dump(DATA, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    welcome()
    first_time()
    initial_data()
    option()
