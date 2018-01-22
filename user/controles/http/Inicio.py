
from modulos.controlador import Controlador

from Controladores.http.default import default 

class Inicio(default):
	def __init__(self,data):
		default.__init__(self,data)

		self.vista="index"

		if data["metodo"]==None and data["control"]==None and data["action"]==None:
			self.servir()
		self.modelo=data["model"]["paginas"]
		

	def Administrativo(self):

		self.add_vista("administrativo")
		self.servir()
	def Coordinaciones(self):
		self.add_vista("coordinaciones")
		self.servir()
	def Organizaciones(self):
		self.add_vista("organizaciones")
		self.servir()
	def Instalaciones(self):
		self.add_vista("instalaciones")
		self.servir()
	





		
		