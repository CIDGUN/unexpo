db=DB()
db('Anuncios').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Anuncios').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Anuncios').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Anuncios').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Anuncios').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Anuncios').insertar('Te xamos la bienvenida a nuestro sitio', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'Te xamos la bienvenida a nuestro sitio'}, {'opcion': 0, 'Imagen': 'select', 'value': 45, 'name': 'img'}, {'Contenido': 'textarea', 'name': 'publish', 'value': 'Queso roqueford ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\r\n\t\t\t\t\t\t\t'}]], {'Anuncio': 0}, '22/6/2017 21:45:17', [])