from abc import ABC, abstractmethod


# class Estudiante:
#     def _init_(self, nombre, valor_matricula, id):
#         self.nombre = nombre
#         self.valor_matricula = valor_matricula
#         self.id = id


# class Descuento(ABC):
#     @abstractmethod
#     def calcular(self, valor_matricula):
#         pass


# class MatriculaHonor(Descuento):
#     def _init_(self, porcentaje=0.50):
#         self.porcentaje = porcentaje

#     def calcular(self, valor_matricula):
#         return valor_matricula * self.porcentaje


# class Convenio(Descuento):
#     def _init_(self, porcentaje=0.20):
#         self.porcentaje = porcentaje

#     def calcular(self, valor_matricula):
#         return valor_matricula * self.porcentaje


# class Monitoria(Descuento):
#     def _init_(self, horas, valor_hora=15000):
#         self.horas = horas
#         self.valor_hora = valor_hora

#     def calcular(self, valor_matricula):
#         return self.horas * self.valor_hora


# # 3. Responsabilidad: liquidar la matrícula aplicando los descuentos
# class CalculadoraLiquidacion:
#     def liquidar(self, estudiante, descuentos):
#         total_descuento = sum(
#             d.calcular(estudiante.valor_matricula)
#             for d in descuentos
#         )

#         total_descuento = min(
#             total_descuento, estudiante.valor_matricula
#         )

#         return estudiante.valor_matricula - total_descuento


# # 4. Responsabilidad: mostrar el resultado
# class ReporteLiquidacion:
#     def imprimir(self, estudiante, descuentos, total):
#         print(f"Estudiante: {estudiante.nombre} (ID {estudiante.id})")
#         print(f"Matrícula base: ${estudiante.valor_matricula:,.0f}")

#         for d in descuentos:
#             print(
#                 f"  - {type(d)._name_}: "
#                 f"-${d.calcular(estudiante.valor_matricula):,.0f}"
#             )

#         print(f"Total a pagar: ${total:,.0f}")


# if _name_ == "_main_":
#     est = Estudiante("Juan", 5_000_000, 1)

#     descuentos = [
#         MatriculaHonor(),
#         Convenio(0.10),
#         Monitoria(horas=40)
#     ]

#     total = CalculadoraLiquidacion().liquidar(est, descuentos)

#     ReporteLiquidacion().imprimir(est, descuentos, total)

#---------------------------15 oct---------------------------#


class EmailSender:
    def senEmail(self, message):
        print("Enviado notificación{message}")

class SMSSender:
    pass

class WhatsappSender:
    pass


class NotificationService:
    def _init_(self):
        #Ya estor "amarrando" la funcionalidad a una implementracion concreta
        self.sender = EmailSender

    def sendNotification(self, message):
        self.snder.sendEmail(message)


#COMO LO SOLUCIONAMOS:
#Creamos una interfaz que define eñ contrato de las notificaciones
class INotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(INotificationService):
    def send(self, message):
        print("Enviando notificación:{message}, por email")

class SMSSender(INotificationService):
    def send(self, message):
        print(f"Enviando notificación:{message}, por sms")

class WhatsappSender(INotificationService):
    def send(self, message):
        print(f"Enviando notificación:{message}, por whatsapp")

#ESTA ES LA CLASE DE ALTO NIVEL QUE DEPENDE DE LA ABSTACCIÓN (LA INTERFAZ):
class NotificationService:
    #aqui aplicamos inyeccion de dependencia:
    def _init_(self, sender:NotificationService):
        self.sender = sender

    def sendNotification(self, message):
        self.sender.send(message)


sender_vis_sms = SMSSender()
myNotificationService = INotificationService(sender_vis_sms)
myNotificationService.send("Hola ya llego el pedido")
