import pyperclip
import tkinter as tk


# Define a function to modify the badges
def modify_badges():
    # Get the repository name and file name from the input fields
    repo_name = repo_name_field.get()
    file_name = file_name_field.get()

    # Modify the badges in the input field
    input_text = input_field.get("1.0", tk.END)
    modified_text = input_text.replace("Swing_prediction.lua", repo_name).replace(".lua", f"/blob/main/{file_name}").replace("Swing_prediction", repo_name)

    # Copy the modified badges to the clipboard and display them in the output field
    pyperclip.copy(modified_text)
    output_field.delete("1.0", tk.END)
    output_field.insert("1.0", modified_text)

# Create a Tkinter window with input and output fields
root = tk.Tk()
root.title("Badge Modifier")
root.configure(bg="#24292e")

# Create input fields for the repository name, file name, and badge URLs
repo_name_label = tk.Label(root, text="Repository Name:", fg="white", bg="#24292e")
repo_name_field = tk.Entry(root)
file_name_label = tk.Label(root, text="File Name:", fg="white", bg="#24292e")
file_name_field = tk.Entry(root)
input_label = tk.Label(root, text="Input Badges:", fg="white", bg="#24292e")
input_field = tk.Text(root, height=10, width=50, bg="#2c333a")
output_label = tk.Label(root, text="Modified Badges:", fg="white", bg="#24292e")
output_field = tk.Text(root, height=10, width=50, bg="#2c333a")

# Create a button to modify the badges
modify_button = tk.Button(root, text="Modify Badges", command=modify_badges, bg="#2ea44f", fg="white")

# Add the input and output fields and the button to the window
repo_name_label.pack()
repo_name_field.pack()
file_name_label.pack()
file_name_field.pack()
input_label.pack()
input_field.pack()
modify_button.pack()
output_label.pack()
output_field.pack()

# Start the Tkinter main loop
root.mainloop()
