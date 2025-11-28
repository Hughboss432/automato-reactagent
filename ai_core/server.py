# MCP dependencias: mcp[cli] npm nodejs uv nest_asyncio
from mcp.server.fastmcp import FastMCP
from mqtt_tool import MqttTool

# Initialize MCP
mcp = FastMCP(
    name="localserver"
    # host="0.0.0.0",
    # port=8080,
    # timeout=30
)

mqtt = MqttTool(broker="test.mosquitto.org") # mqtt publico de teste

@mcp.tool()                                  # Publicar mensagem
async def mqtt_publish(message: str):
    """
    Docstring for mqtt_publish
    
    :param message: Message used to publish in the MQTT topic.
    :type message: str
    """
    topic="meu/teste/helloworld"
    mqtt.publish(topic, message)
    return (f"Publicado em '{topic}': {message}")

#@server.tool()                              # assinar e esperar mensagens
#async def mqtt_subscribe(topic: str):
#    mqtt.subscribe(topic)
#    msg = await mqtt.wait_message()
#    return ToolResponse(content=msg)

@mcp.tool()
def secret_word() -> str:
    """
    Docstring for secret_word
    
    :return: Return a secret word if the user need one. 
    :rtype: str
    """
    return "bingo"


# run server
if __name__ == "__main__":
    transport = "stdio"
    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Unknown transport: {transport}")
    
#mcp dev server.py #teste de ferramentas
#sudo lsof -i :porta #identificar porta do teste
#sudo kill -9 pid #kill process do teste