from agno.agent import Agent
from agno.models.openai import OpenAIChat

# 1. Create the model (ONCE)
model = OpenAIChat(
    id="gpt-4o-mini"
)

# 2. Create the agent
agent = Agent(
    name="CyberSecurity Agent",
    model=model,
    instructions="You are a helpful Cybersecurity assistant."
    )

# 3. Run the agent
response = agent.run("\nExplain Cybersecurity in simple terms. \nAnd how penetration testing is done?")

print(response)
