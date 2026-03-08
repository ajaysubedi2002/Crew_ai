from evaluator_crew.crew import BlogEvaluatorCrew

def run_evaluator():
    # Read the final blog from outputs
    with open("outputs/05_blogpost.md", "r", encoding="utf-8") as f:
        blog_content = f.read()
    
    # Run only the evaluator crew
    result = BlogEvaluatorCrew().crew().kickoff(
        inputs={"blog_content": blog_content}
    )
    
    print("Evaluation Result:")
    print(result)

if __name__ == "__main__":
    run_evaluator()