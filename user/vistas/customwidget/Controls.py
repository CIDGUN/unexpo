from pyjamas import DOM
from pyjamas.ui.FocusWidget import FocusWidget
from pyjamas.Window import alert
class VerticalDemoSlider(FocusWidget):
	def __init__(self,min_value, max_value,start_value=None):
		#creo un div
		element=DOM.createDiv()
		FocusWidget.__init__(self,element)
		self.min_value=min_value
		self.max_value=max_value
		if start_value is None:
			start_value=min_value
		self.value=start_value
		self.valuechange_listeners=[]
		DOM.setStyleAttribute(element,"position","relative")
		DOM.setStyleAttribute(element,"overflow","hidden")
		#creo un div
		self.handle=DOM.createDiv()
		#agrego el div dentro del otro
		DOM.appendChild(element,self.handle)

		DOM.setStyleAttribute(self.handle,"border","1px")
		DOM.setStyleAttribute(self.handle,"width","	100%")
		DOM.setStyleAttribute(self.handle,"height","10px")
		DOM.setStyleAttribute(self.handle,"backgroundColor","#808080")
		self.addClickListener(self)


	def onClick(self,sender,event):
		# work out the relative position of cursor 
		alert(event)
		alert(sender)
		mouse_y = DOM.eventGetClientY(event) - \
				  DOM.getAbsoluteTop(sender.getElement())

		self.moveSlider(mouse_y)


	def moveSlider(self,mouse_y):
		relative_y=mouse_y-DOM.getAbsoluteTop(self.getElement())
		widget_height=self.getOffsetHeight()
		#limit the position to be in the widget!
		if relative_y <0:
			relative_y=0
		height_range=widget_height - 10 # handle height is hard-coded
		if relative_y >= height_range:
			relative_y=height_range
		#move the handle
		DOM.setStyleAttribute(self.handle,"top","%dpx" % relative_y)
		DOM.setStyleAttribute(self.handle,"position","absolute")
		val_diff=self.max_value - self.min_value
		new_value= ((val_diff*relative_y)/height_range)+self.min_value
		self.setValue(new_value)

	def setValue(self,new_value):
		old_value=self.value
		self.value=new_value
		for listener in self.valuechange_listeners:
			listener.onControlValueChanged(self,old_value,new_value)

	def addControlValueListener(self,listener):
		self.valuechange_listeners.append(listener)
	def removeControlValueListener(self,listener):
		self.valuechange_listeners.remove(listener)



