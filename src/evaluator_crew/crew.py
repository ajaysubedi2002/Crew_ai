from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from config import settings

@CrewBase
class BlogEvaluatorCrew():
    """
    Evaluates generated blog posts and revises based on human feedback.
    """

    agents: List[BaseAgent]
    tasks: List[Task]

    def _llm(self) -> LLM:
        return LLM(
            model="ollama/llama3.1:latest",
            base_url=settings.base_url,
        )

    @agent
    def blog_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_evaluator"],
            verbose=True,
            allow_delegation=False,
            llm=self._llm(),
            
        )
    
    @agent
    def blog_reviser(self) -> Agent:
        """Agent that revises the blog based on human feedback."""
        return Agent(
            config=self.agents_config["blog_reviser"],
            verbose=True,
            allow_delegation=False,
            llm=self._llm(),
        )

    @task
    def evaluate_blog(self) -> Task:
        return Task(
            config=self.tasks_config["evaluate_blog"],
            output_file="outputs/evaluation_report.md",            
        )
    
    @task
    def human_review(self) -> Task:
        return Task(
            config=self.tasks_config["human_review"],
            human_input=True,  
        )
    
    @task
    def revise_blog(self) -> Task:
        return Task(
            config=self.tasks_config["revise_blog"],
            output_file="outputs/06_revised_blogpost.md",
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )