from input_handler import get_user_input
from prompt_builder import build_prompt
from integrator import call_openai_api
from response import parse_response
from scoring import add_scoring_logic
from output_formatter import format_output

def main():
    scenario, goal, constraint = get_user_input()
    prompt = build_prompt(scenario, goal, constraint)
    response_text = call_openai_api(prompt)
    parsed_output = parse_response(response_text)
    scored_output = add_scoring_logic(parsed_output)
    final_output = format_output(scored_output)
    print(final_output)

if __name__ == "__main__":
    main()