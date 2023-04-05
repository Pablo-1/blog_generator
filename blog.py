import tkinter as tk

root = tk.Tk()

# main window dimensions
root.geometry("600x500")
root.title("Blogpost generator GUI")

label = tk.Label(root, text="Generate a blogpost", font=('Arial', 20))
label.pack(padx=20, pady=20)

# subject box label 
title_box_lab = tk.Label(root, text="Type the subject of your post in the box below.", font=('Arial', 15))
title_box_lab.pack(pady=10)

# subject box
textbox = tk.Text(root, font=('Arial', 15), height=2)
textbox.pack(padx=20)


gen_button = tk.Button(root, text="Generate", font=('Arial', 15))
gen_button.pack(pady=10)

blogpost_lab = tk.Label(root, text="Your blogpost below.", font=('Arial', 15))
blogpost_lab.pack(pady=10)

blogpost_box = tk.Text(root, font=('Arial', 20), height=10)
blogpost_box.pack(padx=20)

root.mainloop()