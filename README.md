# NflPrediction Crew

Welcome to the NflPrediction Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

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

## Design

Goal: Given the date and teams playing, predict the winning probabilities of NFL games.


### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/nfl_prediction/config/agents.yaml` to define your agents
- Modify `src/nfl_prediction/config/tasks.yaml` to define your tasks
- Modify `src/nfl_prediction/crew.py` to add your own logic, tools and specific args
- Modify `src/nfl_prediction/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the nfl_prediction Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The nfl_prediction Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the NflPrediction Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
