import openai
import tkinter as tk

# Generate the secret_key on openai website
openai.api_key = "secret_key"

# Create the main window
root = tk.Tk()
root.geometry("600x500")
root.title("Blogpost generator GUI")

# Subject box label
title_box_lab = tk.Label(root, text="Type the subject of your post in the box below.", font=('Arial', 15))
title_box_lab.pack(pady=10)

# Subject box
textbox = tk.Text(root, font=('Arial', 15), height=2)
textbox.pack(padx=20)

# Generate blog button
def generate_blogpost():
    # Get the subject from the textbox from first character to last -1 which is new line character 
    subject = textbox.get("1.0", "end-1c")

    # if subject box has been left empty
    if not subject:
        blogpost_box.delete("1.0", "end")
        blogpost_box.insert("1.0", "Please enter a subject for your blog post.")
        return

    # Generating the blogpost with ChatGPT API
    response = openai.Completion.create(
        # GPT engine 
        engine="text-davinci-002",
        # Prompt to generate the blogpost
        prompt=f"Write a blog post on {subject}.",
        # Argument on the scale of 0.0 to 1.0, controls creativity and risktaking 
        temperature=0.5,
        #Number of tokens
        max_tokens=1024,
        # Number of responses to generate
        n=1,
        # Argument stops generating response if the condition is met, set to None
        stop=None,
        # Number of seconds for response to be generated before its terminated
        timeout=10,
    )

    # Get the generated blog post from the API response
    blogpost = response.choices[0].text

    # Insert the blog post into the blogpost box
    blogpost_box.configure(wrap='word')
    blogpost_box.delete("1.0", "end")
    blogpost_box.insert("1.0", blogpost)

gen_button = tk.Button(root, text="Generate", font=('Arial', 15), command=generate_blogpost)
gen_button.pack(pady=10)

# Blog box label
blogpost_lab = tk.Label(root, text="Your blogpost below.", font=('Arial', 15))
blogpost_lab.pack(pady=10)

# Blogpost box
blogpost_box = tk.Text(root, font=('Arial', 15), height=15)
blogpost_box.pack(padx=20)

root.mainloop()