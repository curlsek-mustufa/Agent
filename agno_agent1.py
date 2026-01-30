from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.os import AgentOS

agno_agent = Agent(
    name="Agno Cybersecurity Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    db=SqliteDb(db_file="agno.db"),
    add_history_to_context=True,
    markdown=True,
)

agent_os = AgentOS(agents=[agno_agent])
app = agent_os.get_app()
