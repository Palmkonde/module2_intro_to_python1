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
OPTION = ("V", "D", "A", "Q",
          "VIEW", "ADD", "DELETE", "QUIT"
          )

# folder
CURRENT_DIR = os.getcwd()
FOLDER_NAME = ".vetit"
PATH_TO_STORE = os.path.join(CURRENT_DIR, FOLDER_NAME)
PASSWORD_FILE = "/".join([PATH_TO_STORE, ".userpassword.json"])
KEY_FILE = "/".join([PATH_TO_STORE, ".secret_key.key"])

# OS
USER_OS = None

# DATA
DATA = {}

# bool state
IS_LOGIN = False
IS_FOLDER_CREATED = False

# Command
CLEAR_SCREEN = ""


def dance_welcome() -> None:
    """ 
    Show NEVERGONNAGIVEU UP NEVERGONNALET U DOWN Boys 
    Let him welcome you

    Args: 
        None
    Returns: 
        None
    """
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


def quit_the_program() -> None:
    """ 
    THANK YOU and quit the program 

    Args: 
        None
    Returns: 
        None
    """
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


def is_valid(text: str) -> bool:
    """ 
    to validate input 

    Args: 
        text (str): 
            input to check than contain space or not

    Returns:
        is_valid (bool): 
            True means valid False means invalid
    """

    if len(text) == 0:
        return False

    if " " in text:
        return False

    return True


def add_password() -> None:
    """ 
    ADD username and password to database

    Args: 
        None

    Returns: 
        None
    """

    os.system(CLEAR_SCREEN)

    website = input("Please enter name of website: ").lower().strip()
    username = input("Please enter username: ").strip()
    password = input("Please enter password: ").strip()

    if not (is_valid(website) or is_valid(username) or is_valid(password)):
        print("There are some invalid password")
        return

    data_injson = {
        website: {
            "username": username,
            "password": encrypt(password)
        },
    }
    DATA.update(data_injson)


def create_ascii_table(headers: list[str], rows: list[list[str]]) -> None:
    """ 
    table that will show your password 
    Args:
        headers (list[str]):  
            column name
        rows (list[list[str]]): 
            each row of Data

    Returns: 
        None
    """

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
            # if it is first column
            if i == 0:
                row_data = "| " + f"{number} {data:<{col_w-1}}"
            else:
                row_data = "| " + f"{data:<{col_w}} "
            print(row_data, end="")
        print("|")

    # bot
    print(hon_line)


def delete_password() -> None:
    """
    Delete from database 

    Args: 
        None

    Return: 
        None
    """
    os.system(CLEAR_SCREEN)

    if len(DATA) == 1:
        print("There is nothing to delete!!!")
        return

    # name of each column
    headers = ["Website", "Username", "Password"]

    # should create tabel like this
    row = []
    passwords = []
    for website, data in DATA.items():
        if website == "userpassword":
            continue

        username = data["username"]
        passwords.append(data["password"])
        row.append([website, username, "Hide"])

    create_ascii_table(headers, row)

    # user_input which password that use want to delete
    print("Which password do you want to delete?")
    select = input("Please enter website name or number: ").lower().strip()

    if not is_valid(select):
        print("There are some invalid try again")
        return

    deleted = ""

    # select is a number
    if select.isdigit() and (1 <= int(select) <= len(row)):
        select = int(select) - 1
        deleted = row[select][0]
        DATA.pop(row[select][0])

    elif select in DATA:
        deleted = select
        DATA.pop(select)
    else:
        print("Not in choice! Try again")
        return

    os.system(CLEAR_SCREEN)
    print(f"{deleted}'s password deleted")


def view_password() -> None:
    """
    create an table to show you all password

    Args: 
        None

    Returns: 
        None
    """
    os.system(CLEAR_SCREEN)

    # for now DATA contains only password that use for login
    if (not DATA) or len(DATA) == 1:
        print("There is nothing to show!!!")
        return

    # name of each column
    headers = ["Website", "Username", "Password"]

    # should create tabel like this
    row = []
    passwords = []
    for website, data in DATA.items():
        if website == "userpassword":
            continue

        username = data["username"]
        passwords.append(data["password"])
        row.append([website, username, "Hide"])

    create_ascii_table(headers, row)

    print("\nWhich password do you want to show?")
    select = input("Enter website name or number: ").lower().strip()

    if select.isdigit() and (1 <= int(select) <= len(row)):
        select = int(select) - 1
        row[select][2] = decrypt(passwords[select])

    elif select in DATA:
        for i, name in enumerate(row):
            if select == name[0]:
                name[2] = decrypt(passwords[i])

    else:
        print("Not in choice! Try again")
        return

    os.system(CLEAR_SCREEN)
    create_ascii_table(headers, row)


def load_initial_data() -> list[str, str, dict]:
    """ 
    function intialize data before run anything 

    Args: 
        None

    Returns:
        list: a list that contains these elements:
            user_os (str):
                specify user_os whether they use UNIX or WINDOW
            clear_screen (str):
                select between "cls" and "clear" by their OS
            data (dict):
                Load Data from JSON file
    """

    # inital_OS
    user_os = ""
    if os.name == "nt":
        user_os = "WINDOW"

    elif os.name == "posix":
        user_os = "UNIX"

    # Load data
    data = None
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

    # initail command base on user_os
    clear_screeen = ""
    if user_os == "WINDOW":
        clear_screeen = "cls"

    elif user_os == "UNIX":
        clear_screeen = "clear"

    return [user_os, clear_screeen, data]


def select_option() -> None:
    """ 
    main function to select action to do 

    Args: 
        None

    Return: 
        None
    """

    os.system(CLEAR_SCREEN)

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
            input("PLEASE ENTER TO CONTINUE")
            os.system(CLEAR_SCREEN)

        if user_option in ("V", "VIEW"):
            view_password()

        elif user_option in ("A", "ADD"):
            add_password()

        elif user_option in ("D", "DELETE"):
            delete_password()

        elif user_option in ("Q", "QUIT"):
            update_json()
            quit_the_program()


def run_first_time() -> bool:
    """
    When user use this program first time
    we need to collect password for this program and create Key, folder, etc

    Args: 
        None

    Returns:
        is_folder_created (bool):
            have folder .vetit or not
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


def encrypt(plain: str) -> str:
    """ 
    function to encryption password

    principle
    1. change each character to int according to ascii
        ex. if input "A", character is 65
    2. use XOR with key
    3. then convert it to hex number
        ex. plain = "ABC", we got [37, 27, 37]
    4. concate it and convert to base 10
        ex. [37, 27, 37] -> 372737 -> 3614519
    5. then change it into base44 and respresent in index of Thai alphabet
    6. reverse and put "==" for fun!!!

    Args:
        plain (str):
            Text that you want to encrypt

    Returns:
        result (str): 
            Encrypted Text
    """

    with open(KEY_FILE, "r", encoding="utf-8") as file:
        key = file.readline()

    cipher = []
    alphabet = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ"

    for i, character in enumerate(plain):
        cipher += chr(ord(character) ^ ord(key[i]))

    cipher = "".join([hex(ord(i))[2:].zfill(2) for i in cipher])
    cipher = int(cipher, 16)

    result = ""
    alphabet_l = len(alphabet)
    while cipher != 0:
        result += alphabet[cipher % alphabet_l]
        cipher //= alphabet_l
    result = result[::-1]
    result += "=="

    return result


def decrypt(cipher: str) -> str:
    """ 
    function to decrypt password 

    principle
    1. reverse and delete "=="
    2. change it into base 10
    3. change it into hex 
        (some bug appear when 0 is first of the base 10 value)
    4. seperate to each of hex value 
    5. XOR with key and the convert to character

    Args:
        cipher (str):
            Encrypted_text
    Returns:
        plain (str):
            plain_text

    """

    with open(KEY_FILE, "r", encoding="utf-8") as file:
        key = file.readline()

    plain = ""
    alphabet = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ"
    alphabet_l = len(alphabet)
    cipher = cipher[::-1]
    cipher = cipher[2:]

    tmp = 0
    for i, character in enumerate(cipher):
        tmp += (alphabet_l ** i) * alphabet.index(character)
    tmp = hex(tmp)[2:]

    if len(tmp) % 2 != 0:
        tmp = "0" + tmp

    fake_plain = []
    for i in range(0, len(tmp), 2):
        fake_plain.append(int(tmp[i:i + 2], 16))

    for i, character in enumerate(fake_plain):
        plain += chr(character ^ ord(key[i]))

    return plain


def login() -> list[bool, str | None]:
    """ 
    login second time check whether password is as same as before 
    Args: 
        None

    Returns:
        list: that contains these elements:
            is_login (bool): 
                check that user logged in
            user_password (str | None):  
                user_password might be None unless it user first time

    """
    user_password = None
    is_login = False

    # user first time
    if not (os.path.exists(PASSWORD_FILE) or os.path.isfile(PASSWORD_FILE)):

        while not user_password:
            user_password = input("Please create new password: ").strip()

            if not user_password:
                input("Password Can't be empty!!! ENTER to try again")
                user_password = ""
                os.system(CLEAR_SCREEN)

            elif not is_valid(user_password):
                input("Password can't contains space!!! ENTER to try again")
                user_password = ""
                os.system(CLEAR_SCREEN)

        is_login = True
        return [is_login, user_password]

    # login
    user_password = input("Please login with your password: ")
    stored_password = decrypt(DATA["userpassword"])  # bug bounty

    if stored_password != user_password:
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

        input("Please ENTER to continue")
        sys.exit()

    is_login = True
    return [is_login, user_password]


def update_json() -> None:
    """ 
    update file password before end program 

    Args: 
        None

    Returns: 
        None
    """

    if USER_OS == "WINDOW":
        os.system(f"attrib -h {PASSWORD_FILE}")

    with open(PASSWORD_FILE, "w", encoding="utf-8") as file:
        json.dump(DATA, file, indent=4, ensure_ascii=False)

    if USER_OS == "WINDOW":
        os.system(f"attrib +h {PASSWORD_FILE}")


if __name__ == "__main__":
    dance_welcome()
    IS_FOLDER_CREATED = run_first_time()
    USER_OS, CLEAR_SCREEN, DATA = load_initial_data()
    IS_LOGIN, initial_password = login()

    # mean it's user first time
    if initial_password:
        DATA = {
            "userpassword": encrypt(initial_password)
        }
    select_option()
