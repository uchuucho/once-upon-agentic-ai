import logging
from strands import Agent
#TODO: import python_repl, file_write
from strands_tools import python_repl, file_write
#TODO: Enable Strands debug log level
logging.getLogger("strands").setLevel(logging.DEBUG)

# Your magical creation here
arcane_scribe = Agent(
    #tools= #TODO: add the tools
    system_prompt="""You are Kiro the Grey Hat, a wizard who specializes in the ancient art of code magic. 
    When asked to create spells (code), you inscribe them on parchment (files) and then cast them to demonstrate their power.""",
    tools=[python_repl, file_write]
)

response = arcane_scribe("Create a magical scroll that generates the first 10 numbers of the Fibonacci sequence and demonstrate its power!")
print(response)