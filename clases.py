import random

class Demanda_x_dia(object):
    def __init__(self, intervalos, probabilidades):
        self.intervalos = intervalos
        self.probabilidades = probabilidades
        self.acumulador=[]

    def set_acumulador(self):
        aux=[0]*len(self.probabilidades)
        for i in range(len(self.probabilidades)):
            aux[i]=sum(aux)+self.probabilidades[i]
        self.acumulador=aux

class Demoras(object):
    def __init__(self,dias, probabilidades):
        self.dias = dias
        self.probabilidades = probabilidades
        self.acumulador=[]

    def set_acumulador(self):
        aux=[0]*len(self.probabilidades)
        for i in range(len(self.probabilidades)):
            aux[i]=sum(aux)+self.probabilidades[i]
        self.acumulador=aux


class Costos(object):
    def __init__(self,decenas_pedidas, costos):
        self.decenas_pedidas = decenas_pedidas
        self.costos = costos


class Resolucion(object):
    def __init__(self, dia,rnd_demanda,demanda,pedido,rnd_demora,demora,stock,decenas_pedidas,costo_orden,costo_almacenamiento,costo_ruptura,costo_total,acumulador_costo, promedio_costo, acumulador_demanda):
        self.dia = dia
        self.rnd_demanda = rnd_demanda
        self.demanda= demanda
        self.pedido= pedido
        self.rnd_demora = rnd_demora
        self.demora = demora
        self.stock = stock
        self.decenas_pedidas = decenas_pedidas
        self.costo_orden = costo_orden
        self.costo_almacenamiento = costo_almacenamiento
        self.costo_ruptura = costo_ruptura
        self.costo_total = costo_total
        self.acumulador_costo = acumulador_costo
        self.promedio_costo = promedio_costo
        self.acumulador_demanda = acumulador_demanda

    def __list__(self):
        return [self.dia, self.rnd_demanda, self.demanda, self.pedido, self.rnd_demora, self.demora, self.stock,self.decenas_pedidas, self.costo_orden, self.costo_almacenamiento, self.costo_ruptura, self.costo_total, self.acumulador_costo, self.promedio_costo]

        
    