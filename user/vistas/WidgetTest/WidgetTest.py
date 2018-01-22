from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button

from pyjamas.ui.HTML import HTML
from __pyjamas__ import JS
from pyjamas.Window import alert
class WidgetTest(SimplePanel):
	"""docstring for WidgetTest"""
	def __init__(self):
		SimplePanel.__init__(self)
		def decodificar(cadena):
			return cadena.replace("<%","<").replace("%>",">")
		panel=VerticalPanel()
		header=decodificar("{{=returnHTML(incluir(data,'header'))}}")
		footer=decodificar("{{=returnHTML(incluir(data,'footer'))}}")
		panel.add(HTML(header+footer))
		panel.add(HTML("hola mundo"))
		
		self.add(panel)
		
		


if __name__=="__main__":
	RootPanel().add(WidgetTest())