import numpy as np
import matplotlib.pyplot as plt
import math
        
DIAS_MES = 30
MESES = 12 # anio
CANT_MUESTRAS = 1

PRODUCCION = {
    'dias': 15,
    'auto_parte_1': 110,
    'auto_parte_2': 160    
}
DEMANDA = {
    'funcion': np.random.poisson,
    'parametros': {'lam': 70}    
}
EMPLEADOS = {
    'cantidad': 2,
    'horas_trabajo':12,  # ponemos que trabajan 12 horas diarias atendiendo demandas
    'funcion': np.random.poisson,
    'auto_parte_1': 8,
    'auto_parte_2': 12
}
cola_de_pedido = []


# En base a la cant de horas de trabajo y de la funcion de tiempo aleatorio de atencion de demanda:
# devuelvo la cantidad de demandas que puede procesra en un dia para auto parte 1 y autoparte 2.
def getCantDemandaEmpleado():
    total_minutos = EMPLEADOS['horas_trabajo'] * 60
    cant_demanda_1 = EMPLEADOS['funcion'](total_minutos/EMPLEADOS['auto_parte_1'])
    cant_demanda_2 = EMPLEADOS['funcion'](total_minutos/EMPLEADOS['auto_parte_2'])
    return cant_demanda_1, cant_demanda_2

# retorno una lista L con cant de demandas para cada empleado. len(L) == cantidad de empleados
def getCantDemandasEmpleados():
    cant_demandas_atender = []
    return [min(getCantDemandaEmpleado()) for i in range(EMPLEADOS['cantidad'])]

def main():    
    for i in range(CANT_MUESTRAS):
        cola_de_pedidos = [{'dia':0, 'mes':1, 'acumulado':0}]
        stock_autoparte_1 = stock_autoparte_2 =  0
        for mes in range(1, MESES + 1):
            for dia in range(1, DIAS_MES + 1 ):
                if dia < PRODUCCION['dias']:
                    stock_autoparte_1 += PRODUCCION['auto_parte_1']        
                    stock_autoparte_2 += PRODUCCION['auto_parte_2']
                cant_acumulada = cola_de_pedidos[len(cola_de_pedidos) - 1]['acumulado']
                demanda_aleatoria = DEMANDA['funcion'](**DEMANDA['parametros'])
                total_demanda_diaria = demanda_aleatoria + cant_acumulada
                cant_demandas_empleados = sum(getCantDemandasEmpleados())
                cant_demandas_satisfechas = min(stock_autoparte_1, stock_autoparte_2, total_demanda_diaria, cant_demandas_empleados)
                stock_autoparte_1 -= cant_demandas_satisfechas
                stock_autoparte_2 -= cant_demandas_satisfechas
                total_demanda_diaria -= cant_demandas_satisfechas
                cola_de_pedidos.append({'dia': dia, 
                                        'mes': mes, 
                                        'acumulado': total_demanda_diaria,
                                        'stock_autoparte_1':stock_autoparte_1,
                                        'stock_autoparte_2':stock_autoparte_2
                                       })
        for cola in cola_de_pedidos: print cola
        mostrar_promedios(cola_de_pedidos[1:])
        
def mostrar_promedios(cola_de_pedidos):
    print "/////// INICIO SIMULACION ///////"
    print "Cantidad total de dias %d"%(len(cola_de_pedidos))
    print "Cantidad total acumulada %d"%(sum(map( lambda dia: dia['acumulado'],cola_de_pedidos)))
    print "Promedio acumulado por dia %d"%(np.average(map(lambda dia: dia['acumulado'],cola_de_pedidos)))
    print "Cantidad de de dias con Demoras por empleados %d"%(len(demoras_empleados(cola_de_pedidos)))
    print "Cantidades demandas sin atender por demoras de empleados %s"%(sum(demoras_empleados(cola_de_pedidos)))
    
def demoras_empleados(cola_de_pedidos):
    return [res for res in map(demora_empleados_en, cola_de_pedidos) if res > 0]

#retorno cantidad de demandas insatisfechas en un dia por demoras de empleados.
def demora_empleados_en(dia):
    return min(min(dia['stock_autoparte_1'], dia['stock_autoparte_2']), dia['acumulado'])   
    
if __name__ == '__main__':
    main()
    