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

def print_state(state, end="===============", header="Current state: \n===============", should_clear_consol=False):
    if should_clear_consol:
        clear_consol()
    
    print(header)
    for key, value in state.items():
        print(f"{key}: {value}")
    print(end)


def add_new_items_to_state(state, items_to_add):
    print("Dodawanie itemów do stanu: " + str(items_to_add))
    if items_to_add[0] in state:
        state[items_to_add[0]] += 1
    else:
         state[items_to_add[0]] = 1
    
    if len(items_to_add) > 1:
        items_to_add.remove(items_to_add[0])
        add_new_items_to_state(state, items_to_add)
    
def export_to_file(state, filename="state.txt"):
    with open(filename, "w") as file_handle:
        for key, value in state.items():
             file_handle.write(f"{key}: {value}\n")


def main():
    current_state = get_init_state()
    print_state(current_state)
    print_state(current_state, should_clear_consol=True)
    add_new_items_to_state(current_state, ["gpu", "cpu", "camera", "gpu"])
    print_state(current_state)
    export_to_file(current_state)

if __name__ == "__main__":
    main()