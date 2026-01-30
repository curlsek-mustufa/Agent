from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
import time

load_dotenv()

web_research_agent = Agent(
    name="Web Research Agent",
    role="Research cybersecurity topics and recent threats",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "Find high-level information about cybersecurity threats.",
        "Mention common attack types.",
        "Mention known sources (names only)."
    ],
    markdown=True,
)

cyber_analyst_agent = Agent(
    name="Cybersecurity Analyst",
    role="Analyze threats and explain defenses",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "Explain attack techniques clearly.",
        "Explain mitigation strategies.",
        "Use bullet points or tables where helpful."
    ],
    markdown=True,
)

cyber_team = Team(
    name="Cybersecurity Team",
    members=[web_research_agent, cyber_analyst_agent],
    instructions=[
        "Combine research and analysis into a single response.",
        "Structure the answer clearly.",
        "Keep explanations beginner friendly."
    ],
)

start_time = time.perf_counter()

cyber_team.print_response(
    "Explain ransomware attacks, how they work, and how organizations defend against them.",
    stream=True
)

end_time = time.perf_counter()

print("\nTotal execution time:")
print(f"{end_time - start_time:.2f} seconds")
