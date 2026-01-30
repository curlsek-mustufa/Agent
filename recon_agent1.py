from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team
from dotenv import load_dotenv

load_dotenv()

scope_guard = Agent(
    name="Scope Guard",
    role="Validate legal authorization and scope",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "Verify the target is explicitly authorized.",
        "Reject unknown or unsafe domains.",
        "Enforce bug bounty or ownership assumptions.",
        "Stop execution if scope is unclear."
    ],
)
passive_recon = Agent(
    name="Passive Recon Agent",
    role="Collect public-facing metadata",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "Perform passive reconnaissance only.",
        "Enumerate subdomains from public sources.",
        "Analyze DNS, WHOIS, SSL certificates.",
        "Extract HTTP headers and metadata.",
        "Do not simulate attacks."
    ],
    markdown=True,
)
surface_mapper = Agent(
    name="Surface Mapper",
    role="Map exposed web and application surface",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "Identify public endpoints and paths.",
        "Analyze robots.txt and sitemap.xml.",
        "Detect API presence.",
        "List exposed file types."
    ],
    markdown=True,
)
tech_agent = Agent(
    name="Tech Fingerprinting Agent",
    role="Identify technologies and infrastructure",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "Identify server, frameworks, CMS, CDN, WAF.",
        "Detect language stacks and versions (if public).",
        "Use only observable data."
    ],
    markdown=True,
)
risk_analyst = Agent(
    name="Risk Analyst",
    role="Assess security posture from recon data",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "Identify weak security signals.",
        "Explain why they matter.",
        "Provide defensive remediation steps.",
        "Avoid exploit guidance."
    ],
    markdown=True,
)
recon_team = Team(
    name="Full Recon Team",
    members=[
        scope_guard,
        passive_recon,
        surface_mapper,
        tech_agent,
        risk_analyst
    ],
    instructions=[
        "Execute recon in strict order.",
        "Stop if scope is invalid.",
        "Merge findings into a structured report.",
        "Stay ethical and defensive."
    ],
)
recon_team.print_response(
    "Perform full reconnaissance on http://testphp.vulnweb.com "
    "assuming explicit authorization. Generate a complete recon report.",
    stream=True
)
