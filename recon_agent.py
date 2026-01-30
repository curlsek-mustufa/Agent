from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team
from dotenv import load_dotenv

load_dotenv()

recon_agent = Agent(
    name="Recon Agent",
    role="Perform passive reconnaissance on authorized websites",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "Perform ONLY passive reconnaissance.",
        "Analyze publicly available information.",
        "Identify technologies, headers, DNS, SSL, and metadata.",
        "Do NOT suggest exploitation.",
        "Do NOT simulate attacks.",
        "Assume target is authorized or a bug bounty scope."
    ],
    markdown=True,
)
analysis_agent = Agent(
    name="Security Analyst",
    role="Analyze recon data and suggest defensive improvements",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "Analyze recon findings.",
        "Explain potential security risks (high-level).",
        "Suggest defensive best practices only.",
        "No offensive steps."
    ],
    markdown=True,
)

recon_team = Team(
    name="Recon Team",
    members=[recon_agent, analysis_agent],
    instructions=[
        "Combine recon findings and analysis.",
        "Keep output beginner friendly.",
        "Stay ethical and defensive."
    ],
)

recon_team.print_response(
    "Perform passive reconnaissance on http://testhtml5.vulnweb.com. "
    "Identify public technologies, headers, and security posture.",
    stream=True
)
