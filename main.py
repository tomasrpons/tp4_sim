from clases import Demanda_x_dia, Demoras, Costos




def main():
    while(True):

        demanda_x_dia, demoras, decenas_x_costos = cargaDatos()

        





        
        







        
    
def cargaDatos():
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