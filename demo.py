from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.playground import Playground, serve_playground_app
from load_storage import load_social_media_storage

agent = Agent(
    name='My agent',
    model=Ollama(id='llama3.2:3b'),
    storage=load_social_media_storage(),
    num_history_responses=10,
    add_history_to_messages=True,
)

app = Playground(agents=[agent]).get_app()

if __name__ == '__main__':
    serve_playground_app('demo:app', reload=True)
