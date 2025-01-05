#!/usr/bin/env python
import sys
import warnings

from nfl_prediction.crew import NflPrediction

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
warnings.filterwarnings("ignore")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """

    # Get Team1 name as input from user, deafult it to Jets
    team1 = input("Enter Team1 name(default Jets): ") or "Jets"

    # Get Team2 name as input from user, deafult it to Jaguars
    team2 = input("Enter Team2 name(default Jagars): ") or "Jaguars"

    # Get the match date as input from user, default it to 15 Jan
    match_date = input("Enter Match Date(default 15 Jan): ") or "15 Jan"

    inputs = {
        "team1": team1,
        "team2": team2,
        "date": match_date,
    }

    print("Running the crew with the following inputs: ", inputs)
    NflPrediction().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        NflPrediction().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        NflPrediction().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        NflPrediction().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
