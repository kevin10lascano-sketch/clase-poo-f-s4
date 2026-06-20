class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}\nEmail: {self.email}"
    
    def __str__(self):
        return self.nombre