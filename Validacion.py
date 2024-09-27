import tkinter as tk
import re
from tkinter import messagebox

def reset_fields():
    txt_first_name.delete(0, tk.END)
    txt_last_name.delete(0, tk.END)
    txt_height.delete(0, tk.END)
    txt_phone.delete(0, tk.END)
    txt_age.delete(0, tk.END)
    gender_var.set(0)

# Validaciones
def valid_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def valid_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def valid_phone(value):
    return value.isdigit() and len(value) == 10

def valid_text(value):
    return bool(re.match("^[a-zA-Z\s]+$", value))


def submit():
    first_name = txt_first_name.get()
    last_name = txt_last_name.get()
    age = txt_age.get()
    phone = txt_phone.get()
    height = txt_height.get()
    gender = ""
    
    if gender_var.get() == 1:
        gender = "Masculino"
    elif gender_var.get() == 2:
        gender = "Femenino"
    
    # Validar los datos
    if (valid_int(age) and valid_float(height) and valid_phone(phone) and valid_text(first_name) and valid_text(last_name)):
        user_data = (f"Nombre(s): {first_name}\nApellidos: {last_name}\nEdad: {age}\n"
                     f"Celular: {phone}\nEstatura: {height}\nGénero: {gender}")
        with open("UserData.txt", "a") as file:
            file.write(user_data + "\n\n")
        messagebox.showinfo("Información", "Registro Exitoso\n\n" + user_data)
    else:
        messagebox.showerror("Error", "Error al guardar los datos\n\nFormato incorrecto")
    
    reset_fields()

# Interfaz gráfica
app = tk.Tk()
app.geometry("480x640")
app.title("Formulario")

gender_var = tk.IntVar()

lbl_first_name = tk.Label(app, text="Nombre(s): ")
lbl_first_name.pack()
txt_first_name = tk.Entry(app)
txt_first_name.pack()

lbl_last_name = tk.Label(app, text="Apellidos:")
lbl_last_name.pack()
txt_last_name = tk.Entry(app)
txt_last_name.pack()

lbl_age = tk.Label(app, text="Edad:")
lbl_age.pack()
txt_age = tk.Entry(app)
txt_age.pack()

lbl_phone = tk.Label(app, text="Celular:")
lbl_phone.pack()
txt_phone = tk.Entry(app)
txt_phone.pack()

lbl_height = tk.Label(app, text="Estatura:")
lbl_height.pack()
txt_height = tk.Entry(app)
txt_height.pack()

lbl_gender = tk.Label(app, text="Género:")
lbl_gender.pack()
rb_male = tk.Radiobutton(app, text="Masculino", variable=gender_var, value=1)
rb_male.pack()
rb_female = tk.Radiobutton(app, text="Femenino", variable=gender_var, value=2)
rb_female.pack()

btn_reset = tk.Button(app, text="Limpiar Campos", command=reset_fields)
btn_reset.pack()

btn_submit = tk.Button(app, text="Enviar Formulario", command=submit)
btn_submit.pack()

app.mainloop()
