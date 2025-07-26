# Simulation-Led Decision Intelligence Platform

This project is a simulation-led decision intelligence platform designed to model pricing, timing, behavioral strategies, and market dynamics in high-value residential real estate scenarios. It harnesses the power of OpenAI's GPT models to provide in-depth analysis and actionable insights.

## Project Structure

simulation_agent/

│
├── main.py # Entry point for the simulation

├── input_handler.py # Handles CLI input gathering and validation

├── prompt_builder.py # Constructs the GPT prompt based on input

├── integrator.py # Interfaces with the OpenAI API

├── response.py # Parses the GPT model response into JSON

├── output.json # stores the structured results of the simulation. 

├── scoring.py # Implements custom scoring logic

├── result.txt # (Output) Memo file created by report_generator

├── output_formatter.py # Formats the final structured output

└── config.py # Manages API key and settings


## How to Run

### Prerequisites

1. **Python:** Ensure Python is installed on your system.
2. **OpenAI API Key:** Obtain your OpenAI API key from [OpenAI](https://platform.openai.com/).

### Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd simulation_agent
Create and Activate a Virtual Environment:

bash
python -m venv env
source env/bin/activate     # On Windows use `.\env\Scripts\activate`

Running the Application
Execute the Program:

bash
python main.py

##***Input Required***

**Property Scenario:** Description of the property.

**Time on Market:** Specify how long the property has been listed. 

**Current Status:** Provide the current market and seller situation.

**Goal:** Objective you want to achieve.

**Constraint:** Any limitations or constraints.




##***Thought Process***

**Objective**

The purpose of this project is to simulate a real estate scenario and provide actionable insights using natural language processing capabilities.

**Design**

Modular Structure:
Each component of the project (input handling, API interaction, response parsing) is modularized into separate scripts. This enhances maintainability and readability.

API Integration:
The integrator.py encapsulates API communication, ensuring seamless interaction with OpenAI's GPT models.

Output and Reporting:
The output is structured in JSON format for easy consumption. A detailed report is also generated to provide qualitative insights.

**Development Workflow**

Input Handling:
Collect user input for the property scenario, goals, and constraints using input_handler.py.

Prompt Generation:
Construct a detailed prompt dynamically using prompt_builder.py to ensure comprehensive API interaction.

Data Processing:
Utilize integrator.py for API calls and response.py to parse responses. Apply scoring.py for custom analysis metrics.

Output Generation:
Leverage output_formatter.py to produce well-structured results, and generate a detailed report.txt for summary and insights.


Bonus: Diagnostic Report
The project includes an optional one-page memo (report.txt) that covers:

Diagnosis: what’s really going wrong

Strategic Actions: 2–3 key recommendations

Forecast: likelihood of success and why

Commentary: insight into agent/seller behavior

**Contributions and Feedback**

Contributions are welcome! Feel free to fork this repository and submit pull requests. For issues or questions, please create an issue in the issue tracker.

**License**

This project is licensed under the MIT License.
