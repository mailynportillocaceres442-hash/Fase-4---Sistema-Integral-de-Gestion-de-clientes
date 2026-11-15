import tkinter as tk
from tkinter import messagebox
from models.cliente import Cliente, ClienteError

# ==========================================
# SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ
# ==========================================

# Configuracion de la ventana principal
ventana = tk.Tk()
ventana.title("Software FJ - Sistema Integral de Gestion")
ventana.geometry("950x650")
ventana.resizable(False, False)
ventana.configure(bg="#F2F4F8")

# Colores del sistema
AZUL_OSCURO = "#0973F4"
AZUL_CLARO = "#DCE6F1"
FONDO = "#F2F4F8"
BLANCO = "#FFFFFF"
GRIS = "#64748B"


# ==========================================
# FUNCIONES DE LOS BOTONES
# ==========================================

def modulo_pendiente(nombre):
    messagebox.showinfo(
        "Modulo en desarrollo",
        f"El modulo de {nombre} sera implementado "
        "durante el desarrollo del proyecto."
    )
def abrir_modulo_clientes():
    ventana_clientes = tk.Toplevel(ventana)
    ventana_clientes.title("Software FJ - Gestión de Clientes")
    ventana_clientes.geometry("500x400")
    ventana_clientes.configure(bg="#F2F4F8")

    tk.Label(ventana_clientes, text="Registro de Clientes", font=("Arial", 14, "bold"), bg="#F2F4F8", fg="#0973F4").pack(pady=15)

    tk.Label(ventana_clientes, text="DNI:", bg="#F2F4F8").pack(anchor="w", padx=40)
    entry_dni = tk.Entry(ventana_clientes, width=40)
    entry_dni.pack(padx=40, pady=5)

    tk.Label(ventana_clientes, text="Nombre:", bg="#F2F4F8").pack(anchor="w", padx=40)
    entry_nombre = tk.Entry(ventana_clientes, width=40)
    entry_nombre.pack(padx=40, pady=5)

    tk.Label(ventana_clientes, text="Email:", bg="#F2F4F8").pack(anchor="w", padx=40)
    entry_email = tk.Entry(ventana_clientes, width=40)
    entry_email.pack(padx=40, pady=5)

    tk.Label(ventana_clientes, text="Teléfono:", bg="#F2F4F8").pack(anchor="w", padx=40)
    entry_telefono = tk.Entry(ventana_clientes, width=40)
    entry_telefono.pack(padx=40, pady=5)

    def guardar_cliente():
        try:
            nuevo_cliente = Cliente(
                dni=entry_dni.get(),
                nombre=entry_nombre.get(),
                email=entry_email.get(),
                telefono=entry_telefono.get()
            )
            messagebox.showinfo("Éxito", f"Cliente registrado correctamente:\n{nuevo_cliente}")
            ventana_clientes.destroy()
        except ClienteError as e:
            messagebox.showerror("Error de Validación", str(e))

    btn_guardar = tk.Button(ventana_clientes, text="Guardar Cliente", bg="#0973F4", fg="#FFFFFF", font=("Arial", 10, "bold"), command=guardar_cliente)
    btn_guardar.pack(pady=20)

# ==========================================
# ENCABEZADO
# ==========================================

encabezado = tk.Frame(
    ventana,
    bg=AZUL_OSCURO,
    height=150
)
encabezado.pack(fill="x")
encabezado.pack_propagate(False)

titulo = tk.Label(
    encabezado,
    text="SOFTWARE FJ",
    font=("Arial", 28, "bold"),
    fg=BLANCO,
    bg=AZUL_OSCURO
)
titulo.pack(pady=(25, 5))

subtitulo = tk.Label(
    encabezado,
    text="Sistema Integral de Gestion",
    font=("Arial", 16),
    fg=BLANCO,
    bg=AZUL_OSCURO
)
subtitulo.pack()

descripcion = tk.Label(
    encabezado,
    text="Administracion de clientes, servicios y reservas",
    font=("Arial", 10),
    fg=AZUL_OSCURO,
    bg=AZUL_CLARO
)
descripcion.pack(pady=5)


# ==========================================
# MENSAJE DE BIENVENIDA
# ==========================================

bienvenida = tk.Label(
    ventana,
    text="¡Bienvenido al sistema!",
    font=("Arial", 22, "bold"),
    bg=FONDO,
    fg=AZUL_OSCURO
)
bienvenida.pack(pady=(30, 5))

instruccion = tk.Label(
    ventana,
    text="Seleccione el modulo que desea administrar",
    font=("Arial", 12),
    bg=FONDO,
    fg=GRIS
)
instruccion.pack(pady=(0, 25))


# ==========================================
# MENU PRINCIPAL
# ==========================================

menu = tk.Frame(
    ventana,
    bg=FONDO
)
menu.pack()

opciones = [
    ("CLIENTES", "Administracion de clientes"),
    ("RESERVAS", "Gestion de reservas"),
    ("SALAS", "Reserva de salas"),
    ("ALQUILER DE EQUIPOS", "Gestion de equipos"),
    ("ASESORIAS", "Asesorias especializadas"),
    ("CONSULTAR REGISTROS", "Consulta de operaciones")
]

# Distribucion de los botones en dos columnas
for indice, (nombre, descripcion_modulo) in enumerate(opciones):
    accion = abrir_modulo_clientes if nombre == "CLIENTES" else lambda n=nombre: modulo_pendiente(n)

    fila = indice // 2
    columna = indice % 2

    boton = tk.Button(
        menu,
        text=f"{nombre}\n{descripcion_modulo}",
        font=("Arial", 12, "bold"),
        width=32,
        height=3,
        bg=AZUL_CLARO,
        command=accion,
        fg=AZUL_OSCURO,
        activebackground=AZUL_OSCURO,
        activeforeground=BLANCO,
        relief="flat",
        cursor="hand2",
        command=lambda n=nombre: modulo_pendiente(n)
    )

    boton.grid(
        row=fila,
        column=columna,
        padx=15,
        pady=10
    )


# ==========================================
# PIE DE PAGINA
# ==========================================

pie = tk.Label(
    ventana,
    text="SOFTWARE FJ  |  Sistema de gestion de clientes",
    font=("Arial", 9),
    bg=FONDO,
    fg=GRIS
)
pie.pack(side="bottom", pady=18)


# ==========================================
# EJECUCION DEL SISTEMA
# ==========================================

ventana.mainloop()
