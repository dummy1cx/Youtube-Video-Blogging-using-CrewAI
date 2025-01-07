from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"


llm = "gpt-4-0125-preview"


## Create a senior blog content researcher


blog_researcher = Agent(
    role = 'Blog Researcher from Youtube videos',
    goal = 'get the relevant video content for the topic{topic} from yt channel',
    verbose = True,
    memory = True,
    backstory = (
        "Expert in london and its famous place"
        ),
    tools = [yt_tool],
    llm = llm,
    allow_delegation=True
)


###creating a senior blog writer agent with YT tool

blog_writer = Agent(
    role = 'Blog Writer',
    goal = 'Narrative ceompelling tech stories about the video{topic}from yt Channel',
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner"
    ),
    tools = [yt_tool],
    llm = llm,
    allow_delegation=False
)