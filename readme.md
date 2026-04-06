# N-gram Language Model & Sentence Generator & Compute Perplexity

This project implements a trigram-based language model using unigrams, bigrams, and trigrams for predicting the next word, generating sentences, and computing perplexity on text data. While it is designed to work with Project Gutenberg text files, it can be easily adapted for any plain text corpus.

The project provides a complete pipeline for data ingestion, preprocessing, n-gram generation, and an interactive interface for exploring language modeling tasks.

## The project includes a pipeline for data ingestion, preprocessing, n-gram generation, and interactive next-word prediction or sentence generation.

## Features
- Build unigram, bigram, and trigram models from text.
- Generate next-word predictions based on n-gram probabilities.
- Generate sentences using the trained n-gram models.
- Compute perplexity for individual sentences to evaluate model performance.
- Interactive command-line interface for experimentation and testing.

## Project Structure

```
project-root/
│
├─ main.py                     # Entry point: orchestrates the pipeline and interactive interface
├─ gutenberg.txt               # Example Project Gutenberg text file for training
│
└─ source/
   ├─ __init__.py             # Marks the folder as a Python package
   ├─ data_ingestion.py       # Reads and loads text files
   ├─ preprocessing.py        # Cleans text, removes headers/footers, and tokenizes
   ├─ n_grams.py              # Generates uni/bi/trigrams and frequency counts
   ├─ get_prediction.py       # Functions for next-word prediction
   ├─ sentence_generator.py   # Generates sentences based on n-grams
   ├─ perplexity.py           # Computes perplexity for sentences
   ├─ pipeline.py             # Full pipeline orchestration
   └─ user_pipeline.py        # Interactive interface for predictions, sentence generation, and perplexity
```

## Setup & Installation

### 1. Clone the repository:

```
git clone https://github.com/noumanhafeez/ml-ds-assignment-2
cd word-predictor-and-sentence-generator
```

### 2. Install Python 3 (if not already installed). Recommended: Python 3.10+
### 3. Create a virtual environment (optional but recommended):

```
python -m venv venv
# Activate environment:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 4. Install required packages:
This project uses only Python standard libraries (collections, re). No extra packages are required.

## How to Run

### 1. Make sure your text file (e.g., gutenberg.txt) is in the project root.
### 2. Run the main script:
```
python main.py
```

### 3. The pipeline will:

 i. Load the text file

 ii. Preprocess and tokenize it

 iii. Build uni/bi/trigrams and frequency counters

 iv. Display example predictions and generated sentences

 v. Start an interactive session where you can:

 vi. Predict the next word

 vii. Generate sentences

 viii. Exit the interface

 ix: Compute perplexity for a book sentence and a random sentence.
