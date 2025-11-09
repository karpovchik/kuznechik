import modules

def open_file(user_input : str, e_ : int) -> str:
    base_dir = modules.path.abspath("../files")         # define base dir

    file_path = modules.path.join(base_dir, user_input) # concatanate base dir with user input

    # check new path in base_dir
    if not modules.path.commonpath([base_dir, modules.path.abspath(file_path)]) == base_dir:
        print("Error: Invalid file path!")
    else:
        try:
            if e_ == 1:
                with open(file_path, 'rt', encoding='cp1251') as file:
                    content = file.read()
                return content
            elif e_ == 2:
                with open(file_path, 'rb') as file:
                    content = file.read()
                return content
            else:
                print("Error: Invalid mode!")
        except FileNotFoundError:
            print("Error: File not found!")
        except Exception:
            print("Error: Could not read file!")


def add_paddings(arr : list) -> list:
    res = arr
    L = len(arr) % 16

    if (L != 0):
        padd_len = 16 - L
    else:
        padd_len = 16
 
    for i in range(padd_len):
        res.append(hex(padd_len))       # add paddings

    return res

def del_paddings(arr : list, padd_len : int) -> list:
    if (padd_len == 16): arr.pop()
    else:
        for i in range(padd_len):
            arr[-1].pop()

    return arr
