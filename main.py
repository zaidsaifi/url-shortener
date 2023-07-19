import tkinter as tk
import pyshorteners
import pyperclip

def shorten_url():
    url = entry.get()
    if url:
        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(url)
            result_label.config(text=short_url)
            copy_button.config(state=tk.NORMAL) 
        except:
            result_label.config(text="Error: Unable to shorten the URL.")
            copy_button.config(state=tk.DISABLED) 
    else:
        result_label.config(text="Error: Please enter a URL.")
        copy_button.config(state=tk.DISABLED)  

def copy_to_clipboard():
    short_url = result_label.cget("text")
    pyperclip.copy(short_url)

window = tk.Tk()
window.title("URL Shortener")
window.geometry("400x250")
window.configure(bg= "pink")

label = tk.Label(window, text="Enter URL:", font=("consolas", 14), bg = "pink", fg= "black")
label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=10, padx=20, fill=tk.X)

button = tk.Button(window, text="Shorten URL", font=("Arial", 12), command=shorten_url , bg = "#FFA4B6", fg= "black")
button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue", bg= "pink")
result_label.pack(pady=10)

copy_button = tk.Button(window, text="Copy", font=("Arial", 12), command=copy_to_clipboard, state=tk.DISABLED , bg = "#FFA4B6", fg= "black")
copy_button.pack(pady=5)

window.mainloop() 
