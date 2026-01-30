from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.anthropic import Claude
from agno.os import AgentOS
from agno.tools import MCPTools

agno_agent = Agent(
    name="Agno Agent",
    model=Claude(id="claude-sonnet-4-5"),
    db=SqliteDb(db_file="agno.db"),
    tools=[MCPTools(url="https://docs.agno.com/mcp")],
    add_history_to_context=True,
    markdown=True,
)

agent_os = AgentOS(agents=[agno_agent])
app = agent_os.get_app()