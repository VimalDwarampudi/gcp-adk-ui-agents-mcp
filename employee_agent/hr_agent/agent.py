from google.adk.agents import Agent
from .sub_agents.leave_agent.agent import leave_agent
from .sub_agents.policy_agent.agent import leave_policy_agent

# Define the agent
root_agent = Agent(
    name="employee_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are a coordinator. 
    1. If the user asks about personal leave balances , status, employee contact details etc please  DELEGATE to the 'leave_agent'.
    2. If the user asks about company rules, limits, or policy text, DELEGATE to the 'leave_policy_agent'.
    Do not try to use both at the same time.
    """,
    description="An agent that helps with employee leave information",
    sub_agents=[leave_agent, leave_policy_agent]
)