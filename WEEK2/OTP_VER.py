#------------------------------------------------------------------Library-----------------------------------------------------------------
import random
import smtplib
import tkinter as tk
from tkinter import messagebox

#----------------------------------------------------------------OTP_6_digit---------------------------------------------------------------

otp = random.randint(100000, 999999)

#------------------------------------------------------------------Functions---------------------------------------------------------------
def email_send(user_email):

        email_sender = 'hagerashry0@gmail.com'
        email_password = 'hlfcbaqyvxhdvghf'
       
        message = f'Subject: OTP Verification\n\n OTP is : {otp}'
        
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, user_email, message)
        
        messagebox.showinfo("Success", "OTP sent successfully!")	

def verify_otp(user_otp):
    if int(user_otp) == otp:
        messagebox.showinfo("Success", "OTP verified successfully!")
    else:
        messagebox.showerror("Error", "Invalid OTP!")

#--------------------------------------------------------------------GUI------------------------------------------------------------------  

root = tk.Tk()
root.title("OTP Verification Project")
root.geometry("250x200")

tk.Label(root, text="Enter your email:").pack(pady=5)

email_entry = tk.Entry(root)
email_entry.pack(pady=5)

tk.Label(root, text="Enter OTP:").pack(pady=5)

otp_entry = tk.Entry(root)
otp_entry.pack(pady=5)

tk.Button(root, text="Send OTP", command=lambda: email_send(email_entry.get())).pack(pady=5)

tk.Button(root, text="Verify", command=lambda: verify_otp(otp_entry.get())).pack(pady=5)


root.mainloop()


