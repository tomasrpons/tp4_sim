from clases import Demanda_x_dia, Demoras, Costos
from montecarlo import tabla_montecarlo_A
import tabulate 




def main():
    while(True):
        
        print('OPCION 1: Cargar los datos manualmente')
        print('OPCION 2: Cargar los datos automaticamente')
        opcion=int(input('Ingrese la opcion solicitada: '))
        
        if opcion == 1:
            print('\nAL LOBBY PETE\n')
        if opcion == 2:
            dias=int(input('Ingrese la cantidad de dias: '))
            demanda_x_dia, demoras, decenas_x_costos = cargaDatos()
            resoluciones = tabla_montecarlo_A(demanda_x_dia, demoras, decenas_x_costos, dias, 7, 180)

            dias=[]
            rnd_demanda=[]
            demanda=[]
            pedido=[]
            rnd_demora=[]
            demoras=[]
            stock=[]
            decenas_pedidas=[]
            costo_orden=[]
            costo_almacen=[]
            costo_ruptura=[]
            costo_acumulado=[]
            costo_total = []
            promedio_costo=[]

            for i in range(len(resoluciones)):
                dias.append(resoluciones[i].dia)
                rnd_demanda.append(resoluciones[i].rnd_demanda)
                demanda.append(resoluciones[i].demanda)
                pedido.append(resoluciones[i].pedido)
                rnd_demora.append(resoluciones[i].rnd_demora)
                demoras.append(resoluciones[i].demora)
                stock.append(resoluciones[i].stock)
                decenas_pedidas.append(resoluciones[i].decenas_pedidas)
                costo_orden.append(resoluciones[i].costo_orden)
                costo_almacen.append(resoluciones[i].costo_almacenamiento)
                costo_ruptura.append(resoluciones[i].costo_ruptura)
                costo_total.append(resoluciones[i].costo_total)
                costo_acumulado.append(resoluciones[i].acumulador_costo)
                promedio_costo.append(resoluciones[i].promedio_costo)

            res={'DIAS':dias,'RND DEMANDA': rnd_demanda,'DEMANDA':demanda,'PEDIDO':pedido,'RND DEMORA':rnd_demora, 'DEMORA':demoras,'STOCK':stock,'DECENAS PEDIDAS':decenas_pedidas,
            'COSTO ORDEN': costo_orden, 'COSTO ALMACEN.': costo_almacen, 'COSTO RUPTURA': costo_ruptura, 'COSTO TOTAL':costo_total, 'COSTO ACUM':costo_acumulado,'PROMEDIO':promedio_costo}
            
            var= tabulate.tabulate(res, headers=['DIA','RND DEMANDA', 'DEMANDA', 'PEDIDO', 'RND DEMORA', 'DEMORA', 'STOCK', 'DECENAS PEDIDAS', 'COSTO ORDEN', 'COSTO ALMACEN.', 'COSTO RUPTURA','COSTO TOTAL' ,'COSTO ACUM.','PROMEDIO COSTO'], tablefmt='fancy_grid')

            print(var)




        
        
        

def cargaDatos():

    demanda_x_dia =Demanda_x_dia([0,10,20,30,40,50], [0.05,0.12,0.18,0.25,0.22,0.18])
    demanda_x_dia.set_acumulador()

    decenas_x_costos=Costos([100,200,9999999], [200,280,300])

    demoras=Demoras([1,2,3,4],[0.15,0.20,0.40,0.25])
    demoras.set_acumulador()

    return demanda_x_dia, demoras, decenas_x_costos


       
    
def cargaDatos_a_mano():
        cantidad_demandas=int(input("Ingrese la cantidad de intervalos posibles: "))

        intervalos=[0]*cantidad_demandas
        probabilidades_demandas=[0]*cantidad_demandas

        demanda_maxima=int(input("Ingrese la demanda maxima de docenas posibles: "))
        for i in range(len(intervalos)):
            if i==0:
                probabilidades_demandas[i]=float(input("Ingrese la probabilidad para el primer intervalo: "))
                continue
            else:
                intervalos[i]=intervalos[i-1]+demanda_maxima/(len(intervalos)-1)
                probabilidades_demandas[i]=float(input("Ingrese la probabilidad para el intervalo "+str(intervalos[i-1])+" - "+str(intervalos[i])+": "))

        demanda_x_dia=Demanda_x_dia(intervalos, probabilidades_demandas)

        cantidad_dias=int(input("Ingrese la cantidad de dias posibles de demora: "))
        dias=[0]*cantidad_dias

        probabilidades_dias=[0]*cantidad_dias
        for i in range(len(dias)):
            dias[i]=i
            probabilidades_dias[i]=float(input("Ingrese la probilidad para el dia "+str(i+1)+":"))

        demoras=Demoras(dias,probabilidades_dias)

        cantidad_decenas=int(input("Ingrese la cantidad de intervalos de decenas pedidas: "))
        intervalos_decenas=[0]*cantidad_decenas

        costos=[0]*cantidad_decenas
        
        for i in range(len(intervalos_decenas)):
            intervalos_decenas[i]=int(input("Ingrese el intervalo "+str(i+1)+": "))
            costos[i]=int(input("Ingrese el costo para ese intervalo: "))

        decenas_x_costos=Costos(intervalos_decenas, costos)

        return demanda_x_dia, demoras, decenas_x_costos



if __name__ == "__main__":
    main()



        #     print('DEMANDAS POR DIA:\n', demanda_x_dia.intervalos,"\n", demanda_x_dia.probabilidades,"\n DEMORAS: \n", demoras.dias,"\n",demoras.probabilidades,"\n DECENAS X COSTOS:\n"
        # , decenas_x_costos.decenas_pedidas, "\n", decenas_x_costos.costos)