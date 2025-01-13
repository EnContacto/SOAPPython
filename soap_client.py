from zeep import Client

WSDL_URL = "http://localhost:8000/?wsdl"

client = Client(WSDL_URL)

response = client.service.say_hello("Bryan")
print("Server response :", response)

response = client.service.say_hello("")
print("Server response:", response)
