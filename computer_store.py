import os

def get_init_state():
    return {
        "mouse": 20,
        "keyboard": 15,
        "laptop": 3,
        "gpu": 10
    }

def clear_consol():
    os.system("cls || clear")

def print_state(state, keys_in_order=[], end="===============", header="Current state: \n===============", should_clear_consol=False):
    if should_clear_consol:
        clear_consol()
    
    print(header)
    if len(keys_in_order) == 0:
        for key, value in state.items():
            print(f"{key}: {value}")
    else:
        for key in keys_in_order:
            print(f"{key}: {state[key]}")
        
    print(end)


def add_new_items_to_state(state, items_to_add, print_on=False):
    if print_on:
        print("Dodawanie itemów do stanu: " + str(items_to_add))
    if items_to_add[0] in state:
        state[items_to_add[0]] += 1
    else:
         state[items_to_add[0]] = 1
    
    if len(items_to_add) > 1:
        items_to_add.remove(items_to_add[0])
        add_new_items_to_state(state, items_to_add)
    
def export_to_file(state, filename="state.txt", header="PC STORE STATE:"):
    with open(filename, "w") as file_handle:
        file_handle.write(f"{header}\n")
        for key, value in state.items():
             file_handle.write(f"{key}: {value}\n")


def main():
    current_state = get_init_state()
    add_new_items_to_state(current_state, ["gpu", "cpu", "camera", "gpu"])
    print_state(current_state)

    key_order = sorted(current_state)
    print_state(current_state, keys_in_order=key_order)


    # item[0] - sortowanie po kluczu, item[1] - sortowanie po wartosc
    key_order_tuples = sorted(current_state.items(), key=lambda item: item[1], reverse=True)
    print(key_order_tuples)
    key_order = []
    for element in key_order_tuples:
        key_order.append(element[0])

    print(key_order)

    print_state(current_state, keys_in_order=key_order)
    export_to_file(current_state)

if __name__ == "__main__":
    main()