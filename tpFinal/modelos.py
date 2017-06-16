import numpy as np
import json

class Producto:
	def __init__(self, nombre, stock=0):
		self.nombre = nombre
		self.stock = stock		

	def decrementar_stock(self, cant):
		assert int(cant) >= 0 and int(cant) <= self.stock, "Cantidad negativo, excesiva o incorrecta"
		self.stock -= cant		

	def aumentar_stock(self, cant):
		assert int(cant) >= 0, "No se puede aumentar stock con cantidad negativa"
		self.stock += cant

class Produccion:
	def __init__(self, producto, cantidad):
		assert type(cantidad) == int and cantidad > 0   
		self.producto = producto
		self.cantidad = cantidad

	def producir(self):
		self.producto.aumentar_stock(self.cantidad)
		return self.cantidad

class Demanda:

	def __init__(self, funcion, parametros):
		self.funcion = funcion
		self.parametros = parametros

	def aleatoria(self):
		return self.funcion(**self.parametros)

class Empleado:
	def __init__(self):
		self.atenciones = []

	def agregar_atencion(self, atencion):
		assert atencion.producto not in map(lambda a: a.producto, self.atenciones),"Producto repetido para el Empleado"
		self.atenciones.append(atencion)

	def cantidad_atender(self):
		assert self.atenciones, "Empleado sin atenciones"
		r = min(map(lambda a: a.cantidad_atender(), self.atenciones))
		return r


class Atencion:

	def __init__(self, producto, funcion, parametros=None, unidad_tiempo=1):
		self.producto = producto
		self.funcion = funcion
		self.unidad_tiempo = unidad_tiempo
		self.parametros = parametros
		self.parametros['lam'] = float(self.unidad_tiempo) / self.parametros['lam']
		
	def cantidad_atender(self):
		return self.funcion(**self.parametros)


class Estadisticas:

	def init_response(self):
		return {
			'anio':None,
			'cant_total_acumulada':0, 
			'prom_acumulado_por_dia':0,
			'cant_dias_falta_stock':0,
			'cant_demandas_sin_atender_por_falta_stock':0,
			'cant_dias_demoras_empl':0,
			'cant_demandas_sin_atender_por_demoras_empl':0,
			'total_demandas': 0,
			'demandas_insatisfechas':0
		}

	def getEstadisticas(self, result):
		stats_anio = self.init_response()
		respuestas= []
		for dict_anio in result['simulacion']:
			stats_anio['anio']= dict_anio['anio']
			for e in dict_anio['eventos']:
				stats_anio['cant_total_acumulada'] += e['acumulado']
				stats_anio['total_demandas'] += e['demanda']
				stats_anio['demandas_insatisfechas'] = min(e['demanda'], e['acumulado'])			
				if self.falto_stock(e):
					stats_anio['cant_dias_falta_stock'] += 1 
					stats_anio['cant_demandas_sin_atender_por_falta_stock'] += stats_anio['demandas_insatisfechas']
				if self.demora_empleados(e):
					stats_anio['cant_dias_demoras_empl'] += 1 
					stats_anio['cant_demandas_sin_atender_por_demoras_empl'] += stats_anio['demandas_insatisfechas']
			stats_anio['prom_acumulado_por_dia'] = stats_anio['cant_total_acumulada'] / len(dict_anio['eventos'])
			respuestas.append(stats_anio)
			stats_anio = self.init_response()
		
		promedios = {
			"cant_total_acumulada": int(np.average(map(lambda r: r['cant_total_acumulada'],respuestas))),
			"prom_acumulado_por_dia": int(np.average(map(lambda r: r['prom_acumulado_por_dia'],respuestas))),
			"cant_dias_falta_stock": int(np.average(map(lambda r: r['cant_dias_falta_stock'],respuestas))),
			"cant_dias_demoras_empl": int(np.average(map(lambda r: r['cant_dias_demoras_empl'],respuestas))),
			"cant_demandas_sin_atender_por_falta_stock": int(np.average(map(lambda r: r['cant_demandas_sin_atender_por_falta_stock'],respuestas))),
			"cant_demandas_sin_atender_por_demoras_empl": int(np.average(map(lambda r: r['cant_demandas_sin_atender_por_demoras_empl'],respuestas))),
			"total_dias": int(np.average(map(lambda s: len(s['eventos']),result['simulacion']))),
			"promedio_total_demandas": int(np.average(map(lambda r: r['total_demandas'],respuestas)))
		}
		

		return {
			'promedios_por_anios':respuestas,
			'promedios_totales':promedios
		}

	def falto_stock(self, evento):
		return  evento['acumulado'] > 0 and min(map(lambda p: p.values()[0], evento['stock'])) == 0

	def demora_empleados(self, evento):
		return evento['acumulado'] > 0 and min(map(lambda p: p.values()[0], evento['stock'])) > 0


class Simulacion:

	ESTADOS = ['nada', 'configurada', 'iniciada', 'finalizada']
	
	def __init__(self):
		self.estado = 'nada'
		self.response = []	

	def configurar(self, json_config):
		self.dias_mes = json_config['dias_mes']
		self.meses_anio = json_config['meses_anio']
		self.cant_anios = json_config['cant_anios']
		self.dias_produccion = json_config['dias_produccion']
		self.horas_trabajo = json_config['empleados']['horas_trabajo']
		self.empleados = []
		self.productos = []
		self.produccion = []

		self.demanda = Demanda(eval(json_config['demanda']['funcion']), json_config['demanda']['parametros'])
		
		for i in range(json_config['empleados']['cantidad']):
			self.empleados.append(Empleado())

		for producto in  json_config['productos']:
			p = Producto(producto['nombre'], producto['stock'])
			self.productos.append(p)
			self.produccion.append(Produccion(p, producto['produccion_por_dia']))
			
			atencion = Atencion(p, eval(producto['funcion_tiempo_atencion']), producto['parametros'], self.horas_trabajo*60)
			for e in self.empleados:
				e.agregar_atencion(atencion)
				
		self.estado = 'configurado'
		return 'ok'

	def iniciar(self):
		self.response = {
			"simulacion":[]
		}
		for anio in range(1, self.cant_anios + 1):
			cola = {'anio':anio, 'eventos':[]}
			for mes in range(1, self.meses_anio + 1):
				for dia in range(1, self.dias_mes + 1):
					# el acum dia anterior o cero
					acum_dia = cola['eventos'][-1]['acumulado'] if cola['eventos'] else 0 
					demanda_random = self.demanda.aleatoria()
					acum_dia += demanda_random
					if dia <= self.dias_produccion:
						for produccion in self.produccion: produccion.producir()
					atencion_empl = sum(map(lambda e: e.cantidad_atender(), self.empleados))
					satisfecho = min(acum_dia, atencion_empl, min(map(lambda p:p.stock, self.productos)))
					for producto in self.productos: producto.decrementar_stock(satisfecho)
					acum_dia -= satisfecho
					stock = [{p.nombre:p.stock} for p in self.productos]
					cola['eventos'].append({
						'acumulado':acum_dia,
						'demanda':demanda_random,
						'dia': "%d - %d"%(dia, mes),
						'stock':stock
						})
			self.response['simulacion'].append(cola)						
		self.estado = 'finalizado'
		return self.response