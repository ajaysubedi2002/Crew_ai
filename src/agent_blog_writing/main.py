#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from agent_blog_writing.crew import AgentBlogWriting

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

import shutil
import os
from agent_blog_writing.crew import AgentBlogWriting

def clear_memory():
    paths = [
        "./memory",
        "./.crewai_memory",   # default crewai memory folder
        "./db",               # chroma default
    ]
    for path in paths:
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"Cleared memory: {path}")

def run():
    clear_memory()   # ← wipe before every run
    
    result = AgentBlogWriting().crew().kickoff(
        inputs={"topic": "Latest updates on Iran vs Israel and America"}
    )
    print(result)

if __name__ == "__main__":
    run()


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "Self-driving cars",
#     }
#     try:
#         AgentBlogWriting().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         AgentBlogWriting().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "Self-driving cars",
#     }

#     try:
#         AgentBlogWriting().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")

# def run_with_trigger():
#     """
#     Run the crew with trigger payload.
#     """
#     import json

#     if len(sys.argv) < 2:
#         raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

#     try:
#         trigger_payload = json.loads(sys.argv[1])
#     except json.JSONDecodeError:
#         raise Exception("Invalid JSON payload provided as argument")

#     inputs = {
#         "crewai_trigger_payload": trigger_payload,
#         "topic": "Self-driving cars",
#         "current_year": ""
#     }

#     try:
#         result = AgentBlogWriting().crew().kickoff(inputs=inputs)
#         return result
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew with trigger: {e}")
