from flask import Flask
import os 

app = Flask(__name__)


@app.route('/factorial/<int:numero>')
def factorial(numero):
    container_id = os.uname()[1] 

    if numero < 0:
        return "El numero ingresado debe ser positivo"
    else:
        result = 1
        for i in range(1, numero + 1):
            result *= i
        return f"{str(result)} - Container Id: {container_id}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
