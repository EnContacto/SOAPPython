# SOAPPython
 Application built in Python using the SOAP architecture. 
 This is a simple application with **SOAP** architecture developed in **Python** using the **Flask**. 
## Features

- **SOAP server**: 
  - Exposes the `say_hello(name: str) -> str` method which returns a greeting. If no name is provided, it returns `Hello, World!`.
- **SOAP client**: 
  - Consumes the SOAP service and displays the responses in the console.

## Prerequisites

Before you begin, make sure you have the following requirements installed:

- **Python 3.8 or higher**.  
  You can download it from [python.org](https://www.python.org/).
- **pip** (Python package manager)
  
## Steps to Download and Run the Project

1. **Clone the Repository**.  
   Clone this repository on your local machine using the command:
   ```bash
   git clone https://github.com/EnContacto/SOAPPython.git
   cd SOAPPython
2. **Using the SOAP Server**.
   Run the server
   Start the SOAP server by running the main file:
   `python server.py`
   You will see a message in the console indicating that the server is running:
3. **Using the SOAP Client**
   Run the client
   In another terminal, run the client file to consume the SOAP service:
   `python client.py`
   This will send two requests to the SOAP service and display the responses in the console. 

## Project Structure.
   The project has the following basic structure:
   ```bash
 📁 project-soap
 ┣ 📄 server.py # SOAP server implementation
 ┣ 📄 client.py # Client consuming the SOAP service
 ┗ 📄 README.md # Documentation of the project
