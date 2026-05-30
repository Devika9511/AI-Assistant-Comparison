import pandas as pd

results = []

def add_result(
        model,
        prompt,
        response,
        category):

    results.append({
        "model": model,
        "prompt": prompt,
        "response": response,
        "category": category
    })

def save_results():

    df = pd.DataFrame(results)

    df.to_csv(
        "evaluation/results.csv",
        index=False
    )