import paho.mqtt.client as mqtt
import time
import random

# Configura los tópicos
topics = [
    "ceres/sensor/ambiente/temperatura",
    "ceres/sensor/ambiente/humedad",
    "ceres/sensor/fotoresistencia/estado",
    "ceres/sensor/fotoresistencia",
    "ceres/sensor/planta/humedad-tierra",
    "ceres/tanque/principal/estado",
    "ceres/tanque/auxiliar/estado",
    "ceres/tanque/principal/volumen-total",
    "ceres/tanque/auxiliar/volumen-total",
    "ceres/tanque/principal/volumen-liquido",
    "ceres/tanque/auxiliar/volumen-liquido",
    "ceres/tanque/principal/porcentaje-liquido",
    "ceres/tanque/auxiliar/porcentaje-liquido"
]

# Función para generar datos aleatorios
def generate_random_data():
    return random.randint(0, 100)  # Cambia este rango según tus necesidades

# Configura el cliente MQTT
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)  # Cambia la dirección y el puerto MQTT según tus necesidades

# Bucle para enviar datos aleatorios a los tópicos
while True:
    for topic in topics:
        data = generate_random_data()
        client.publish(topic, str(data))
        print(f"Publicado en {topic}: {data}")
    
    time.sleep(60)  # Espera 60 segundos antes de enviar nuevos datos
