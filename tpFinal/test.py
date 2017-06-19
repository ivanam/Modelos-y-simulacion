import unittest
from  modelos import * 
import random
import json
import ast
import numpy as np


class TestProductos(unittest.TestCase):
	
	def setUp(self):
		self.producto = Producto("Autoparte_1")

	def test_nombre_producto(self):
		self.assertEqual(self.producto.nombre, "Autoparte_1")
	
	def test_stock_inicial_defecto_producto(self):
		self.assertEqual(self.producto.stock, 0)

	def test_stock_inicial_producto(self):
		p = Producto("Autoparte_2", 100)
		self.assertEqual(p.stock, 100)

	def test_decrementar_stock_a_cero(self):
		self.producto.stock = 10
		self.producto.decrementar_stock(10)
		self.assertEqual(self.producto.stock, 0)

	def test_decrementar_stock_cant_cero(self):
		self.producto.stock = 10
		self.producto.decrementar_stock(0)
		self.assertEqual(self.producto.stock, 10)

	def test_decrementar_stock_cant_negativa(self):
		self.producto.stock = 10
		with self.assertRaises(AssertionError):
			self.producto.decrementar_stock(-1)
		self.assertEqual(self.producto.stock, 10)

	def test_decrementar_stock_cant_excesiva(self):
		self.producto.stock = 10
		with self.assertRaises(AssertionError):
			self.producto.decrementar_stock(11)
		self.assertEqual(self.producto.stock, 10)
	
	def test_decrementar_stock_cant_incorrecta(self):
		self.producto.stock = 10
		with self.assertRaises(ValueError):
			self.producto.decrementar_stock('chau')
		self.assertEqual(self.producto.stock, 10)

	def test_aumentar_stock_cant_positiva(self):
		self.producto.stock = 2
		self.producto.aumentar_stock(10)
		self.assertTrue(self.producto.stock == 12)

	def test_aumentar_stock_cant_negativa(self):
		self.producto.stock = 2
		with self.assertRaises(AssertionError):
			self.producto.aumentar_stock(-10)
		self.assertEqual(self.producto.stock, 2)

	def test_aumentar_stock_cant_incorrecta(self):
		self.producto.stock = 2
		with self.assertRaises(ValueError):
			self.producto.aumentar_stock("chau")
		self.assertEqual(self.producto.stock, 2)
	

class TestProduccion(unittest.TestCase):
	
	def setUp(self):
		self.producto = Producto("Autoparte_1")
		self.produccion = Produccion(self.producto, 100)

	def test_produccion_producir(self):
		self.assertEqual(self.produccion.producir(), 100)

	def test_nueva_produccion_cantidad_erronea(self):
		with self.assertRaises(AssertionError):
			Produccion(Producto("Autoparte_1"), -1)
		with self.assertRaises(AssertionError):
			Produccion(Producto("Autoparte_1"), 0)
		with self.assertRaises(AssertionError):
			Produccion(Producto("Autoparte_1"), "chau")

	def test_produccion_aumenta_stock_en_producto(self):
		self.assertTrue(self.producto.stock == 0)
		self.assertTrue(self.produccion.cantidad == 100)
		producido = self.produccion.producir()
		self.assertTrue(self.producto.stock == producido)

# ACLARACION: en los siguientes test, las funciones dentro de Setup son creadas 
# para suplantar a las funciones numpy para generar numeros aleatorios que configurara la ap
class TestDemandas(unittest.TestCase):
	
	def setUp(self):

		def generadorAleatorio(numero):
			return numero
		
		self.funcion = generadorAleatorio
		self.parametros = {'numero':100}

	def test_demanda_aleatoria(self):
		demanda = Demanda(self.funcion, self.parametros)
		cantidad = demanda.aleatoria()
		self.assertTrue(cantidad == 100)

class TestAtencion(unittest.TestCase):
	
	def setUp(self):
		self.funcion = np.random.poisson
		self.parametros = {'lam':12}
		self.producto = Producto('autoparte_1')
		self.atencion = Atencion(self.producto, self.funcion, self.parametros, 720)

	def test_tiempo_atencion(self):
		tiempo = self.atencion.cantidad_atender()
		#self.assertTrue(tiempo > 0)
	
class TestEmpleado(unittest.TestCase):

	def setUp(self):
		self.producto = Producto('Autoparte_1')
		self.atenciones = [
			Atencion(Producto('Autoparte_1'), np.random.poisson, {'lam':12}),
			Atencion(Producto('Autoparte_2'), np.random.poisson, {'lam':12}),
			Atencion(Producto('Autoparte_3'), np.random.poisson, {'lam':12}),
			Atencion(Producto('Autoparte_4'), np.random.poisson, {'lam':12})
		]
		self.empleado = Empleado()

	def test_nuevo_empleado_con_atenciones(self):
		for atencion in self.atenciones:
			self.empleado.agregar_atencion(atencion)
		self.assertTrue(len(self.empleado.atenciones) > 0)
		
	def test_empleado_con_atenciones_repetidas(self):
		self.empleado.agregar_atencion(self.atenciones[0])
		with self.assertRaises(AssertionError):
			self.empleado.agregar_atencion(self.atenciones[0])
		self.assertTrue(len(self.empleado.atenciones) > 0)

	def test_empleado_get_tiempo_total_sin_atenciones(self):
		self.assertTrue(self.empleado.atenciones == [])
		with self.assertRaises(AssertionError):
			self.empleado.cantidad_atender()

	def test_empleado_get_tiempo_total_con_atenciones(self):
		a1, a2 = self.atenciones[:2]
		self.empleado.agregar_atencion(a1)
		self.empleado.agregar_atencion(a2)
		#self.assertTrue(len(self.empleado.atenciones) > 2)
		#self.assertTrue(self.empleado.cantidad_atender() > 4)

class TestProducciones(unittest.TestCase):
	
	def setUp(self):
		self.producto = Producto("Autoparte_1")

	def test_get_produccion(self):
		prod = self.producto
		produccion = Produccion(prod, 100)
		producido = produccion.producir()
		self.assertEqual(prod.stock, producido)

	def test_get_json_producto(self):
		p = self.producto
		result = {p.nombre: p.stock}
		#print result

	def test_produccion_acumulativa(self):
		prod = self.producto
		produccion = Produccion(prod, 10)
		producido = produccion.producir()
		self.assertEqual(prod.stock, producido)
		producido += produccion.producir()
		self.assertEqual(prod.stock, producido)

class TestEstadisticas(unittest.TestCase):

	def setUp(self):
		self.estadisticas = Estadisticas()

	def test_estadisticas(self):
		self.assertTrue(self.estadisticas)
	# INCOMPLETOS !!!!


class TestSimulacion(unittest.TestCase):

	def setUp(self):
		self.simulacion = Simulacion()
		with open('config.json') as json_config:
			self.config = json.load(json_config)
		self.simulacion.configurar(self.config)



	def test_config_simulacion(self):
		# probamos otra simulacion para probar estados
		otra_simulacion = Simulacion()
		self.assertTrue(otra_simulacion.estado == 'nada')
		self.assertTrue(otra_simulacion.configurar(self.config) == 'ok')
		self.assertTrue(otra_simulacion.estado == 'configurado')
		
	def test_cant_empleados(self):		
		#self.assertTrue(self.simulacion.cant_anios == 1)
		self.assertTrue(len(self.simulacion.empleados) == 2)
	
	def test_cant_productos(self):
		self.assertTrue(len(self.simulacion.productos) == 2)

	def test_datos_simulacion(self):
		#self.assertTrue(self.simulacion.cant_anios == 1)
		self.assertTrue(self.simulacion.dias_mes == 30)
		self.assertTrue(self.simulacion.meses_anio == 12)
		self.assertTrue(self.simulacion.horas_trabajo == 12)
		#self.assertTrue(self.simulacion.dias_produccion == 15)
		self.assertTrue(self.simulacion.demanda)
		self.assertTrue(self.simulacion.demanda.funcion)

	def test_estado_iniciar_simulacion(self):
		s = self.simulacion
		self.assertTrue(s.estado == 'configurado' and not s.response)
		self.assertTrue(not s.response)
		s.iniciar()
		self.assertTrue(s.response)
		self.assertTrue(s.estado == 'finalizado' and s.response)
		
	def test_response_simulacion_ok(self):
		# {simulacion: [{anio:1, eventos[{acumulado, dia, stock: {nombre_prod:stock}}]}]}
		self.assertTrue(self.simulacion.estado == 'configurado')
		result = self.simulacion.iniciar()
		self.assertTrue(self.simulacion.estado == 'finalizado')
		self.assertTrue(len(result.keys()) == 1 and result.keys()[0] =='simulacion')
		simulacion = result.get('simulacion')
		self.assertTrue(type(simulacion) == list)
		for s in simulacion:
			claves = s.keys()
			self.assertTrue('anio' in claves and 'eventos' in claves)
			self.assertTrue(type(s['anio']) == int)
			self.assertTrue(type(s['eventos']) == list)
			for evento in s['eventos']:
				claves = evento.keys()
				self.assertTrue('acumulado' in claves and 'stock' in claves and 'dia' in claves)
				self.assertTrue(type(evento['acumulado']) == int)
				self.assertTrue(type(evento['dia']) == str)
				self.assertTrue(type(evento['stock']) == list)
				nombres = map(lambda p: p.nombre,self.simulacion.productos)
				self.assertTrue(len(evento['stock']) == len(self.simulacion.productos))
				for s in evento['stock']:
					self.assertTrue(len(s.keys()) == 1)
					c = s.keys()[0]
					self.assertTrue(c in nombres)
					self.assertTrue(type(s[c]) == int)
	
	def test_set_tiempos_atencion_empl(self):
		s = self.simulacion
		self.assertTrue(s.estado == 'configurado')
		s.set_tiempos_atencion(2, 4)
		params = [{'lam':2}, {'lam':4}]
		parametros_atenciones = [a.parametros for e in s.empleados for a in e.atenciones]
		self.assertTrue(all(map(lambda p: p['lam'] == 360 or p['lam']==180, parametros_atenciones)))
		
	

	def test_response_cant_eventos_anios_iniciar_simulacion(self):
		s = self.simulacion
		s.iniciar()
		#self.assertTrue(len(s.response['anios']) == s.cant_anios)

	def test_response_cant_eventos_iniciar_simulacion(self):
		s = self.simulacion
		s.iniciar()
		cant_eventos = s.dias_mes * s.meses_anio * s.cant_anios
		#self.assertTrue(sum(map(lambda a: len(a), s.response['anios'])) == cant_eventos)

	def test_response_as_result_after_ok_simulacion(self):
		s = self.simulacion
		result = s.iniciar()
		self.assertTrue(result == s.response)

	def test_datos_result(self):
		s = self.simulacion
		result = s.iniciar()


class TestEstadisticas(unittest.TestCase):

	def setUp(self):
		self.estadisticas = Estadisticas()
		self.simulacion = Simulacion()
		with open('config.json') as json_config:
			self.config = json.load(json_config)
		self.simulacion.configurar(self.config)
		self.result = self.simulacion.iniciar()
		d = "{'simulacion': [{'anio':1,'eventos':[{'acumulado': 0, 'dia': '1 - 1', 'demanda':0,'stock': [{u'auto_parte_1': 57}, {u'auto_parte_2': 107}]}]}]}"	
		self.result_simulacion_mock = eval(d)

	def test_estado_simulacion_mock_finalizada_ok(self):
		self.assertTrue(self.simulacion.estado == 'finalizado')

	def test_get_dict_estadisticas_response_simulacion(self):
		dict_estadisticas = Estadisticas().getEstadisticas(self.result)
		self.assertTrue(type(dict_estadisticas) is dict)
		
	def test_response_get_estadisticas_response_simulacion(self):
		dict_estadisticas = Estadisticas().getEstadisticas(self.result)
		datos = dict_estadisticas.keys()
		self.assertTrue('promedios_por_anios' in datos)
		self.assertTrue('promedios_totales' in datos)

	def test_tipos_response_get_estadisticas(self):
		dict_estadisticas = Estadisticas().getEstadisticas(self.result)
		self.assertTrue(type(dict_estadisticas.get('promedios_por_anios')) == list)
		self.assertTrue(type(dict_estadisticas.get('promedios_totales')) == dict)
		
	def test_promedios_por_anio_get_estadisticas(self):
		dict_estadisticas = Estadisticas().getEstadisticas(self.result)
		lista_dicts = dict_estadisticas.get('promedios_por_anios')
		datos = [
			'anio',
			'cant_total_acumulada', 
			'prom_acumulado_por_dia',
			'cant_dias_falta_stock',
			'cant_demandas_sin_atender_por_falta_stock',
			'cant_dias_demoras_empl',
			'cant_demandas_sin_atender_por_demoras_empl'
		]
		esta = True
		for dic_result in lista_dicts:
			claves = dic_result.keys()
			if not all(map(lambda d: d in claves, datos)):
				esta = False
				break
		self.assertTrue(esta)

	def test_response_estadisticas(self):
		dict_estadisticas = self.estadisticas.getEstadisticas(self.result_simulacion_mock)
		self.assertTrue(dict_estadisticas)
		p_anios = dict_estadisticas.get('promedios_por_anios')
		self.assertTrue(len(p_anios) == 1)
		for a in p_anios:
			self.assertTrue(a.get('cant_total_acumulada') == 0)
			self.assertTrue(a.get('prom_acumulado_por_dia') == 0)
			self.assertTrue(a.get('cant_dias_falta_stock') == 0)
			self.assertTrue(a.get('cant_demandas_sin_atender_por_falta_stock') == 0)
			self.assertTrue(a.get('cant_dias_demoras_empl') == 0)
			self.assertTrue(a.get('cant_demandas_sin_atender_por_demoras_empl') == 0)
			
	# hace el mismo de arriba con otro mock
	def test_estadisticas_sin_demora_por_falta_stock(self):
		eventos = [
			{'acumulado': 0, 'stock': [{'auto_parte_1': 0}, {'auto_parte_2': 107}]},
			{'acumulado': 0, 'stock': [{'auto_parte_1': 10}, {'auto_parte_2': 107}]},
			{'acumulado': 10, 'stock': [{'auto_parte_1': 10}, {'auto_parte_2': 107}]},
			{'acumulado': 11, 'stock': [{'auto_parte_1': 10}, {'auto_parte_2': 107}]}
		]
		for e in eventos: self.assertFalse(self.estadisticas.falto_stock(e))		
		
	def test_estadisticas_con_demora_por_falta_stock(self):
		evento = {'acumulado': 1, 'stock': [{'auto_parte_1': 0}, {'auto_parte_2': 107}]}
		self.assertTrue(self.estadisticas.falto_stock(evento))

	def test_estadisticas_con_demora_por_empleado(self):
		evento = {'acumulado': 1, 'stock': [{'auto_parte_1': 1}, {'auto_parte_2': 107}]}
		self.assertTrue(self.estadisticas.demora_empleados(evento))

	def test_estadisticas_sin_demora_por_empleado(self):
		evento = {'acumulado': 1, 'stock': [{'auto_parte_1': 0}, {'auto_parte_2': 107}]}
		self.assertFalse(self.estadisticas.demora_empleados(evento))

	def test_estadisticas(self):
		print "---------!!!!!!!!!!!!!!!!!!!!!!"
		result = Estadisticas().getEstadisticas(self.result)
		print self.result

		print json.dumps(result, indent=4, sort_keys=True)



if __name__ == '__main__':
    unittest.main()