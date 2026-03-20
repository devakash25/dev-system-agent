import platform
import datetime
from google.adk.agents import SequentialAgent, LlmAgent
from google.adk.tools import FunctionTool

def get_system_status():
    """Fetches system facts. Takes no arguments."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    system = platform.system()
    return f"Time: {now}, OS: {system}."

specialist = LlmAgent(
    name="Specialist",
    instruction="IMMEDIATELY call get_system_status(). Do not ask for permission. Do not explain. Just run the tool and pass the raw output to 'raw_data'.",
    tools=[FunctionTool(get_system_status)],
    model="gemini-2.5-flash",
    output_key="raw_data"
)

critic = LlmAgent(
    name="Critic",
    instruction="Review {raw_data}. Create a short report and add the stamp 'DEV-VERIFIED'.",
    model="gemini-2.5-flash"
)

root_agent = SequentialAgent(
    name="DEV_System",
    sub_agents=[specialist, critic]
)
