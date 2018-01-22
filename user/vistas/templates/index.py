doc+='''<!DOCTYPE html>
<html>
'''
try: doc+=str(incluir(data,"head"))
except Exception as e: doc+=str(e)
doc+='''
<body onload="brython(1)">
'''
try: doc+=str(incluir(data,"widget-navbar"))
except Exception as e: doc+=str(e)
doc+='''
'''
#=incluir(data,"nav-bar")
doc+='''
	


<section class="container font-s12" style="font-family: sans-serif;">
	<div class="row">
	<div class="col-md-8">
	<article class="text-justify">
		<h1>Admision</h1>
		<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
		consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
		proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
	</article>
	<hr>
	<article class="text-justify">
		<h2>Graduando</h2>
		<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
		consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
		proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
	</article>

	</div>
	<aside class="col-md-4">
	
	'''
try: doc+=str(incluir(data,"box-sidebar"))
except Exception as e: doc+=str(e)
doc+='''
	</aside>	
	</div>
	
</section>
'''
try: doc+=str(incluir(data,"subfooter"))
except Exception as e: doc+=str(e)
doc+='''
'''
try: doc+=str(incluir(data,"footer"))
except Exception as e: doc+=str(e)
doc+='''

</body>
</html>'''