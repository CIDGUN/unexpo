db=DB()
db('Entradas').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Entradas').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Entradas').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Entradas').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Entradas').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Entrada-0').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Entrada-0').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Entrada-0').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Entrada-0').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Entrada-0').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Entrada-0').insertar('index', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'index'}, 
                                   {'Contenido': 'textarea', 'name': 'contenido', 'value': ''},
                                  ]], 
                             {'Entrada-0': 0},
                             '23/8/2017 12:22:40', [])
db('Entradas').insertar('index', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'index'}, 
                                   {'Contenido': 'textarea', 'name': 'contenido', 'value': ''},
                                  ]],
                            {'Entrada': 0}, 
                            '14/10/2017 10:38:35', [])
db.load=False

