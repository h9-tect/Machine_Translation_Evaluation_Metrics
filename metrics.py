import nltk
from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import corpus_bleu
from nltk.translate.meteor_score import meteor_score
from jiwer import wer
from rouge_score import rouge_scorer
import bert_score
from comet import download_model, load_from_checkpoint

def calculate_bleu(candidate, reference):
    # Calculate BLEU score for a single candidate and reference translation
    candidate = word_tokenize(candidate)
    reference = word_tokenize(reference)
    return nltk.translate.bleu_score.sentence_bleu([reference], candidate)

def calculate_meteor(candidate, reference):
    # Calculate METEOR score for a single candidate and reference translation
    return meteor_score(reference, candidate)

def calculate_ter(candidate, reference):
    # Calculate TER score for a single candidate and reference translation
    return wer(reference, candidate)

def calculate_rouge(candidate, reference):
    # Calculate ROUGE scores for a single candidate and reference translation
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, candidate)
    return scores['rouge1'].fmeasure, scores['rougeL'].fmeasure

def calculate_bert_score(candidate, reference):
    # Calculate BERTScore for a single candidate and reference translation
    _, _, f_score = bert_score.score([candidate], [reference])
    return f_score.item()

def evaluate_with_comet(model, data):
    model_output = model.predict(data, batch_size=8, gpus=1)
    return model_output

# Download and load the COMET model
model_path = download_model("Unbabel/wmt22-comet-da")
model = load_from_checkpoint(model_path)
