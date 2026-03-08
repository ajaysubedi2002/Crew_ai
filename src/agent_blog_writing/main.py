import sys
import warnings
import shutil
import os
from agent_blog_writing.crew import AgentBlogWriting
from evaluator_crew.crew import BlogEvaluatorCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def clear_memory():
    paths = [
        "./memory",
        "./.crewai_memory",
        "./db",
    ]
    for path in paths:
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"Cleared memory: {path}")

def run():
    clear_memory()
    
    topic = "Latest updates on Iran vs Israel and America"
    
    # Step 1: Generate blog with writing crew
    print("Generating Blog Post")
    blog_result = AgentBlogWriting().crew().kickoff(
        inputs={"topic": topic}
    )
    
    # Step 2: Evaluate with evaluator crew
    print(" Evaluating Blog Post")
    evaluation_result = BlogEvaluatorCrew().crew().kickoff(
        inputs={"blog_content": str(blog_result)}
    )
    
    print("FINAL RESULTS")
    print("\nBlog Output:", blog_result)
    print("\nEvaluation:", evaluation_result)

if __name__ == "__main__":
    run()


