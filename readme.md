# N-gram Language Model & Sentence Generator & Compute Perplexity

## This project implements a trigram-based language model using unigrams, bigrams, and trigrams to predict the next word and generate sentences from text data. It is designed to work with Project Gutenberg text files but can be used with any plain text.

## The project includes a pipeline for data ingestion, preprocessing, n-gram generation, and interactive next-word prediction or sentence generation.

# Project Structure

``` word-predictor-and-sentence-generator/
│
├─ main.py                     # Entry point: runs pipeline, interactive interface, and perplexity
├─ gutenberg.txt               # Example text file (Project Gutenberg) for training
│
└─ source/
   ├─ __init__.py             # Marks the folder as a Python package
   ├─ data_ingestion.py       # Reads text files
   ├─ preprocessing.py        # Preprocess text: clean, remove headers/footers, tokenize
   ├─ n_grams.py              # Generate uni/bi/trigrams and frequency counts
   ├─ get_prediction.py       # Functions to predict next word using N-grams
   ├─ sentence_generator.py   # Generate sentences based on n-grams
   ├─ perplexity.py           # Compute perplexity of a sentence
   ├─ pipeline.py             # Full pipeline orchestration
   └─ user_pipeline.py        # Interactive user interface for predictions, sentence generation, perplexity
``` 

# Setup & Installation

## 1. Clone the repository:

```
git clone https://github.com/your-username/word-predictor-and-sentence-generator.git
cd word-predictor-and-sentence-generator
```

## 2. Install Python 3 (if not already installed). Recommended: Python 3.10+
## 3. Create a virtual environment (optional but recommended):

```
python -m venv venv
# Activate environment:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

## 4. Install required packages:
### This project uses only Python standard libraries (collections, re). No extra packages are required.

# How to Run

## 1. Make sure your text file (e.g., gutenberg.txt) is in the project root.
## 2. Run the main script:
```
python main.py
```

## 3. The pipeline will:

### i. Load the text file

### ii. Preprocess and tokenize it

### iii. Build uni/bi/trigrams and frequency counters

### iv. Display example predictions and generated sentences

### v. Start an interactive session where you can:

### vi. Predict the next word

### vii. Generate sentences

### viii. Exit the interface

### ix: Compute perplexity for a book sentence and a random sentence.