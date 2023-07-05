import pandas as pd
import os.path
from .metrics import *
def read_csv(file_path):
    # Read a CSV file and return the data as a Pandas DataFrame
    data = pd.read_csv(file_path)
    return data

def read_excel(file_path):
    # Read an Excel file and return the data as a Pandas DataFrame
    data = pd.read_excel(file_path)
    return data

def evaluate_translation(data, candidate_column, reference_column):
    # Evaluate translations in the provided DataFrame using all available evaluation metrics
    evaluation_functions = [
        calculate_bleu,
        calculate_meteor,
        calculate_ter,
        calculate_rouge,
        calculate_bert_score
    ]

    for evaluation_function in evaluation_functions:
        metric_name = evaluation_function.__name__[10:]  # Remove "calculate_" from function name
        data[metric_name] = data.apply(lambda row: evaluation_function(row[candidate_column], row[reference_column]), axis=1)

    return data

# Prompt the user to input the file path
file_path = input("Enter the path to the CSV or Excel file: ")

while not os.path.isfile(file_path):
    print("Invalid file path. Please try again.")
    file_path = input("Enter the path to the CSV or Excel file: ")

data = None
if file_path.endswith('.csv'):
    data = read_csv(file_path)
elif file_path.endswith('.xlsx'):
    data = read_excel(file_path)
else:
    print("Unsupported file format. Please provide a CSV or Excel file.")

if data is not None:
    print("Columns available in the file:")
    print(data.columns)

    candidate_column = input("Enter the column name for the candidate translations: ")
    reference_column = input("Enter the column name for the reference translations: ")

    data = evaluate_translation(data, candidate_column, reference_column)

    print("Evaluation scores:")
    for column in data.columns:
        print(f"{column} scores:")
        for score in data[column]:
            print(score)
