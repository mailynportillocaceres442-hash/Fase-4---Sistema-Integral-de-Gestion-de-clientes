# -*- coding: utf-8 -*-
"""
Módulo: cliente.py
Descripción: Define la entidad Cliente con encapsulación estricta, validaciones 
robustas y excepciones personalizadas para la gestión de errores en los datos.
Curso: Programación - UNAD
"""

# ==========================================
# EXCEPCIONES PERSONALIZADAS PARA CLIENTES
# ==========================================

class ClienteError(Exception):
    """Excepción base para todos los errores relacionados con la entidad Cliente."""
    pass


class DniInvalidoError(ClienteError):
    """Se lanza cuando el documento de identidad está vacío o no es numérico."""
    def __init__(self, mensaje="El documento de identidad ingresado no es válido."):
        super().__init__(mensaje)


class NombreInvalidoError(ClienteError):
    """Se lanza cuando el nombre está vacío o contiene caracteres no permitidos (números)."""
    def __init__(self, mensaje="El nombre del cliente no puede estar vacío ni contener números."):
        super().__init__(mensaje)


class EmailInvalidoError(ClienteError):
    """Se lanza cuando el correo electrónico no cumple con la estructura estándar."""
    def __init__(self, mensaje="El formato del correo electrónico es inválido."):
        super().__init__(mensaje)


class TelefonoInvalidoError(ClienteError):
    """Se lanza cuando el teléfono no contiene una longitud o caracteres correctos."""
    def __init__(self, mensaje="El número de teléfono debe contener solo dígitos y una longitud adecuada."):
        super().__init__(mensaje)


# ==========================================
# CLASE ENTIDAD: CLIENTE
# ==========================================

class Cliente:
    """
    Representa a un cliente de la empresa Software FJ.
    Implementa encapsulación mediante atributos privados y propiedades (@property).
    """

    def __init__(self, dni: str, nombre: str, email: str, telefono: str):
        """Constructor de la clase que inicializa y valida los datos del cliente."""
        self.dni = dni          
        self.nombre = nombre    
        self.email = email      
        self.telefono = telefono 

    # --- Propiedad y Validación de DNI ---
    @property
    def dni(self) -> str:
        return self.__dni

    @dni.setter
    def dni(self, valor: str):
        if not valor or not isinstance(valor, str) or not valor.strip():
            raise DniInvalidoError("El DNI del cliente no puede estar vacío.")
        if not valor.strip().isdigit():
            raise DniInvalidoError("El DNI debe contener exclusivamente números.")
        self.__dni = valor.strip()

    # --- Propiedad y Validación de Nombre ---
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not isinstance(valor, str) or not valor.strip():
            raise NombreInvalidoError("El nombre del cliente no puede estar vacío.")
        if any(char.isdigit() for char in valor):
            raise NombreInvalidoError("El nombre del cliente no puede contener números.")
        self.__nombre = valor.strip().title()

    # --- Propiedad y Validación de Email ---
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, valor: str):
        if not valor or not isinstance(valor, str) or not valor.strip():
            raise EmailInvalidoError("El correo electrónico no puede estar vacío.")
        valor_limpio = valor.strip()
        if "@" not in valor_limpio or "." not in valor_limpio.split("@")[-1]:
            raise EmailInvalidoError(f"El correo '{valor_limpio}' no tiene un formato válido.")
        self.__email = valor_limpio

    # --- Propiedad y Validación de Teléfono ---
    @property
    def telefono(self) -> str:
        return self.__telefono

    @telefono.setter
    def telefono(self, valor: str):
        if not valor or not isinstance(valor, str) or not valor.strip():
            raise TelefonoInvalidoError("El teléfono del cliente no puede estar vacío.")
        tel_limpio = valor.strip().replace("+", "").replace(" ", "")
        if not tel_limpio.isdigit() or len(tel_limpio) < 7:
            raise TelefonoInvalidoError("El teléfono debe contener al menos 7 dígitos numéricos.")
        self.__telefono = valor.strip()

    def __str__(self) -> str:
        return f"Cliente [DNI: {self.__dni}, Nombre: {self.__nombre}, Email: {self.__email}, Teléfono: {self.__telefono}]"

    def to_dict(self) -> dict:
        return {
            "dni": self.__dni,
            "nombre": self.__nombre,
            "email": self.__email,
            "telefono": self.__telefono
        }
