doc+='''<!doctype html>
<html lang="es">
<head>
 
 <meta charset="utf-8">
 <link rel="stylesheet" type="text/css" href="'''
try: doc+=str(data['base_url'])
except Exception, e: doc+=str(e)
doc+='''static/css/color.css">

 <link rel="stylesheet" href="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/css/swiper.min.css">
 <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/jquery-3.1.0.js"></script>

 <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/brython/brython.js"></script>
 <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/brython/brython_stdlib.js"></script>
 
 <link rel="icon" type="image/png" href="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/imgs/Logo.jpg" />
 <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
 
 <link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/css/ff.css">
 <link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/css/bootstrap.css">
 <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/swiper.min.js"></script>

<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/bootstrap.js"></script>
<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/bootstrap/tooltip.js"></script>

 <style type="text/css">

    html, body {
        position: relative;
        height: 100%;
    }
    body {
        background: #eee;
        font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
        font-size: 14px;
        color:#000;
        margin: 0;
        padding: 0;
    }
    .swiper-container {
        width: 100%;
        height: 100%;
    }
    .swiper-slide {
        text-align: center;
        font-size: 18px;
        background: #fff;

        /* Center slide text vertically */
        display: -webkit-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;
        -webkit-box-pack: center;
        -ms-flex-pack: center;
        -webkit-justify-content: center;
        justify-content: center;
        -webkit-box-align: center;
        -ms-flex-align: center;
        -webkit-align-items: center;
        align-items: center;
    }
 </style>

</head>
'''