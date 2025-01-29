from phi.agent import Agent
from phi.tools.youtube_tools import YouTubeTools
from phi.model.groq import Groq
from dotenv import load_dotenv
import httpx
# Disable SSL verification
httpx_client = httpx.Client(verify=False)

import os
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = groq_api_key

agent = Agent(
    tools=[YouTubeTools()],
    model = Groq(id = "llama-3.3-70b-versatile", http_client=httpx_client),
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
)

agent.print_response("Summarize this video https://www.youtube.com/watch?v=74SnvbQYgx8, also give the name of the channel and instructor in the video", markdown=True)
