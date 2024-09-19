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
import sys

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
IS_LOGIN = False
IS_FOLDER_CREATED = False

# Command
CLEAR_SCREEN = ""


def welcome():
    """ NEVERGONNAGIVEU UP NEVERGONNALET U DOWN"""
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


def quit_the_program():
    """ THANK YOU """
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
    sys.exit()


def add_password():
    """ ADD username and password """

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


def delete_password():
    """Delete from database """


def view_password():
    """create an table to show you all password"""

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

    print("\nWhich password do you want to show?")
    select = input("Enter password name or number: ")

    # TODO: to select name to show password


def initial_data():
    """ function intialize data before run everythingelse """

    # inital_OS
    if os.name == "nt":
        user_os = "WINDOW"

    elif os.name == "posix":
        user_os = "UNIX"

    # Load data
    data, key = None, None
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r", encoding="utf-8") as file:
            key = file.read()

    # initail command base on user_os
    if user_os == "WINDOW":
        clear_screeen = "cls"

    if user_os == "UNIX":
        clear_screeen = "clear"

    return [user_os, clear_screeen, data, key]


def option():
    """ main function to select action to do """

    # Already have folder and already login
    while IS_FOLDER_CREATED and IS_LOGIN:

        print("\nWhat do you want to do?")
        print("""
                (V)iew passwords
                (A)dd new password
                (D)elete password
                (Q)uit""")

        user_option = input().upper()
        if not user_option in OPTION:
            print("It is NOT in choices!!!")
            input("PLEASE TYPE ANYTHING TO CONTINUE")
            os.system(CLEAR_SCREEN)

        if user_option in ("V", "VEIW"):
            view_password()

        if user_option in ("A", "ADD"):
            add_password()

        if user_option in ("D", "DELETE"):
            delete_password()

        if user_option in ("Q", "QUIT"):
            update_json()
            quit_the_program()


def first_time():
    """
        When user use this program first time
        we need to collect password for this program and create Key, folder, etc.
    """

    is_folder_created = False
    # Check whether is there folader yet?
    if os.path.exists(PATH_TO_STORE) and os.path.isdir(PATH_TO_STORE):
        is_folder_created = True
        # print("DEBUG: Folder exists")

    # Create folder if user used for first time
    if not is_folder_created:
        print("It looks like your first time")
        print("Do you want to create Folder (y)es/(n)o")

        user_option = input().upper()
        if user_option in ("Y", "YES"):

            # user already signin, next step is create folder
            os.system("mkdir .vetit")

            # generate_key for decryption
            key = "vetuay" * 1000
            with open(KEY_FILE, "w", encoding="utf-8") as file:
                file.write(key)

            # for Window make folder hidden
            if USER_OS == "WINDOW":
                os.system(f"attrib +h {PATH_TO_STORE}")

            # change state to true
            if os.path.exists(PATH_TO_STORE) and os.path.isdir(PATH_TO_STORE):
                # print("DEBUG: Folder exists")
                is_folder_created = True

        else:
            user_option = input(
                "Sorry, We CANNOT start without initail folder")
            quit_the_program()

    return is_folder_created


def encrypt(plain):
    """ SECRET """
    cipher = ""
    alphabet = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ"

    for i, character in enumerate(plain):
        cipher += chr(ord(character) ^ ord(KEY[i]))

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


def decrypt(cipher):
    """ SECRET """
    plain = ""
    alphabet = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ"
    alphabet_l = len(alphabet)
    cipher = cipher[::-1]
    cipher = cipher[2:]

    tmp = 0
    for i, character in enumerate(cipher):
        tmp += (alphabet_l ** i) * alphabet.index(character)
    tmp = hex(tmp)[2:]

    fake_plain = ""
    for i in range(0, len(tmp), 2):
        fake_plain += chr(int(tmp[0 + i:2 + i], 16))

    for i, character in enumerate(fake_plain):
        plain += chr(ord(character) ^ ord(KEY[i]))

    return plain


def login():
    """ login second time check whether password is as same as before """

    # user first time
    if not (os.path.exists(PASSWORD_FILE) or os.path.isfile(PASSWORD_FILE)):
        user_password = input("Please create new password: ")
        again_password = input("Confirm again: ")

        if user_password != again_password:
            input("Wrong! Please try again")
            quit_the_program()

        # save user password
        user_newfile = PASSWORD_FILE
        json_format = {
            "userpassword": encrypt(user_password)
        }
        with open(user_newfile, "w", encoding="utf-8") as file:
            json.dump(json_format, file, indent=4, ensure_ascii=False)

        return True

    user_password = input("Please login: ")
    password = decrypt(DATA["userpassword"])

    if password != user_password:
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
        sys.exit()

    return True


def update_json():
    """ update file password before end program """

    if USER_OS == "WINDOW":
        os.system(f"attrib -h {PASSWORD_FILE}")

    with open(PASSWORD_FILE, "w", encoding="utf-8") as file:
        json.dump(DATA, file, indent=4, ensure_ascii=False)

    if USER_OS == "WINDOW":
        os.system(f"attrib +h {PASSWORD_FILE}")


if __name__ == "__main__":
    welcome()
    IS_FOLDER_CREATED = first_time()
    USER_OS, CLEAR_SCREEN, DATA, KEY = initial_data()
    IS_LOGIN = login()
    option()
