from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        if not name:
            name = "World"
        return f"Hello, {name}!"


application = Application(
    [HelloWorldService],
    tns="hello.soap.example",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server("0.0.0.0", 8000, wsgi_app)
    print("Servidor SOAP running on http://0.0.0.0:8000")
    server.serve_forever()
