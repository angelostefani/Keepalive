RESTful service in Python to implement a keepalive mechanism.

Flask application with a single /keepalive route. When this route is invoked via a GET request, the keep_alive() function executes and returns a "Service reachable" response with an HTTP status code of 200, indicating that the service is active and reachable.

To start the service, just run this Python script. Make sure you have Flask installed in your Python environment (pip install Flask).
Once the service is launched, it will be available at http://localhost:5000/keepalive.

You can test the service by making a GET request to http://localhost:5000/keepalive using tools like cURL, Postman, or even a simple web browser. You will see that you will receive the response "Service reachable".
