from html.parser import HTMLParser
#Modulo que va a servir para realizar una salida de html
#Se arma una clase orientada a objeto que va a preparar el proceso que luego dara la salida desde el feed.
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)
salida = MyHTMLParser()
salida.feed("<html><head><title>Mi primera pagina web</title></head><body><h1>Primer Titulo</h1></body></html>")

#Es lo más básico en escencia que va a salir cuando quieran incorporar o visualizar contenido html