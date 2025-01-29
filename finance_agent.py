
from phi.agent.agent import Agent
# from phi.utils import identity
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import httpx

# Disable SSL verification
httpx_client = httpx.Client(verify=False)

import os
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = groq_api_key

# web search agent: 
web_search_agent = Agent(
    name = "web search agent",
    model = Groq(id = "llama-3.3-70b-versatile",http_client=httpx_client),
    tools = [DuckDuckGo()],
    instructions= ["always include the sources"],
    show_tool_calls=True,
    markdown=True
)
# financial agent: 
finance_agent = Agent(
    name = "finance agent",
    model = Groq(id = "llama-3.3-70b-versatile", http_client=httpx_client),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    show_tool_calls = True, 
    markdown = True
)

# multi agent:
multi_ai_agent = Agent(
    model = Groq(id = "llama-3.3-70b-versatile", http_client=httpx_client),
    team = [web_search_agent],
    instructions=["Use the web search agent to find information about the company  and the finance agent to find information about the stock price, analyst recommendations, and stock fundamentals."],
    show_tool_calls=True,
    markdown=True,
)

# initiate the multi agent
multi_ai_agent.print_response("Share the NVDA stock price and analyst recommendations", markdown=True)
