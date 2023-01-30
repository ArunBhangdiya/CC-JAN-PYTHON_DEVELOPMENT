import smtplib
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def send_email():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        username = username_var.get()
        password = password_var.get()
        server.login(username, password)

        subject = subject_var.get()
        body = body_var.get("1.0", "end-1c")
        msg = f"Subject: {subject}\n\n{body}"

        to_email = to_var.get()
        server.sendmail(username, to_email, msg)

        server.close()
        messagebox.showinfo("Success", "Email sent successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error sending email: {e}")

root = tk.Tk()
root.title("Gmail App")
root.resizable(0,0)
root.geometry("350x250")

username_var = tk.StringVar()
username_label = ttk.Label(root, text="Username:")
username_label.grid(row=0, column=0)
username_entry = ttk.Entry(root, textvariable=username_var)
username_entry.grid(row=0, column=1)

password_var = tk.StringVar()
password_label = ttk.Label(root, text="Password:")
password_label.grid(row=1, column=0)
password_entry = ttk.Entry(root, textvariable=password_var, show="*")
password_entry.grid(row=1, column=1)

to_var = tk.StringVar()
to_label = ttk.Label(root, text="To:")
to_label.grid(row=2, column=0)
to_entry = ttk.Entry(root, textvariable=to_var)
to_entry.grid(row=2, column=1)

subject_var = tk.StringVar()
subject_label = ttk.Label(root, text="Subject:")
subject_label.grid(row=3, column=0)
subject_entry = ttk.Entry(root, textvariable=subject_var)
subject_entry.grid(row=3, column=1)

body_label = ttk.Label(root, text="Body:")
body_label.grid(row=4, column=0)
body_var = tk.Text(root, height=5, width=30)
body_var.grid(row=4, column=1, columnspan=2)

send_button = ttk.Button(root, text="Send", command=send_email)
send_button.grid(row=5, column=1, columnspan=4, pady=10)

root.mainloop()