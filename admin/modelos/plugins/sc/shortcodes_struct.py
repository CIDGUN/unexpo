db=DB()
#============================================
#TABLA de opciones
db("Opciones").campo("Nombre",db.str)
db("Opciones").campo("Valores",db.list)
db("Opciones").insertar("Becas",["Empresarial","Política","Preparaduria","Trabajo"])
#=============================================
db("Plantillas").campo("Nombre",db.str)
db("Plantillas").campo("Contenido",db.list)
db("Plantillas").campo("args",db.dict)
db("Plantillas").campo("Fecha",db.str)
db("Plantillas").campo("Status",db.list)
#============================================
db("Shortcodes").campo("Nombre",db.str)
db("Shortcodes").campo("Contenido",db.list)
db("Shortcodes").campo("args",db.dict)
db("Shortcodes").campo("Fecha",db.str)
db("Shortcodes").campo("Status",db.list)
#--------------------------------------------
db('Plantillas').insertar('Shortcodes', [[{'Nombre': 'titulo', 'name': 'titulo', 'value': 'sc-'}, {'ext': 'py', 'Controlador': 'textarea-code', 'name': 'controlador', 'value': """
from modulos.Plugin import Shortcode

from config import config

class shortcode(Shortcode):
	def __init__(self,plugin,contendor=False):
		Shortcode.__init__(self,plugin,contendor)
		

		
	def run(self,atts,content):
		return 'hola soy tu Shortcode'

	"""}, {'ext': 'html', 'Dise\xc3\xb1o': 'textarea-code', 'name': 'layout', 'value': '<div></div>'}]], {'Plantilla': 0}, '1/12/2017 10:6:39', [])

#--------------------------------------------
db("Shortcodes").insertar("sc-galeria",[
	[{"Nombre":"titulo","name":"titulo","value":"sc-galeria"},
	 {"Controlador":"textarea-code","name":"controlador","value":"","ext":"py"},
	 {"Diseño":"textarea-code","name":"layout","value":"","ext":"html"},
	],
	
	],
	{"Shortcode":0},
	zu.DateTime(),
	[]
	)
