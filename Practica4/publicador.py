import redis
import time

# Configuración de Redis
redis_host = 'redis-14318.c1.us-central1-2.gce.redns.redis-cloud.com'
redis_port = 14318  
redis_password = 'l4fB8L2RcXdAsVMmtXS1J5qEvGtSPooV'

# Conexión a Redis
def connect_to_redis():
    try:
        redis_client = redis.StrictRedis(
            host=redis_host, 
            port=redis_port, 
            password=redis_password, 
            decode_responses=True
        )
        # Verificamos la conexión con un ping
        if redis_client.ping():
            print("Conectado a Redis exitosamente.")
        return redis_client
    except redis.ConnectionError as e:
        print(f"Error de conexión: {e}")
        return None

# Publicador
def publisher():
    try:
        redis_client = connect_to_redis()
        if not redis_client:
            return
        
        while True:
            message = input("Introduce un mensaje para publicar (o 'exit' para salir): ")
            if message.lower() == 'exit':
                print("Saliendo del publicador...")
                break
            redis_client.publish('canal_prueba', message)
            print(f"Publicado: {message}")
    
    except Exception as e:
        print(f"Error en el publicador: {e}")

if __name__ == "__main__":
    publisher()
