import random
from clases import Resolucion


def tabla_montecarlo_A(tabla_demanda, tabla_demora, tabla_pedido, dias, dia_llegada, cant):

    stock_anterior = 20
    resoluciones = []
    pendiente_entrada = False
    decenas_pedidas=180
    costo_orden=0
    demora=-1;
    rnd_demora=0
    intervalo_pedido=dia_llegada

    dia_llegada=0
    

    for i in range (dias):
        decenas_pedidas= 0
        costo_orden = 0
        hay_ruptura = False  # Banderapara el costo de ruptura. Empieza en false
        if dia_llegada == i:
            decenas_pedidas = 180
            dia_llegada += intervalo_pedido        #Defino el proximo día que llegan los pedidos
            rnd_demora = random.uniform(0,1)
            pendiente_entrada = True
            indice_demora = get_indice(tabla_demora.acumulador,rnd_demora)
            demora=tabla_demora.dias[indice_demora]+i
            indice_costo=get_indice(tabla_pedido.decenas_pedidas,decenas_pedidas)
            costo_orden=tabla_pedido.costos[indice_costo]

        if pendiente_entrada and demora==i:
            stock_anterior += stock_anterior + cant
            pendiente_entrada = False
            demora = 0


        rnd_demanda = random.uniform(0,1)
        indice = get_indice(tabla_demanda.acumulador,rnd_demanda)
        demanda = tabla_demanda.intervalos[indice]      #Valor dela demanda
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

        costo_total=costo_mantenimiento+costo_ruptura+costo_orden

        if i==0:
            costo_acumulado=costo_total
        else:
            costo_acumulado=costo_total+resoluciones[i-1].acumulador_costo

        promedio=costo_acumulado/(i+1)

        resolucion = Resolucion(i,rnd_demanda,demanda,dia_llegada,rnd_demora,demora,stock_anterior,decenas_pedidas,costo_orden,costo_mantenimiento,costo_ruptura,costo_total,costo_acumulado, promedio)

        resoluciones.append(resolucion)
        rnd_demora=0
    return resoluciones

def get_indice(tabla,valor):
    for i in range(len(tabla)):
        if valor < tabla[i]:
            return i