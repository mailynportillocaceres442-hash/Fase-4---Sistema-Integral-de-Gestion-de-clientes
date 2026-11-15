import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import clientes


# ==========================================
# CONFIGURACIÓN GENERAL
# ==========================================

VENTANA_ANCHO = 1100
VENTANA_ALTO = 700

COLOR_FONDO = "#F2F5FA"
COLOR_MENU = "#173B63"
COLOR_MENU_HOVER = "#245581"
COLOR_BLANCO = "#FFFFFF"
COLOR_TEXTO = "#263445"
COLOR_SECUNDARIO = "#718096"
COLOR_AZUL = "#2878B5"


# ==========================================
# VENTANA PRINCIPAL
# ==========================================

ventana = tk.Tk()
ventana.title("SOFTWARE FJ | Sistema de Gestión")
ventana.geometry("1100x700")
ventana.minsize(900, 600)
ventana.configure(bg=COLOR_FONDO)

# Centrar ventana
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

pos_x = (ancho_pantalla - VENTANA_ANCHO) // 2
pos_y = (alto_pantalla - VENTANA_ALTO) // 2

ventana.geometry(
    f"{VENTANA_ANCHO}x{VENTANA_ALTO}+{pos_x}+{pos_y}"
)


# ==========================================
# MENÚ LATERAL
# ==========================================

menu_lateral = tk.Frame(
    ventana,
    bg=COLOR_MENU,
    width=245
)

menu_lateral.pack(side="left", fill="y")
menu_lateral.pack_propagate(False)


# Logo
logo = tk.Label(
    menu_lateral,
    text="SOFTWARE FJ",
    font=("Arial", 22, "bold"),
    bg=COLOR_MENU,
    fg=COLOR_BLANCO
)
logo.pack(pady=(30, 5))


subtitulo = tk.Label(
    menu_lateral,
    text="SISTEMA DE GESTIÓN",
    font=("Arial", 9, "bold"),
    bg=COLOR_MENU,
    fg="#B8D4EF"
)
subtitulo.pack(pady=(0, 30))


# Título del menú
titulo_menu = tk.Label(
    menu_lateral,
    text="MENÚ PRINCIPAL",
    font=("Arial", 10, "bold"),
    bg=COLOR_MENU,
    fg="#B8D4EF",
    anchor="w"
)
titulo_menu.pack(fill="x", padx=22, pady=(0, 12))


# ==========================================
# ÁREA CENTRAL DE CONTENIDO
# ==========================================

area_principal = tk.Frame(
    ventana,
    bg=COLOR_FONDO
)

area_principal.pack(
    side="right",
    fill="both",
    expand=True
)


# Encabezado
encabezado = tk.Frame(
    area_principal,
    bg=COLOR_BLANCO,
    height=85
)

encabezado.pack(fill="x")
encabezado.pack_propagate(False)


titulo = tk.Label(
    encabezado,
    text="Panel de administración",
    font=("Arial", 21, "bold"),
    bg=COLOR_BLANCO,
    fg=COLOR_TEXTO
)

titulo.pack(side="left", padx=30, pady=20)


# Espacio donde aparecerán los módulos
contenido = tk.Frame(
    area_principal,
    bg=COLOR_FONDO
)

contenido.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=25
)


# ==========================================
# BARRA DE ESTADO
# ==========================================

estado = tk.Label(
    area_principal,
    text="Sistema iniciado correctamente.",
    font=("Arial", 9),
    bg=COLOR_BLANCO,
    fg=COLOR_SECUNDARIO,
    anchor="w",
    padx=20,
    pady=12
)

estado.pack(side="bottom", fill="x")


# ==========================================
# FUNCIONES DE NAVEGACIÓN
# ==========================================

def limpiar_contenido():

    for widget in contenido.winfo_children():
        widget.destroy()


def mostrar_inicio():

    limpiar_contenido()

    bienvenida = tk.Label(
        contenido,
        text="¡Bienvenido a SOFTWARE FJ!",
        font=("Arial", 22, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_MENU
    )

    bienvenida.pack(anchor="w", pady=(10, 8))

    descripcion = tk.Label(
        contenido,
        text=(
            "Seleccione uno de los módulos del menú lateral "
            "para acceder a sus funcionalidades."
        ),
        font=("Arial", 11),
        bg=COLOR_FONDO,
        fg=COLOR_SECUNDARIO
    )

    descripcion.pack(anchor="w", pady=(0, 25))

    tarjeta = tk.Frame(
        contenido,
        bg=COLOR_BLANCO,
        highlightbackground="#DCE4EE",
        highlightthickness=1
    )

    tarjeta.pack(fill="x", pady=10)

    tk.Label(
        tarjeta,
        text="Panel principal",
        font=("Arial", 16, "bold"),
        bg=COLOR_BLANCO,
        fg=COLOR_MENU
    ).pack(anchor="w", padx=25, pady=(22, 10))

    tk.Label(
        tarjeta,
        text=(
            "Desde esta interfaz podrá acceder a los módulos "
            "de clientes, servicios, reservas, salas, alquiler "
            "de equipos, asesorías y consulta de registros.\n\n"
            "Cada módulo cuenta con un archivo independiente "
            "dentro del proyecto SOFTWARE FJ."
        ),
        font=("Arial", 11),
        bg=COLOR_BLANCO,
        fg=COLOR_TEXTO,
        justify="left",
        wraplength=650
    ).pack(anchor="w", padx=25, pady=(0, 25))

    estado.config(text="Página de inicio")


def abrir_clientes():

    limpiar_contenido()

    try:
        clientes.mostrar(contenido)

        estado.config(text="Módulo Clientes abierto correctamente.")

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"No fue posible abrir el módulo Clientes:\n{error}"
        )


def mostrar_modulo_pendiente(nombre):

    limpiar_contenido()

    tk.Label(
        contenido,
        text=nombre.upper(),
        font=("Arial", 22, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_MENU
    ).pack(anchor="w", pady=15)

    tk.Label(
        contenido,
        text=f"El módulo {nombre} está pendiente de desarrollo.",
        font=("Arial", 12),
        bg=COLOR_FONDO,
        fg=COLOR_SECUNDARIO
    ).pack(anchor="w", pady=10)

    estado.config(text=f"Módulo seleccionado: {nombre}")


# ==========================================
# BOTONES DEL MENÚ
# ==========================================

modulos = [
    ("Inicio", mostrar_inicio),
    ("Entidades", lambda: mostrar_modulo_pendiente("Entidades")),
    ("Clientes", abrir_clientes),
    ("Servicios", lambda: mostrar_modulo_pendiente("Servicios")),
    ("Servicios especializados", lambda: mostrar_modulo_pendiente("Servicios especializados")),
    ("Reservas", lambda: mostrar_modulo_pendiente("Reservas")),
    ("Salas", lambda: mostrar_modulo_pendiente("Salas")),
    ("Alquiler de equipos", lambda: mostrar_modulo_pendiente("Alquiler de equipos")),
    ("Asesorías", lambda: mostrar_modulo_pendiente("Asesorías")),
    ("Consultar registros", lambda: mostrar_modulo_pendiente("Consultar registros"))
]


for nombre, funcion in modulos:

    boton = tk.Button(
        menu_lateral,
        text=nombre,
        font=("Arial", 10, "bold"),
        bg=COLOR_MENU,
        fg=COLOR_BLANCO,
        activebackground=COLOR_MENU_HOVER,
        activeforeground=COLOR_BLANCO,
        relief="flat",
        bd=0,
        cursor="hand2",
        anchor="w",
        padx=22,
        pady=9,
        command=funcion
    )

    boton.pack(fill="x", padx=8, pady=2)

    boton.bind(
        "<Enter>",
        lambda evento, b=boton: b.config(bg=COLOR_MENU_HOVER)
    )

    boton.bind(
        "<Leave>",
        lambda evento, b=boton: b.config(bg=COLOR_MENU)
    )


# ==========================================
# PIE DEL MENÚ
# ==========================================

pie_menu = tk.Label(
    menu_lateral,
    text="SOFTWARE FJ\nVersión 1.0",
    font=("Arial", 9),
    bg=COLOR_MENU,
    fg="#B8D4EF",
    justify="center"
)

pie_menu.pack(side="bottom", pady=25)


# ==========================================
# INICIAR EN LA PÁGINA DE BIENVENIDA
# ==========================================

mostrar_inicio()

ventana.mainloop()
