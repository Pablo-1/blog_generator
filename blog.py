import tkinter as tk

root = tk.Tk()

root.geometry("600x400")
root.title("Blogpost generator GUI")

label = tk.Label(root, text="Generate a blogpost", font=('Arial', 20))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, font=('Arial', 15), height=2)
textbox.pack(padx=40)


gen_button = tk.Button(root, text="Generate", font=('Arial', 15))
gen_button.pack(pady=20)

root.mainloop()