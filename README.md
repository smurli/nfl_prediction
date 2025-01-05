# NFL Prediction Agent

Welcome to the NFL Prediction project, powered by [crewAI](https://crewai.com).

## Installation

Ensure miniconda is installed on your system. If not, you can download it [here](https://docs.conda.io/en/latest/miniconda.html).

Create a new conda environment and activate it:

```bash
cd <git-path>/nfl_prediction
conda env create
conda activate nfl_prediction
```

Install crewai dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```


## Running the Project
Create .env file with the following keys:
- MODEL, Example MODEL="gpt-4o-mini"
- OPENAI_API_KEY (or respective API keys for the model)
- SERPAPI_API_KEY
- SERPER_API_KEY

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the nfl_prediction Crew, assembling the agents and assigning them tasks as defined in your configuration.

Output from this AI Agent will be created in `outputs/report.md` file.

# Design

## Goal
Calculate the winning probability between {team1} vs {team2} for the upcoming game on {date}.

## Output
Probable winning team: <team>  
Willing Probability: <probability %>  
Rationale:
- reason1
- reason2
- etc

## Agents
- nfl_expert: Expert NFL Odds Compiler
- nfl_research_agent: NFL Analytics Researcher

## Tools
- Goolge Search API
- Web Scraper
- Website Search Tool

## CrewAI Parameters
- Use Manager LLM and hierarchical process for more structured data analysis
- Use memory to reduce context size and online learning
