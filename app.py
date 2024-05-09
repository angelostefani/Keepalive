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
