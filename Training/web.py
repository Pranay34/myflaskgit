import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return """
   <h1>IAm Pondala Pranay</h1>
   <p>This is my first dockerized web application</p>
   """

if __name__ == '__main__':
	app.run(host=socket.gethostname(),port=5000)