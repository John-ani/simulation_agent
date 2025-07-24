def build_prompt(scenario, goal, constraint):
    return (
        f"Scenario: {scenario}\n"
        f"Goal: {goal}\n"
        f"Constraint: {constraint}\n\n"
        "Provide a diagnosis, strategic actions, and a simulation score."
    )