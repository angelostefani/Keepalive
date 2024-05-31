#14/05/2024 - angelo.stefani@enea.it
#RESTful service in Python to implement a keepalive mechanism.
#Flask application with a single /keepalive route. When this route is invoked via a GET request, the keep_alive() function executes and returns a "Service reachable" response with an HTTP status code of 200, indicating that the service is active and reachable.
#To start the service, just run this Python script. Make sure you have Flask installed in your Python environment (pip install Flask). Once the service is launched, it will be available at http://localhost:5000/keepalive.
#You can test the service by making a GET request to http://localhost:5000/keepalive using tools like cURL, Postman, or even a simple web browser. You will see that you will receive the response "Service reachable".

from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route '/keepalive' that responds to GET requests
@app.route('/keepalive', methods=['GET'])
def keep_alive():
    # When this route is called, this function is executed
    # and returns a response "Service reachable" with HTTP status code 200
    return 'Service reachable', 200

# Run the application only if this script is executed directly
if __name__ == '__main__':
    # Start the Flask application in debug mode
    app.run(debug=True)
