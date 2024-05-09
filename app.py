from flask import Flask

# Creiamo un'applicazione Flask
app = Flask(__name__)

# Definiamo una route '/keepalive' che risponde alle richieste GET
@app.route('/keepalive', methods=['GET'])
def keep_alive():
    # Quando questa route viene richiamata, questa funzione viene eseguita
    # e restituisce una risposta "Servizio raggiungibile" con codice di stato HTTP 200
    return 'Servizio raggiungibile', 200

# Eseguiamo l'applicazione solo se questo script viene eseguito direttamente
if __name__ == '__main__':
    # Avviamo l'applicazione in modalità debug
    app.run(debug=True)
