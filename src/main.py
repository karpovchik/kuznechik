import extra_funcs
import kuz

extra_funcs.modules.system("cls")

while (1):    
    res = ""
    plain_text = []
    hex_arr = []
    cypher_text = []

    print("="*152)
    print("\t\t\t\t\t\t\t\t<<< Laboratory work №4 >>>")
    print("="*152)

    print("\n<<< Exercise 1 >>>\nData encryption.\n")

    print("<<< Enter a number to choose a desirable action >>>\n")
    print("(1) - Open a file with a plain text to encrypt it;")
    print("(2) - Enter text by yourself;")
    print("(0) - Exit program;")
    entr = int(input("> "))

    if (entr == 0):
        extra_funcs.modules.system("cls")
        print("Bye, Bye!")
        break

    if (entr == 1):
        user_input = input("Enter the name of the file: ").strip()

        s = extra_funcs.open_file(user_input, entr)             # open text file
        entr = 0

    if (entr == 2):
        s = input("Enter your text: ")

    print("<<< Choose an action to load master key >>>\n")
    print("(1) - Enter key by yourself;")
    print("(2) - Open a file with a key from ГОСТ 34.12-2015;")
    entr = int(input("> "))

    if (entr == 1):
        key = input("Enter your key > ")
        key = [ "0x" + key[i : i + 2] for i in range(0, len(key), 2) ]

    if (entr == 2):
        user_input = input("Enter the name of the file with key: ").strip()
        key = extra_funcs.open_file(user_input, entr)
        key = bytes.fromhex(key.decode())
        key = [ f"0x{i:02x}" for i in key ]               # key in hex repr

    kuz.GF256_Generate_Table()                            # generate pow, log tables for multiplication
    RND_KEYS = kuz.K(key)                                 # form round keys

    for i in s:
        hex_arr.append('0x'+i.encode('cp1251').hex())

    text_len = len(hex_arr)
    hex_arr = extra_funcs.add_paddings(hex_arr)           # add paddings and convert to hexadecimal repr
    paddings = len(hex_arr) - text_len

    # select 16-byte blocks
    hex_arr = [ list(hex_arr[i : i + 16]) for i in range(0, len(hex_arr), 16)]
    print()
    print("="*190)
    print("\t\t\t\t\t\t\t\t\t<<< Plain text before encryption >>>")
    print("="*190)
    print(f"\n{s}\n")
    extra_funcs.display(hex_arr)
    print()

    print()
    print("="*190)
    print("\t\t\t\t\t\t\t\t\t<<< Cypher text in HEX representation >>>")
    print("="*190)
    print()
    for block in hex_arr:
        cypher_text.append(kuz.E(block, RND_KEYS))
    extra_funcs.display(cypher_text)
    print()
    
    print()
    print("="*190)
    print("\t\t\t\t\t\t\t\t\t<<< Initial plain text before encryption >>>")
    print("="*190)
    print()
    for block in cypher_text:
        plain_text.append(kuz.D(block, RND_KEYS))
    extra_funcs.display(plain_text)
    print()

    plain_text = extra_funcs.del_paddings(plain_text, paddings)                 # delete paddings

    for block in plain_text:
        for i in block:
            tmp = i[2:]
            if (len(tmp) == 1): tmp = "0" + tmp
            res += tmp

    print()
    print(bytearray.fromhex(res).decode('cp1251'))

    extra_funcs.modules.sleep(16)
    extra_funcs.modules.system("clear")

