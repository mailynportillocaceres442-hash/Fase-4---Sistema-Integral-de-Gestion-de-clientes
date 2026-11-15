import tkinter as tk
from tkinter import messagebox


# ==========================================
# EXCEPCIONES PERSONALIZADAS PARA CLIENTES
# ==========================================

class ClienteError(Exception):
    """Excepción base para errores relacionados con Cliente."""
    pass


class DniInvalidoError(ClienteError):
    def _init_(self, mensaje="El documento de identidad no es válido."):
        super()._init_(mensaje)


class NombreInvalidoError(ClienteError):
    def _init_(self, mensaje="El nombre no es válido."):
        super()._init_(mensaje)


class EmailInvalidoError(ClienteError):
    def _init_(self, mensaje="El correo electrónico es inválido."):
        super()._init_(mensaje)


class TelefonoInvalidoError(ClienteError):
    def _init_(self, mensaje="El teléfono no es válido."):
        super()._init_(mensaje)


# ==========================================
# CLASE ENTIDAD: CLIENTE
# ==========================================

class Cliente:
    """
    Representa un cliente de SOFTWARE FJ.
    Implementa encapsulación y validación de datos.
    """

    def _init_(self, dni: str, nombre: str, email: str, telefono: str):
        self.dni = dni
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    # DNI
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise DniInvalidoError("El DNI no puede estar vacío.")

        if not valor.strip().isdigit():
            raise DniInvalidoError("El DNI debe contener solamente números.")

        self.__dni = valor.strip()

    # NOMBRE
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise NombreInvalidoError("El nombre no puede estar vacío.")

        if any(char.isdigit() for char in valor):
            raise NombreInvalidoError("El nombre no puede contener números.")

        self.__nombre = valor.strip().title()

    # EMAIL
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise EmailInvalidoError("El correo no puede estar vacío.")

        valor_limpio = valor.strip()

        if "@" not in valor_limpio or "." not in valor_limpio.split("@")[-1]:
            raise EmailInvalidoError("El formato del correo electrónico es inválido.")

        self.__email = valor_limpio

    # TELEFONO
    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise TelefonoInvalidoError("El teléfono no puede estar vacío.")

        tel_limpio = valor.strip().replace("+", "").replace(" ", "")

        if not tel_limpio.isdigit() or len(tel_limpio) < 7:
            raise TelefonoInvalidoError(
                "El teléfono debe contener al menos 7 dígitos numéricos."
            )

        self.__telefono = valor.strip()

    def _str_(self):
        return (
            f"Cliente [DNI: {self._dni}, Nombre: {self._nombre}, "
            f"Email: {self._email}, Teléfono: {self._telefono}]"
        )

    def to_dict(self):
        return {
            "dni": self.__dni,
            "nombre": self.__nombre,
            "email": self.__email,
            "telefono": self.__telefono
        }


# ==========================================
# INTERFAZ GRÁFICA DEL MÓDULO CLIENTES
# ==========================================

# Lista temporal para almacenar los clientes registrados
lista_clientes = []


def mostrar(contenedor):

    # Colores del módulo
    FONDO = "#F2F5FA"
    AZUL = "#173B63"
    BLANCO = "#FFFFFF"
    TEXTO = "#263445"
    SECUNDARIO = "#718096"

    # Título
    titulo = tk.Label(
        contenedor,
        text="MÓDULO DE CLIENTES",
        font=("Arial", 22, "bold"),
        bg=FONDO,
        fg=AZUL
    )
    titulo.pack(anchor="w", pady=(10, 5))

    descripcion = tk.Label(
        contenedor,
        text="Registro y administración de los datos personales de los clientes.",
        font=("Arial", 10),
        bg=FONDO,
        fg=SECUNDARIO
    )
    descripcion.pack(anchor="w", pady=(0, 20))

    # Tarjeta del formulario
    tarjeta = tk.Frame(
        contenedor,
        bg=BLANCO,
        highlightbackground="#DCE4EE",
        highlightthickness=1
    )
    tarjeta.pack(fill="x", pady=(0, 15))

    tk.Label(
        tarjeta,
        text="REGISTRAR NUEVO CLIENTE",
        font=("Arial", 14, "bold"),
        bg=BLANCO,
        fg=AZUL
    ).pack(anchor="w", padx=20, pady=(18, 12))

    # Contenedor de campos
    formulario = tk.Frame(tarjeta, bg=BLANCO)
    formulario.pack(fill="x", padx=20, pady=(0, 15))

    entradas = {}

    campos = [
        ("Documento de identidad (DNI)", "dni"),
        ("Nombre completo", "nombre"),
        ("Correo electrónico", "email"),
        ("Número de teléfono", "telefono")
    ]

    for i, (etiqueta, clave) in enumerate(campos):

        fila = i // 2
        columna = i % 2

        grupo = tk.Frame(formulario, bg=BLANCO)
        grupo.grid(
            row=fila,
            column=columna,
            sticky="ew",
            padx=10,
            pady=8
        )

        tk.Label(
            grupo,
            text=etiqueta,
            font=("Arial", 10, "bold"),
            bg=BLANCO,
            fg=TEXTO
        ).pack(anchor="w", pady=(0, 5))

        entrada = tk.Entry(
            grupo,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )
        entrada.pack(fill="x", ipady=7)

        entradas[clave] = entrada

    formulario.grid_columnconfigure(0, weight=1)
    formulario.grid_columnconfigure(1, weight=1)

    # ==========================================
    # TABLA VISUAL DE CLIENTES
    # ==========================================

    tarjeta_lista = tk.Frame(
        contenedor,
        bg=BLANCO,
        highlightbackground="#DCE4EE",
        highlightthickness=1
    )
    tarjeta_lista.pack(fill="both", expand=True)

    tk.Label(
        tarjeta_lista,
        text="CLIENTES REGISTRADOS",
        font=("Arial", 14, "bold"),
        bg=BLANCO,
        fg=AZUL
    ).pack(anchor="w", padx=20, pady=(15, 10))

    marco_lista = tk.Frame(tarjeta_lista, bg=BLANCO)
    marco_lista.pack(fill="both", expand=True, padx=20, pady=(0, 15))

    columnas = ("dni", "nombre", "email", "telefono")

    tabla = tk.Frame(marco_lista, bg=BLANCO)
    tabla.pack(fill="both", expand=True)

    encabezados = [
        ("DNI", 15),
        ("NOMBRE", 22),
        ("CORREO", 28),
        ("TELÉFONO", 15)
    ]

    for columna, (texto, ancho) in enumerate(encabezados):
        tk.Label(
            tabla,
            text=texto,
            font=("Arial", 9, "bold"),
            bg=AZUL,
            fg=BLANCO,
            width=ancho,
            pady=8
        ).grid(row=0, column=columna, sticky="nsew")

    lista_visual = tk.Frame(tabla, bg=BLANCO)
    lista_visual.grid(row=1, column=0, columnspan=4, sticky="nsew")

    scrollbar = tk.Scrollbar(lista_visual)
    scrollbar.pack(side="right", fill="y")

    listado = tk.Listbox(
        lista_visual,
        font=("Arial", 9),
        height=7,
        yscrollcommand=scrollbar.set,
        relief="flat",
        selectbackground="#B8D4EF"
    )
    listado.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=listado.yview)

    # ==========================================
    # FUNCIONES DEL MÓDULO
    # ==========================================

    def actualizar_lista():

        listado.delete(0, tk.END)

        for cliente in lista_clientes:
            listado.insert(
                tk.END,
                f"{cliente.dni:<15}  {cliente.nombre:<22}  "
                f"{cliente.email:<28}  {cliente.telefono}"
            )

    def limpiar_campos():

        for entrada in entradas.values():
            entrada.delete(0, tk.END)

    def registrar_cliente():

        try:
            dni = entradas["dni"].get()
            nombre = entradas["nombre"].get()
            email = entradas["email"].get()
            telefono = entradas["telefono"].get()

            cliente = Cliente(dni, nombre, email, telefono)

            # Evitar documentos duplicados
            for registrado in lista_clientes:
                if registrado.dni == cliente.dni:
                    raise DniInvalidoError(
                        "Ya existe un cliente registrado con ese documento."
                    )

            lista_clientes.append(cliente)

            actualizar_lista()
            limpiar_campos()

            messagebox.showinfo(
                "Registro exitoso",
                "El cliente se registró correctamente."
            )

        except ClienteError as error:

            messagebox.showerror(
                "Error de validación",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No fue posible registrar el cliente:\n{error}"
            )

    # ==========================================
    # BOTONES
    # ==========================================

    botones = tk.Frame(tarjeta, bg=BLANCO)
    botones.pack(anchor="e", padx=20, pady=(0, 18))

    tk.Button(
        botones,
        text="Registrar cliente",
        font=("Arial", 10, "bold"),
        bg=AZUL,
        fg=BLANCO,
        activebackground="#245581",
        activeforeground=BLANCO,
        relief="flat",
        cursor="hand2",
        padx=18,
        pady=9,
        command=registrar_cliente
    ).pack(side="left", padx=5)

    tk.Button(
        botones,
        text="Limpiar campos",
        font=("Arial", 10, "bold"),
        bg="#E5EAF1",
        fg=TEXTO,
        relief="flat",
        cursor="hand2",
        padx=18,
        pady=9,
        command=limpiar_campos
    ).pack(side="left", padx=5)
