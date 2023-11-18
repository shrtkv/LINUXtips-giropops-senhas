from flask import Flask, jsonify
import redis
import string
import random
import os
from prometheus_client import Counter, start_http_server

app = Flask(__name__)

# Environment variables for Redis configuration
redis_host = os.environ.get('REDIS_HOST', 'redis-service')
redis_port = 6379
redis_password = ""

# Redis client setup
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Prometheus Counter
senha_gerada_counter = Counter('senha_gerada', 'Contador de senhas geradas')

def criar_senha(tamanho=8, incluir_numeros=True, incluir_caracteres_especiais=True):
    """ Generate a random password. """
    caracteres = string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiais:
        caracteres += string.punctuation
    return ''.join(random.choices(caracteres, k=tamanho))

@app.route('/gerar-senha', methods=['GET'])
def gerar_senha():
    """ Generate a password and store it in Redis. """
    senha = criar_senha()
    r.lpush("senhas", senha)
    senha_gerada_counter.inc()
    return jsonify({"senha": senha})

@app.route('/senhas', methods=['GET'])
def listar_senhas():
    """ List the last 10 generated passwords. """
    senhas = r.lrange("senhas", 0, 9)
    return jsonify(senhas)

@app.route('/metrics')
def metrics():
    """ Expose metrics for Prometheus. """
    return generate_latest()

if __name__ == '__main__':
    start_http_server(8088)  # Start Prometheus metrics server
    app.run(debug=False, host='0.0.0.0', port=5000)

