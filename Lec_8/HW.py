from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data!\n")


def add_new_contact():
    global last_id
    array = ['surname', 'name', 'patronymic', 'phone number']
    answers = []
    for i in array:
        answers.append(data_collection(i))

    if not contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("The entry has been successfully added to the phone book!\n")
    else:
        print("The data already exists!")

def search():
    id = contact(0, input("Enter the search data: "))
    if id:
        print(*id, sep="\n")
    else:
        print("The data is not correct!")

def contact(id, data):
    if id:
        candidates = [i for i in all_data if id in i.split()[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates

def data_collection(num):
    answer = input(f"Enter a {num}: ")
    while True:
        if num in "surname name patronymic":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Use only use only the letters"
                       f" of the alphabet, the length"
                       f" of the number is 11 digits\n"
                       f"Enter a {num}: ")
    return answer

def del_contact():
    
    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Enter the record id: ")

    if contact(del_record, ""):
        all_data = [k for k in all_data if k.split()[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Record deleted!\n")
    else:
        print("The data is not correct!")

def change_contact(data_tuple):
    
    global all_data
    symbol = "\n"

    id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v.split()[0] == id:
            v = v.split()
            v[int(num_data)] = data
            if contact(0, " ".join(v[1:])):
                print("The data already exists!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Record changed!\n")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                del_contact()
            case "6":
                exp_imp_menu()
            case "7":
                play = False
            case _:
                print("Try again!\n")

def edit_menu():
    add_dict = {"1": "surname", "2": "name", "3": "patronymic", "4": "phone number"}

    show_all()
    id = input("Enter the record id: ")

    if contact(id, ""):
        while True:
            print("\nChanging:")
            change = input("1. surname\n"
                           "2. name\n"
                           "3. patronymic\n"
                           "4. phone number\n"
                           "5. exit\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("The data is not recognized, repeat the input.")
    else:
        print("The data is not correct!")


def exp_bd(name):
    symbol = "\n"

    change_name = f"{name}.txt" 
    if not path.exists(change_name):
        with open(change_name, "w", encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')


def ipm_bd(name):
    global file_base
    if path.exists(name):
        file_base = name
        read_records()


def exp_imp_menu():
    while True:
        print("\nExp/Imp menu:")
        move = input("1. Import\n"
                     "2. Export\n"
                     "3. exit\n")

        match move:
            case "1":
                ipm_bd(input("Enter the name of the file: "))
            case "2":
                exp_bd(input("Enter the name of the file: "))
            case "3":
                return 0
            case _:
                print("The data is not recognized, repeat the input.")


main_menu()