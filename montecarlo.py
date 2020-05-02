import random


def tabla_montecarlo_A(tabla_demanda, tabla_demora, tabla_pedido, dias, pedidos_cada, cant):

    stock_anterior = 20
    resolucion = []
    pendiente_entrada = False

  
    for i in range (dias):
        hay_ruptura = False  # Banderapara el costo de ruptura. Empieza en false
        if pedidos_cada == i:
            pedidos_cada += pedidos_cada        #Defino el proximo día que llegan los pedidos
            rnd_demora = random.uniform(0,1)
            pendiente_entrada = True
            indice_demora = get_indicie(tabla_demora.acumulador,rnd_demora)
            demora=tabla_demora.dias[indice_demora]+i

        if pendiente_entrada & demora==i:
            stock_anterior += stock_anterior + cant
            pendiente_entrada = False

        rnd_demanda = random.uniform(0,1)
        indice = get_indicie(tabla_demanda.acumulador,rnd_demanda)
        demanda = tabla_demanda.dias[indice]      #Valor dela demanda
        if demanda <= stock_anterior:           #Defino el nuevo stock
            stock_anterior -= demanda
        else:
            ruptura = demanda - stock_anterior
            stock_anterior = 0
            hay_ruptura = True              #Defino si hay ruptura

        costo_mantenimiento =  stock_anterior * 3
        if hay_ruptura:
            costo_ruptura = ruptura * 4
        else:
            costo_ruptura = 0

        costo_total=costo_mantenimiento+costo_ruptura

        costo_acumulado=costo_total

def get_indicie(tabla,valor):
    for i in range(len(tabla)):
        if valor < tabla[i]:
            return i