# pip install customtkinter
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('600x350')

def login():
    print('login')
    
frame = customtkinter.CTkFrame(master=root)

frame.pack(padx=60, pady=20, fill='both', expand=True)

label1 = customtkinter.CTkLabel(master=frame, text='Login System', font=('Roboto', 24))
label1.pack(padx=10, pady=12)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Username')
entry1.pack(padx=10, pady=12)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show='*')
entry2.pack(padx=10, pady=12)

button1 = customtkinter.CTkButton(master=frame, text='Login', command=login)
button1.pack(padx=10, pady=12)

checkbox1 = customtkinter.CTkCheckBox(master=frame, text='Remember me')
checkbox1.pack(padx=10, pady=12)

root.mainloop()