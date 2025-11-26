import paho.mqtt.client as mqtt
import threading
import asyncio

class MqttTool:
    def __init__(self, broker="localhost", port=1883):
        self.loop = asyncio.get_event_loop()

        self.client = mqtt.Client()
        self.client.on_message = self._on_message
        self.client.connect(broker, port)

        self.client.loop_start()
        self.queue = asyncio.Queue()

    def _on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        asyncio.run_coroutine_threadsafe(
            self.queue.put({"topic": msg.topic, "message": payload}),
            asyncio.get_event_loop()
        )

    def publish(self, topic, message):
        self.client.publish(topic, message)

    def subscribe(self, topic):
        self.client.subscribe(topic)

    async def wait_message(self):
        """Espera a próxima mensagem MQTT e retorna."""
        return await self.queue.get()