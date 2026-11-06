#------------------ EJERCICIO PROX SEMANA ------------------# 
# SISTEMA DE GESTION DE UNA BIBLIOTECA
# (A) LIBROS FISICOS
# (B) E-BOOKS
# (C) AUDIOLIBROS

# 1. ABSTRACCIÓN: Que clase abstrata modela el recurso biblografico (titulo, autor, año)
# 2. HERENCIA: Cada tipo de publicación tiene sus atributos propios
# 3. CADA PUBLICACIÓN TIENE SUS ATRIBUTOS PRIVADOS: usuario en prestamo, fecha de entrega
# 4. POLIMORFISMO: Cada tipo de publicación tiene su propia forma de gestionar

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

from abc import ABC, abstractmethod

class recurso_bibliografico(ABC):
    def __init__(this, titulo:str, autor:str, año:int):
        this.titulo = titulo
        this.autor = autor
        this.año = año
        this._usuario_prestamo = None
        this._fecha_entrega = None

    @abstractmethod
    def gestionar_prestamo(this, usuario:str, fecha_entrega:str):
        pass
    
    @abstractmethod
    def devolver_recurso(this):
        pass

class libro_fisico(recurso_bibliografico):
    def __init__(this, titulo: str, autor: str, año: int, num_paginas: int):
        super().__init__(titulo, autor, año)
        this.num_paginas = num_paginas

    def gestionar_prestamo(this, usuario: str, fecha_entrega: str):
        this._usuario_prestamo = usuario
        this._fecha_entrega = fecha_entrega

        print(f"El libro físico '{this.titulo}' ha sido prestado a {usuario} y debe ser devuelto el {fecha_entrega}.")

    def devolver_recurso(this):
        if this._usuario_prestamo is not None:
            this._usuario_prestamo = None
            this._fecha_entrega = None
            print(f"El libro físico '{this.titulo}' ha sido devuelto y está disponible para préstamo nuevamente.\n")
        else:
            print(f"El libro físico '{this.titulo}' no estaba prestado, por lo que no se puede devolver.\n")

class e_book(recurso_bibliografico):
    def __init__(this, titulo:str, autor:str, año:int, formato:str):
        super().__init__(titulo, autor, año)
        this.formato = formato

    def gestionar_prestamo(this, usuario:str, fecha_entrega:str):
        this._usuario_prestamo = usuario
        this._fecha_entrega = fecha_entrega

        print(f"El e-book '{this.titulo}' se le ha dado acceso digital a {usuario} y se cancela el acceso el {fecha_entrega}.")

    def devolver_recurso(this):
        if this._usuario_prestamo is not None:
            this._usuario_prestamo = None
            this._fecha_entrega = None
            print(f"El e-book '{this.titulo}' ha sido devuelto y el acceso digital ha sido cancelado.\n")
        else:
             print(f"El e-book '{this.titulo}' no estaba prestado, por lo que no se puede devolver.\n")

class audiolibro(recurso_bibliografico):
    def __init__(this, titulo:str, autor:str, año:int, duracion:int):
        super().__init__(titulo, autor, año)
        this.duracion = duracion

    def gestionar_prestamo(this, usuario:str, fecha_entrega:str):
        this._usuario_prestamo = usuario
        this._fecha_entrega = fecha_entrega

        print(f"El audiolibro '{this.titulo}' se le da acceso para escucharlo a {usuario} y se cancela el acceso el {fecha_entrega}.") 

    def devolver_recurso(this):
        if this._usuario_prestamo is not None:
            this._usuario_prestamo = None
            this._fecha_entrega = None
            print(f"El audiolibro '{this.titulo}' ha sido devuelto y el acceso para escucharlo ha sido cancelado.\n")
        else:
            print(f"El audiolibro '{this.titulo}' no estaba prestado, por lo que no se puede devolver.\n")

libro = libro_fisico("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, 863)
libro.gestionar_prestamo("Andrea Arenas", "15-10-2026")
libro.devolver_recurso()

ebook = e_book("1984", "George Orwell", 1949, "PDF")
ebook.gestionar_prestamo("Alejandra López", "20-10-2026")
ebook.devolver_recurso()

audio = audiolibro("El Principito", "Antoine de Saint-Exupéry", 1943, 120)
audio.gestionar_prestamo("Diego Arenas", "25-10-2026")
audio.devolver_recurso() 

recursos = [libro, ebook, audio]
