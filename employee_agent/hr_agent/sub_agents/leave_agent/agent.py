from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool import StreamableHTTPConnectionParams

# Define the agent
leave_agent = Agent(
    name="leave_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful AI agent who helps with the employee leave and contact details information. When asked about leaves always arrage the records in tabular format. Use the MCP server to fetch the records. When asked about contact details share the email and the contact number",
    description="An agent that helps with employee leave and contact information",
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
               # url="http://127.0.0.1:8080/mcp"
               url="https://mcp-server-810309394641.us-central1.run.app/mcp"
            ),
        )
    ],
)