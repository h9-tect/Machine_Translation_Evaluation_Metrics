import unittest
import pandas as pd
from .metrics import *
from files_reading import *


class TestMTMetrics(unittest.TestCase):

    def test_calculate_bleu(self):
        candidate = "Hello world"
        reference = "Bonjour le monde"
        bleu_score = calculate_bleu(candidate, reference)
        self.assertAlmostEqual(bleu_score, 0.0)  # Add your expected BLEU score here

    def test_calculate_meteor(self):
        candidate = "Hello world"
        reference = "Bonjour le monde"
        meteor_score = calculate_meteor(candidate, reference)
        self.assertAlmostEqual(meteor_score, 0.0)  # Add your expected METEOR score here

    def test_calculate_ter(self):
        candidate = "Hello world"
        reference = "Bonjour le monde"
        ter_score = calculate_ter(candidate, reference)
        self.assertAlmostEqual(ter_score, 1.0)  # Add your expected TER score here

    def test_calculate_rouge(self):
        candidate = "Hello world"
        reference = "Bonjour le monde"
        rouge1, rougeL = calculate_rouge(candidate, reference)
        self.assertAlmostEqual(rouge1, 0.0)  # Add your expected ROUGE-1 score here
        self.assertAlmostEqual(rougeL, 0.0)  # Add your expected ROUGE-L score here

    def test_calculate_bert_score(self):
        candidate = "Hello world"
        reference = "Bonjour le monde"
        bert_score = calculate_bert_score(candidate, reference)
        self.assertAlmostEqual(bert_score, 0.0)  # Add your expected BERTScore here

    def test_read_csv(self):
        file_path = "path/to/your/csv/file.csv"
        data = read_csv(file_path)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertNotEqual(len(data), 0)  # Check if data is successfully loaded

    def test_read_excel(self):
        file_path = "path/to/your/excel/file.xlsx"
        data = read_excel(file_path)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertNotEqual(len(data), 0)  # Check if data is successfully loaded

    def test_evaluate_translation(self):
        data = pd.DataFrame({
            'candidate': ['Hello world', 'I am fine'],
            'reference': ['Bonjour le monde', 'Je vais bien']
        })
        candidate_column = 'candidate'
        reference_column = 'reference'
        evaluated_data = evaluate_translation(data, candidate_column, reference_column)
        self.assertIsInstance(evaluated_data, pd.DataFrame)
        self.assertGreater(len(evaluated_data), 0)  # Check if evaluation scores are added

    # Add more tests for other functions if needed


if __name__ == '__main__':
    unittest.main()
