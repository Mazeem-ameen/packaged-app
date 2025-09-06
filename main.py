
from dotenv import load_dotenv
from agents import Agent, Runner,AsyncOpenAI, set_default_openai_client,set_tracing_disabled,OpenAIChatCompletionsModel

api_key= "AIzaSyDcIUGrZca3SYpzNWfSS5qSHLsrtUqEZFo"
load_dotenv()

external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key,
)

set_default_openai_client(external_client)

set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)
agent = Agent(
    name="hello_agent",
    instructions="You are a concise assistant that greets the user in a single short sentence.",
    model=model
)

result = Runner.run_sync(agent, "Say hello in one short sentence.")
print(result.final_output)