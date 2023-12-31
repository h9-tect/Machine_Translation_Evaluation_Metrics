# Machine Translation Evaluation

This repository contains three files (`__init__.py`, `files_reading.py`, and `metrics.py`) that provide functionality for building an MT (Machine Translation) evaluation task. These files include functions for reading data, evaluating translations using various metrics, and calculating evaluation scores.

## Files

1. `__init__.py`: This file serves as the initialization file for the package. It exports the following functions:

   - `calculate_bleu`: Calculates the BLEU score for a translation.
   - `calculate_meteor`: Calculates the METEOR score for a translation.
   - `calculate_ter`: Calculates the TER (Translation Edit Rate) score for a translation.
   - `calculate_rouge`: Calculates the ROUGE scores (ROUGE-1 F-measure and ROUGE-L F-measure) for a translation.
   - `calculate_bert_score`: Calculates the BERTScore for a translation.
   - `evaluate_with_comet`: Performs evaluation using the COMET model.

2. `files_reading.py`: This file provides functions for reading data from CSV and Excel files. It exports the following functions:

   - `read_csv`: Reads a CSV file and returns the data as a Pandas DataFrame.
   - `read_excel`: Reads an Excel file and returns the data as a Pandas DataFrame.
   - `evaluate_translation`: Evaluates translations in a DataFrame using various metrics.

3. `metrics.py`: This file contains the implementation of different evaluation metrics used for MT evaluation. It exports the following functions:

   - `calculate_bleu`: Calculates the BLEU score for a translation.
   - `calculate_meteor`: Calculates the METEOR score for a translation.
   - `calculate_ter`: Calculates the TER score for a translation.
   - `calculate_rouge`: Calculates the ROUGE scores for a translation.
   - `calculate_bert_score`: Calculates the BERTScore for a translation.
   - `evaluate_with_comet`: Performs evaluation using the COMET model.

## Usage

To use these files for MT evaluation, follow these steps:

1. Ensure that you have the required dependencies installed. You may need to install packages in `requirements.txt`
2. Use the imported functions to read data, evaluate translations, and calculate evaluation scores based on your requirements.
   ```python
   file_path = "path/to/your/data.csv"
   data = read_csv(file_path)
   data = evaluate_translation(data, 'candidate_column', 'reference_column')
   bleu_score = calculate_bleu(data['candidate_column'], data['reference_column'])
   ```
3. Customize the code or add additional functions as needed to suit your specific MT evaluation task

