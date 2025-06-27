from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_ollama import ChatOllama

from graph_logic import create_graph_with_tools
from langchain_core.messages import HumanMessage

async def connect_to_server(user_input):
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],  # Caminho para servidor MCP
    )
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()

                # tools_result = await session.list_tools()
                # print("Available tools:")
                # for tool in tools_result.tools:
                #     print(f"  - {tool.name}: {tool.description}")

                tools = await load_mcp_tools(session)
                model = ChatOllama(model="llama3.2").bind_tools(tools)
                app = create_graph_with_tools(tools)

                result = await app.ainvoke({
                "messages": [HumanMessage(content=user_input)],
                "model": model,
                "tools": tools,
                "session": session
                })
                return result
    except Exception as e:
        print(f"Erro ao conectar com MCP: {e}")
        raise
