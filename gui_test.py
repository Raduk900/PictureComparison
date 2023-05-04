import tkinter as tk
import server.client as client
import picture_wia_laptop_camera

client.open_socket()

window = tk.Tk()

window.geometry("400x300")
window.title("Item Manager")

window.config(bg="#f0f0f0")

def add_item_click():
    label.config(text="Enter Product ID")

    # hide the add_item_button and take_item_button
    add_item_button.pack_forget()
    take_item_button.pack_forget()

    # create a frame to hold the widgets
    frame = tk.Frame(window, bg="#f0f0f0")
    frame.pack(fill="both", expand=True)

    def go_back():
        # show the add_item_button and take_item_button again
        add_item_button.pack(pady=10)
        take_item_button.pack(pady=10)
        label.config(text="Choose an action")
        frame.destroy()

    # validate input to allow only digits
    def validate_id(input):
        if input.isdigit():
            return True
        else:
            return False

    id_field = tk.Entry(frame, width=30, font=("Arial", 14), bg="lightgray", borderwidth=2, relief="solid", validate="key")
    id_field.config(validatecommand=(frame.register(validate_id), '%S'))
    id_field.pack(pady=10)

    submit_button = tk.Button(frame, text="Submit", command=lambda: submit_id(window, id_field), bg="lightgray", fg="black", font=("Arial", 14), borderwidth=2, relief="solid")
    submit_button.pack(pady=10)

    back_button = tk.Button(frame, text="Back", command=go_back, bg="lightgray", fg="black", font=("Arial", 14), borderwidth=2, relief="solid")
    back_button.pack(pady=10)

    # set focus to the id_field
    id_field.focus()


def submit_id(id_window, id_field):
    item_id = id_field.get()

    id_window.destroy()

    if item_id:
        picture_wia_laptop_camera.capture_with_screenshot()
        client.sending_data(item_id)
    else:
        print("ID cannot be empty.")

def take_item_click():
    label.config(text="Enter your code")

    add_item_button.pack_forget()
    take_item_button.pack_forget()

    # create a function to go back to the main menu
    def go_back():
        add_item_button.pack(pady=10)
        take_item_button.pack(pady=10)
        back_button.pack_forget()
        input_field.pack_forget()
        submit_button.pack_forget()
        label.config(text="Choose an action")

    # validate the input to allow only 6 digits
    validate_cmd = window.register(validate_input)
    input_field.config(validate="key", validatecommand=(validate_cmd, '%P'))

    input_field.pack(pady=(0,10))

    submit_button = tk.Button(window, text="Submit", command=lambda: submit_click(input_field, submit_button), bg="lightgray", fg="black", font=("Arial", 14), borderwidth=2, relief="solid", state="disabled")
    submit_button.pack(pady=(10,30))

    back_button = tk.Button(window, text="Back", command=go_back, bg="lightgray", fg="black", font=("Arial", 14), borderwidth=2, relief="solid")
    back_button.pack(pady=(10,30))

    input_field.focus()

    def check_input_length(*args):
        if len(input_field.get()) == 3:
            submit_button.config(state="normal")
        else:
            submit_button.config(state="disabled")

    input_field.bind('<KeyRelease>', check_input_length)

def validate_input(input_str):
    if input_str.isdigit() and len(input_str) <= 6:
        return True
    else:
        return False


def submit_click(input_field, submit_button):
    input_text = input_field.get()
    print("Input text:", input_text)
    client.sending_data(input_text)
    input_field.delete(0, tk.END)
    submit_button.config(state="disabled")


label = tk.Label(window, text="Choose an action", font=("Arial", 14), bg="#f0f0f0")
label.pack(pady=(50,10))

add_item_button = tk.Button(window, text="Add Item", command=add_item_click, bg="lightgray", fg="black", font=("Arial", 14), borderwidth=2, relief="solid")
add_item_button.pack(pady=10)

take_item_button = tk.Button(window, text="Take Item", command=take_item_click, bg="lightgray", fg="black", font=("Arial", 14), borderwidth=2, relief="solid")
take_item_button.pack(pady=10)

input_field = tk.Entry(window, width=30, font=("Arial", 14), bg="lightgray", borderwidth=2, relief="solid")
input_field.pack_forget()

window.mainloop()

client.close_socket()
