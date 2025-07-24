import json

def parse_response(response_text):
    lines = response_text.splitlines()
    diagnosis = lines[0].replace("Diagnosis: ", "")
    strategic_actions = [line.strip() for line in lines[1:4]]
    simulation_score = float(lines[4].replace("Simulation Score: ", ""))
    
    output = {
        "diagnosis": diagnosis,
        "strategic_actions": strategic_actions,
        "simulation_score": simulation_score
    }
    return json.dumps(output, indent=2)