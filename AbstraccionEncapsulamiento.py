from abc import ABC, abstractmethod

#------------------ (1) ABSTRACCIÓN ------------------#

# INTRODUCCIÓN A LA ABSTRACCIÓN:
#Clase abstrata que define un metodo de pago:
class MetodoPago(ABC):
    @abstractmethod
    #los metodos que empiecen con una referencia a this, o self, son
    #metodos de instancia 
    def procesar_pago(this, monto:float):
        pass


#Clases concretas: metodos d pago especificos: 
class TarjetaCredito(MetodoPago):
    def procesar_pago(this, monto):
        #return supero().procesar_pago(monto)
        print("Procesar pago con tarkeya de credito por el monto ", monto)

class PagoMercadopago(MetodoPago):
    def procesar_pago(this, monto):
        print("Procesando pago mercado pago por: ", monto)

#------------------ (2) ENCAPSULAMIENTO ------------------#     

# INTRODUCCIÓN AL ENCAPSULAMIENTO:

class CuentaBancaria:
    #el primer parametro del metodo init hace referencua a la instancia del objeto:
    def _init_(this, titular:str, numero:int, saldo_inicial:float):
        #todos los atributos de "this", "self", son atributos de instancia:
        this.titular = titular
        this.numero = numero
        this._saldo = saldo_inicial

    def obtener_saldo(this):
        return this._saldo

    def hacer_deposito(this, valor:float):
        if valor > 0:
            this._saldo += valor

    def hacer_retiro(this, valor:float):
        if valor > 0 and this._saldo >= valor:
            this._saldo -= valor

#------------------ (3) HERENCIA ------------------# 

class Empleado(ABC):
    def _init_(this, nombre:str, id:str, salario_base:float):
        this.nombre = nombre
        this.id = id
        this.salario = salario_base


    @abstractmethod
    def liquidar_paso(this):
        pass

class Administrativo(Empleado):
    #el empleado administrativo tiene un atributo adicional: bono
    def _init_(this, nombre:str, id:str, salario_base:float, bono:float):
        this.nombre = nombre
        this.id = id 
        this.salario = salario_base
        this.bono = bono

    def liquidar_pago(this):
        #liquidar pago con el bono:
        return this.salario + this.bono

class Docente(Empleado):

    def _init_(this, nombre:str, id:str, salario_base:float):
        this.nombre = nombre
        this.id = id
        this.salario = salario_base

    def liquidar_pago(this):
        #Liquidar pago sin el bono
        return this.salario
