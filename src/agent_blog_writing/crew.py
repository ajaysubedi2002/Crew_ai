# from crewai import Agent, Crew, Process, Task
# from crewai.project import CrewBase, agent, crew, task
# from crewai.agents.agent_builder.base_agent import BaseAgent
# from typing import List
# @CrewBase
# class AgentBlogWriting():
#     """AgentBlogWriting crew"""

#     agents: List[BaseAgent]
#     tasks: List[Task]
#     @agent
#     def outline_creator(self) -> Agent:
#         return Agent(
#             config=self.agents_config['outline_creator'], # type: ignore[index]
#             verbose=True
#         )

#     @agent
#     def content_writer(self) -> Agent:
#         return Agent(
#             config=self.agents_config['content_writer'], # type: ignore[index]
#             verbose=True
#         )

#     @agent
#     def editor_enhancer(self) -> Agent:
#         return Agent(
#             config=self.agents_config['editor_enhancer'], # type: ignore[index]
#             verbose=True
#         )
    
#     @task
#     def create_outline(self) -> Task:
#         return Task(
#             config=self.tasks_config['create_outline'], # type: ignore[index]
            
#         )

#     @task
#     def write_content(self) -> Task:
#         return Task(
#             config=self.tasks_config['write_content'], # type: ignore[index]
#         )

#     @task
#     def finalize_blog(self) -> Task:
#         return Task(
#             config=self.tasks_config['finalize_blog'], # type: ignore[index]
#             output_file='blogpost.md'
#         )

#     @crew
#     def crew(self) -> Crew:
#         """Creates the AgentBlogWriting crew"""
#         return Crew(
#             agents=self.agents, # Automatically created by the @agent decorator
#             tasks=self.tasks, # Automatically created by the @task decorator
#             process=Process.sequential,
#             verbose=True,
#             # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
#         )



from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import TavilySearchTool
from typing import List
from agent_blog_writing.tools.custom_tool import BlogImageGeneratorTool
image_tool = BlogImageGeneratorTool()


@CrewBase
class AgentBlogWriting():
    """Autonomous Blog Writing Crew with Independent Web Search"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Initialize Tavily Tool once
    tavily_tool = TavilySearchTool(max_results=5)

    @agent
    def outline_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["outline_creator"],
            tools=[self.tavily_tool],
            verbose=True
        )

    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["content_writer"],
            tools=[self.tavily_tool],
            verbose=True
        )

    @agent
    def editor_enhancer(self) -> Agent:
        return Agent(
            config=self.agents_config["editor_enhancer"],
            tools=[self.tavily_tool],
            verbose=True
        )       

        
    @agent
    def image_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["image_generator"],
            tools=[image_tool],
            verbose=True
        )
    
    @task
    def create_outline(self) -> Task:
        return Task(config=self.tasks_config["create_outline"])

    @task
    def write_content(self) -> Task:
        return Task(config=self.tasks_config["write_content"])

    @task
    def finalize_blog(self) -> Task:
        return Task(
            config=self.tasks_config["finalize_blog"],
            output_file="before_image_blogpost.md"
        )
    
    @task 
    def generate_images_and_embed(self) -> Task:
        return Task(
            config=self.tasks_config["generate_images_and_embed"],
            output_file="blogpost.md"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )