from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task,write_task


##forming the Crew
crew = Crew(
    agents = [blog_researcher, blog_writer],
    tasks = [research_task, write_task],
    process = Process.sequential,
    memory=True,
    max_rpm = 100,
    cache = True,
    share_crew=True
)



##Task Execution process with enhanced feedback
result = crew.kickoff(inputs = {'topic':'first time travel guide to london'})
print(result)