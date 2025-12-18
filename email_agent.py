from dotenv import load_dotenv
load_dotenv()
from crewai import Agent, Task, Crew, LLM

llm = LLM(model="gemini-2.0-flash",
temperature=0.1)


email_assitant = Agent(
    role = "Email Assistant",
    goal = "To assist the user in their email tasks and make email professional and clear",
    llm = llm,
    backstory = "You are an email assistant that helps users with their email tasks",
    verbose = True
)


original_email = "hey team, can you please update me on the project and tell me if some stuff is pending or not"

email_task = Task(
    description=f"Rewrite the following email to be more professional and clear, while maintaining the original request: {original_email}",
    expected_output="A professional and clear version of the original email.",
    agent=email_assitant
)

crew = Crew(
    agents=[email_assitant],
    tasks=[email_task],
    verbose=True
)

result = crew.kickoff()
print(result)

