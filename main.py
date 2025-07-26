from input_handler import get_user_input
from prompt_builder import build_prompt
from integrator import call_openai_api
from response import parse_response
from scoring import add_scoring_logic
from output_formatter import format_output

def generate_report(output):
    """
    Generate a formatted report based on the parsed output data.

    Parameters:
    - output: A dictionary containing diagnosis, strategic actions, and simulation score.
    """
    report = f"""
    **Property Analysis Memo**

    **Property:** £5.25M townhouse, Knightsbridge  
    **Time on Market:** 9 months  
    **Current Status:** No offers, seller resisting price drop  
    **Goal:** Sale in 60 days  
    **Constraint:** Do not go below £4.2M

    **Diagnosis:** {output['diagnosis']}

    **Strategic Actions:**
    """
    
    # Add each strategic action to the report
    for action in output['strategic_actions']:
        report += f"\n- {action}"

    report += f"""
    
    **Forecast:** There's a {output['simulation_score']*100}% probability of offer success.

    **Commentary:** The agent should counsel the seller on market realities and strategic pricing.
    """
    
    # Display the report
    print(report)

    # Save the report to a file
    with open('report.txt', 'w') as file:
        file.write(report)

def main():
    # Gather input from user
    scenario, goal, constraint = get_user_input()
    # Build prompt for the AI model based on input
    prompt = build_prompt(scenario, goal, constraint)
    # Call the OpenAI API with the prompt
    response_text = call_openai_api(prompt)
    # Parse the response from the API
    parsed_output = parse_response(response_text)
    # Apply any scoring logic to the parsed output
    scored_output = add_scoring_logic(parsed_output)
    # Format the final output
    final_output = format_output(scored_output)
    
    # Print the structured JSON output
    print(final_output)

    # Generate and display the analysis report
    generate_report(scored_output)

if __name__ == "__main__":
    # Entry point of the application
    main()