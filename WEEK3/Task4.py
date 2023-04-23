#------------------------------------------------------------------Library-----------------------------------------------------------------
import tkinter as tk
import pyshorteners

s = pyshorteners.Shortener()

#------------------------------------------------------------------Functions---------------------------------------------------------------

	
def To_copied_URL_new(label_text):
    root.clipboard_clear()
    root.clipboard_append(label_text.get())

def copy_button(url_short,label_text):
	url_short.bind("<Button-1>", To_copied_URL_new(label_text))
	
def url_shorten():
    url_long_data = url_long_input.get()
    url_short_data = s.tinyurl.short(url_long_data)
   
    tk.Label(root, text="Shortened URL is :").pack(pady=1)
    
    label_text = tk.StringVar(value=url_short_data)
    url_short = tk.Label(root, textvariable=label_text ,highlightthickness=2, highlightbackground="black")
    url_short.pack(pady=5)
    
    tk.Button(root, text="Copy URL", command=copy_button(url_short,label_text)).pack(pady=5)
    

#--------------------------------------------------------------------GUI------------------------------------------------------------------  
root = tk.Tk()
root.title("URL Shortener")
root.geometry("250x170")

tk.Label(root, text="Enter URL you want to be short :").pack(pady=5)

url_long_input = tk.Entry(root)
url_long_input.pack(pady=5)

tk.Button(root, text="Shorten URL", command=url_shorten).pack(pady=5)

root.mainloop()



