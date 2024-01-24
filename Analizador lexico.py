import tkinter as tk
from tkinter import ttk, messagebox
import ply.lex as lex

tokens = [
    'PuntoComa',
    'Parentesis_Inicio',
    'Parentesis_Final',
    'Llaves_Inicio',
    'Llaves_Final',
    'Corchetes_Inicio',
    'Corchetes_Final',
    'Comillas',
    'Operadores',
    'Reserverd',
    'ID',
    'NUMBER'
]

reserved = {
    'variable': 'Reserverd',
    'entero': 'Reserverd',
    'cadena': 'Reserverd',
    'flotante': 'Reserverd',
    'boleano': 'Reserverd',
    'para': 'Reserverd',
    'si': 'Reserverd',
    'sino': 'Reserverd',
    'funcion': 'Reserverd',
    'regresar': 'Reserverd',
    'principal': 'Reserverd',
    'mostrar': 'Reserverd',
    'arreglo': 'Reserverd',
}

tokens += list(reserved.values())

# Token patterns
t_Parentesis_Inicio = r'\('
t_Parentesis_Final = r'\)'
t_Llaves_Inicio = r'\{'
t_Llaves_Final = r'\}'
t_Corchetes_Inicio = r'\['
t_Corchetes_Final = r'\]'
t_Comillas = r'"'
t_Operadores = r'(=|==|>|<|\++|\+|-)'
t_PuntoComa = r'\;'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  
    return t

t_ignore = ' \t\n'

def t_error(t):
    error_table.insert('', 'end', values=(f"Illegal character '{t.value[0]}'",))
    t.lexer.skip(1)

lexer = lex.lex()

def check_code():
    # Limpia las tablas de tokens y errores
    token_table.delete(*token_table.get_children())
    error_table.delete(*error_table.get_children())

    # Obtiene el texto del usuario
    code = txt.get("1.0", tk.END).strip()
    if not code:
        messagebox.showinfo("Información", "No hay código para verificar.")
        return

    # Procesa el código con el analizador léxico
    lexer.input(code)
    try:
        for token in lexer:
            token_table.insert('', 'end', values=(token.type, token.value))
        # messagebox.showinfo("Información", "Análisis léxico completado sin errores.")
    except Exception as e:
        print("Error", str(e))
        # messagebox.showerror("Error", str(e))

# Parte de la interfaz gráfica relacionada con el analizador léxico
root = tk.Tk()
root.title("Analizador Léxico")

# Cambios visuales
root.geometry("800x500")  # Tamaño de la ventana
root.configure(bg='#2c3e50')  # Fondo gris oscuro

main_frame = ttk.Frame(root, padding=10)
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Cuadro de texto para el código
codigo = '''Ingresa tu código aquí'''
txt = tk.Text(main_frame, width=80, height=15, wrap=tk.WORD, font=('Arial', 12), bg='#34495e', fg='white')
txt.grid(row=0, column=0, padx=10, pady=10, rowspan=3, columnspan=2)

# Botón de análisis
btn = tk.Button(main_frame, text="Analizar Código", command=check_code, width=20, height=2, bg='#2ecc71', fg='white')
btn.grid(row=0, column=2, padx=10, pady=10, rowspan=3, sticky=tk.W)

# Marco para Tokens
token_frame = ttk.LabelFrame(main_frame, text="Tokens", padding=10)
token_frame.grid(row=0, column=3, padx=10, pady=10, rowspan=3, sticky=tk.N)

# Tabla de Tokens
token_table = ttk.Treeview(token_frame, columns=('Type', 'Value'), show='headings', height=10, style="Custom.Treeview")
token_table.heading('Type', text='Token')
token_table.heading('Value', text='Valor')
token_table.pack()

# Marco para Errores
error_frame = ttk.LabelFrame(main_frame, text="Errores de Sintaxis", padding=10)
error_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky=tk.W)

# Tabla de Errores
error_table = ttk.Treeview(error_frame, columns=('Error',), show='headings', height=5, style="Custom.Treeview")
error_table.heading('Error', text='Mensaje de Error')
error_table.column('Error', width=300)
error_table.pack()

# Etiqueta para resultados
result_label = tk.Label(main_frame, text="", fg="red", bg='#2c3e50', font=('Arial', 12, 'italic'))
result_label.grid(row=4, column=0, columnspan=4, pady=10)

# Estilo personalizado para las tablas
style = ttk.Style()
style.configure("Custom.Treeview", background="#34495e", foreground="white", fieldbackground="#34495e")

root.mainloop()

error_frame = ttk.LabelFrame(main_frame, text="Errores de Sintaxis", padding=10)
error_frame.grid(row=2, column=1, padx=10, pady=10, columnspan=2, sticky=tk.W)

error_table = ttk.Treeview(error_frame, columns=('Error',), show='headings', height=5, style="Custom.Treeview")
error_table.heading('Error', text='Mensaje de Error')
error_table.column('Error', width=300)
error_table.pack()

result_label = tk.Label(main_frame, text="", fg="red", bg='#4a90e2', font=('Helvetica', 12, 'italic'))
result_label.grid(row=3, column=0, columnspan=3, pady=10)

# Estilo personalizado para las tablas
style = ttk.Style()
style.configure("Custom.Treeview", background="#ffffff", foreground="#333333", fieldbackground="#ffffff")

root.mainloop()