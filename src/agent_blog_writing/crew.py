# from crewai import Agent, Crew, Process, Task
# from crewai.project import CrewBase, agent, crew, task
# from crewai.agents.agent_builder.base_agent import BaseAgent
# from crewai_tools import TavilySearchTool
# from typing import List
# from agent_blog_writing.tools.custom_tool import BlogImageGeneratorTool
# image_tool = BlogImageGeneratorTool()


# @CrewBase
# class AgentBlogWriting():
#     """Autonomous Blog Writing Crew with Independent Web Search"""

#     agents: List[BaseAgent]
#     tasks: List[Task]

#     # Initialize Tavily Tool once
#     tavily_tool = TavilySearchTool(max_results=5)

#     @agent
#     def outline_creator(self) -> Agent:
#         return Agent(
#             config=self.agents_config["outline_creator"],
#             tools=[self.tavily_tool],
#             verbose=True,            
#             memory = True
#         )

#     @agent
#     def content_writer(self) -> Agent:
#         return Agent(
#             config=self.agents_config["content_writer"],
#             tools=[self.tavily_tool],
#             verbose=True,
#             memory=True
#         )

#     @agent
#     def editor_enhancer(self) -> Agent:
#         return Agent(
#             config=self.agents_config["editor_enhancer"],
#             tools=[self.tavily_tool],
#             verbose=True,
#             memory=True
#         )       

        
#     @agent
#     def image_generator(self) -> Agent:
#         return Agent(
#             config=self.agents_config["image_generator"],
#             tools=[image_tool],
#             verbose=True,
#             memory=True
#         )
    
#     @task
#     def create_outline(self) -> Task:
#         return Task(config=self.tasks_config["create_outline"])

#     @task
#     def write_content(self) -> Task:
#         return Task(config=self.tasks_config["write_content"])

#     @task
#     def finalize_blog(self) -> Task:
#         return Task(
#             config=self.tasks_config["finalize_blog"],
#             output_file="before_image_blogpost.md"
#         )
    
#     @task 
#     def generate_images_and_embed(self) -> Task:
#         return Task(
#             config=self.tasks_config["generate_images_and_embed"],
#             output_file="blogpost.md"
#         )

#     @crew
#     def crew(self) -> Crew:
#         return Crew(
#             agents=self.agents,
#             tasks=self.tasks,
#             process=Process.sequential,
#             verbose=True,
#         )



# from crewai import LLM, Agent, Crew, Process, Task
# from crewai.project import CrewBase, agent, crew, task
# from crewai.agents.agent_builder.base_agent import BaseAgent
# from crewai_tools import TavilySearchTool
# from typing import List
# from agent_blog_writing.tools.custom_tool import BlogImageGeneratorTool
# from crewai import LLM 



# @CrewBase
# class AgentBlogWriting():
#     """
#     Autonomous High-Quality Blog Writing Crew
#     Includes:
#     - SEO Outline Creation
#     - Long-form Content Writing
#     - Fact Verification
#     - Editorial Enhancement
#     - Strategic Image Generation
#     """

#     agents: List[BaseAgent]
#     tasks: List[Task]

#     # Initialize shared tools
#     tavily_tool = TavilySearchTool(max_results=5)
#     image_tool = BlogImageGeneratorTool()
    
    
#     def get_ollama_llm(self):
#         return LLM(
#             model="ollama/llama3.1:latest",  
#             base_url="http://localhost:11434",
#         )

#     @agent
#     def orchestrator(self) -> Agent:
#         return Agent(
#             config=self.agents_config["orchestrator"],
#             verbose=True,
#             allow_delegation=True,
#             llm = self.get_ollama_llm()
#         )

#     @agent
#     def outline_creator(self) -> Agent:
#         return Agent(
#             config=self.agents_config["outline_creator"],
#             tools=[self.tavily_tool],
#             verbose=True,
#             llm = self.get_ollama_llm()
#         )

#     @agent
#     def content_writer(self) -> Agent:
#         return Agent(
#             config=self.agents_config["content_writer"],
#             tools=[self.tavily_tool],
#             verbose=True,
#             llm = self.get_ollama_llm()
            
#         )

#     @agent
#     def fact_verifier(self) -> Agent:
#         return Agent(
#             config=self.agents_config["fact_verifier"],
#             tools=[self.tavily_tool],
#             verbose=True,
#             llm = self.get_ollama_llm() 
#         )

#     @agent
#     def editor_enhancer(self) -> Agent:
#         return Agent(
#             config=self.agents_config["editor_enhancer"],
#             tools=[self.tavily_tool],
#             verbose=True,
#             llm = self.get_ollama_llm()
#         )

#     @agent
#     def image_generator(self) -> Agent:
#         return Agent(
#             config=self.agents_config["image_generator"],
#             tools=[self.image_tool],
#             verbose=True,
#             llm = self.get_ollama_llm()
#         )

#     @task
#     def create_outline(self) -> Task:
#         return Task(
#             config=self.tasks_config["create_outline"]
#         )

#     @task
#     def write_content(self) -> Task:
#         return Task(
#             config=self.tasks_config["write_content"]
#         )

#     @task
#     def verify_facts(self) -> Task:
#         return Task(
#             config=self.tasks_config["verify_facts"]
#         )

#     @task
#     def finalize_blog(self) -> Task:
#         return Task(
#             config=self.tasks_config["finalize_blog"],
#             output_file="before_image_blogpost.md"
#         )

#     @task
#     def generate_images_and_embed(self) -> Task:
#         return Task(
#             config=self.tasks_config["generate_images_and_embed"],
#             context=[self.finalize_blog()],
#             output_file="blogpost.md"
#         )

#     @crew
#     def crew(self) -> Crew:
#         ollama_embedder = {
#             "provider": "ollama",
#             "config": {
#                 "model": "mxbai-embed-large:latest", 
#                 "base_url": "http://localhost:11434"
#             }
#         }
#         return Crew(
#             agents=self.agents,
#             tasks=self.tasks,
#             process=Process.sequential,
#             memory=True,
#             verbose=True,
#             embedder=ollama_embedder,
#         )



from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import TavilySearchTool
from typing import List
from agent_blog_writing.tools.custom_tool import BlogImageGeneratorTool
from models.image_decision import ImageDecision

@CrewBase
class AgentBlogWriting():
    """
    Autonomous High-Quality Blog Writing Crew
    Pipeline:
      orchestrate → create_outline → write_content →
      verify_facts → finalize_blog → generate_images_and_embed
    """

    agents: List[BaseAgent]
    tasks: List[Task]

    tavily_tool = TavilySearchTool(max_results=5)
    image_tool  = BlogImageGeneratorTool()

    def _llm(self) -> LLM:
        """Standard LLM for research/writing agents."""
        return LLM(
            model="ollama/llama3.1:latest",
            base_url="http://localhost:11434",
        )


    @agent
    def orchestrator(self) -> Agent:
        """
        Coordinates the pipeline and validates topic requirements.
        Delegates to specialist agents via sequential process.
        """
        return Agent(
            config=self.agents_config["orchestrator"],
            tools=[self.tavily_tool],   # needs search to assess topic scope
            verbose=True,
            allow_delegation=True,
            max_iter=2,            
            llm=self._llm(),
        )

    @agent
    def outline_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["outline_creator"],
            tools=[self.tavily_tool],
            verbose=True,
            allow_delegation=False,
            max_iter=2,
            llm=self._llm(),
        )

    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["content_writer"],
            tools=[self.tavily_tool],
            verbose=True,
            allow_delegation=False,
            max_iter=2,
            llm=self._llm(),
        )


    @agent
    def editor_enhancer(self) -> Agent:
        return Agent(
            config=self.agents_config["editor_enhancer"],
            tools=[self.tavily_tool],
            verbose=True,
            allow_delegation=False,
            max_iter=2,
            llm=self._llm(),
        )
    
    
    @agent
    def image_decider(self):
        return Agent(
            config=self.agents_config["image_decider"],
            llm=self._llm()
        )
  


    @agent
    def image_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["image_generator"],
            tools=[self.image_tool],    # ONLY the custom image tool
            verbose=True,
            max_iter=3,
            allow_delegation=False,     # must NOT delegate — strict image budget
            llm=self._llm(),
        )

    @task
    def orchestrate(self) -> Task:
        """
        First task: orchestrator analyses the topic, decides research needs,
        and produces a structured creative brief for downstream agents.
        """
        return Task(
            config=self.tasks_config["orchestrate"],
            output_file="outputs/00_brief.md",
        )

    @task
    def create_outline(self) -> Task:
        return Task(
            config=self.tasks_config["create_outline"],
            output_file="outputs/01_outline.md",
        )

    @task
    def write_content(self) -> Task:
        return Task(
            config=self.tasks_config["write_content"],
            output_file="outputs/02_draft.md",
        )


    @task
    def finalize_blog(self) -> Task:
        return Task(
            config=self.tasks_config["finalize_blog"],
            output_file="outputs/04_before_images.md",
        )
        
    @task
    def decide_images(self) -> Task:
        return Task(
            config=self.tasks_config["decide_images"],
            output_pydantic=ImageDecision
        )
    

    @task
    def generate_images_and_embed(self) -> Task:
        return Task(
            config=self.tasks_config["generate_images_and_embed"],
            output_file="outputs/05_blogpost.md",
            condition=lambda context: context["decide_images"].generate_images
        )


    @crew
    def crew(self) -> Crew:
        ollama_embedder = {
            "provider": "ollama",
            "config": {
                "model": "mxbai-embed-large:latest",
                "base_url": "http://localhost:11434",
            },
        }
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            # memory=True,
            verbose=True,
            embedder=ollama_embedder,
        )