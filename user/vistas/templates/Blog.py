#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>
<html>
'''
try: doc+=str(incluir(data,"head"))
except Exception, e: doc+=str(e)
doc+='''
<body onload="brython(1)">
'''
try: doc+=str(incluir(data,"widget-navbar"))
except Exception, e: doc+=str(e)
doc+='''
<section class="container" style="font-family: sans-serif;">
	<div class="row">
	<div class="col-md-8">
	<h1>'''
try: doc+=str(data["post"][0][0]["value"])
except Exception, e: doc+=str(e)
doc+='''</h1>
	'''
try: doc+=str(data["post"][0][1]["value"])
except Exception, e: doc+=str(e)
doc+='''

	</div>
	<aside class="col-md-4">
	'''
try: doc+=str(incluir(data,"box-sidebar"))
except Exception, e: doc+=str(e)
doc+='''
	</aside>	
	</div>
	
</section>
'''
try: doc+=str(incluir(data,"subfooter"))
except Exception, e: doc+=str(e)
doc+='''
'''
try: doc+=str(incluir(data,"footer"))
except Exception, e: doc+=str(e)
doc+='''

</body>
</html>'''