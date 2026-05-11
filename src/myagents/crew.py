from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool

@CrewBase
class Myagents():
    """Myagents crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            tools=[SerperDevTool()],
            llm="gemini/gemini-2.5-flash",
            verbose=True
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'], # type: ignore[index]
            llm="gemini/gemini-2.5-flash",
            verbose=True
        )

    @agent
    def social_media_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['social_media_manager'], # type: ignore[index]
            llm="gemini/gemini-2.5-flash",
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'], # type: ignore[index]
            context=[self.research_task()]
        )

    @task
    def social_media_task(self) -> Task:
        return Task(
            config=self.tasks_config['social_media_task'], # type: ignore[index]
            context=[self.writing_task()],
            output_file='final_content.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Myagents crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
