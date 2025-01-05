from crewai import Agent, Crew, Process, Task, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from chromadb.utils.embedding_functions import GoogleVertexEmbeddingFunction
from langchain_openai import ChatOpenAI
from langchain_google_vertexai import VertexAI
from dotenv import load_dotenv
import os

load_dotenv()


@CrewBase
class NflPrediction:
    """NflPrediction crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    llm = VertexAI(model_name="gemini-1.5-flash-002")

    def get_llm(self):
        if os.getenv("MODEL").startswith("vertex_ai/"):
            return VertexAI(model_name=os.getenv("MODEL").split("/")[1])
        elif os.getenv("MODEL").startswith("gpt"):
            return ChatOpenAI(model_name=os.getenv("MODEL"))

    @agent
    def nfl_expert(self) -> Agent:
        return Agent(
            config=self.agents_config["nfl_expert"],
            allow_delegation=True,
            llm=self.get_llm(),
            verbose=True,
        )

    @agent
    def nfl_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["nfl_research_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            llm=self.get_llm(),
            verbose=True,
        )

    @task
    def nfl_momentum_task(self) -> Task:
        return Task(config=self.tasks_config["nfl_momentum_task"])

    @task
    def nfl_roster_change_task(self) -> Task:
        return Task(config=self.tasks_config["nfl_roster_change_task"])

    @task
    def nfl_task(self) -> Task:
        return Task(config=self.tasks_config["nfl_task"], output_file="report.md")

    @crew
    def crew(self) -> Crew:
        """Creates the NflPrediction crew"""

        manager_llm = self.get_llm()
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            # process=Process.sequential,
            process=Process.hierarchical,
            manager_llm=manager_llm,
            memory=True,
            verbose=True,
        )
