import redis

# Configuración de Redis
redis_host = 'redis-14318.c1.us-central1-2.gce.redns.redis-cloud.com'
redis_port = 14318
redis_password = 'l4fB8L2RcXdAsVMmtXS1J5qEvGtSPooV'

# Conexión a Redis
def connect_to_redis():
    try:
        redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        # Probar la conexión con un ping
        if redis_client.ping():
            print("Conectado a Redis exitosamente")
        return redis_client
    except redis.ConnectionError as e:
        print(f"Error de conexión: {e}")
        return None

# Suscriptor
def subscriber(redis_client):
    try:
        pubsub = redis_client.pubsub()
        pubsub.subscribe('canal_prueba')

        print("Esperando mensajes en el canal 'canal_prueba'...")
        for message in pubsub.listen():
            if message['type'] == 'message':
                print(f"Recibido: {message['data']}")
    except Exception as e:
        print(f"Error durante la suscripción: {e}")

if __name__ == "__main__":
    redis_client = connect_to_redis()
    if redis_client:
        subscriber(redis_client)
    else:
        print("No se pudo conectar a Redis. Verifica tu configuración.")
