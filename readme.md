# NLP N-gram Prediction and Sentence Generation Pipeline

## Overview
# This project implements a full NLP pipeline for text preprocessing, n-gram modeling, next-word prediction, and sentence generation.
# It supports unigram, bigram, and trigram language models with backoff for missing n-grams.
# Users can interactively predict the next word or generate sentences starting from 0, 1, or 2 words.

## Features
# Preprocess text data by cleaning, lowercasing, removing Project Gutenberg headers/footers, and adding sentence boundary tokens.
# Generate unigrams, bigrams, and trigrams from tokenized text.
# Calculate frequency distributions for uni-, bi-, and trigrams for probabilistic next-word predictions.
# Predict next words using unigram, bigram, and trigram models with maximum likelihood estimation (MLE) and backoff.
# Generate sentences of up to a configurable maximum length using trigram model with backoff.
# Interactive command-line interface for predicting words or generating sentences.

## Installation
# 1. Clone the repository to your local machine.
# 2. Ensure Python 3.8+ is installed.
# 3. Install any dependencies if needed (standard Python libraries used, no external packages required).

## Project Structure
# main.py
# - Entry point of the project.
# - Runs the full pipeline and starts interactive user session.
# source/
# ├── __init__.py
# ├── data_ingestion.py        # Functions to read text files
# ├── preprocessing.py         # Text preprocessing and tokenization
# ├── n_grams.py               # Generate uni-, bi-, and trigrams, and compute frequencies
# ├── get_prediction.py        # Next-word prediction functions and frequency setup
# ├── sentence_generator.py    # Generate sentences using trigram model with backoff
# ├── pipeline.py              # Full pipeline orchestration
# └── user_pipeline.py         # Interactive CLI for user input

## Usage
# 1. Place your text file (e.g., gutenberg.txt) in the project directory.
# 2. Run the main script:
#    ```
#    python main.py
#    ```
# 3. The pipeline will:
#    - Load and preprocess text
#    - Generate n-grams and calculate frequencies
#    - Display example predictions and generated sentences
# 4. In the interactive menu:
#    - Option 1: Predict next word after entering 0, 1, or 2 words.
#    - Option 2: Generate a sentence starting with 0, 1, or 2 words.
#    - Option 3: Exit the interactive session.

## Example Predictions
# Most likely unigram: displays the most frequent single word in the text.
# Next word after 'very': displays predicted next word using bigram model.
# Next word after 'in the': displays predicted next word using trigram model.
# Random sentence: generates a random sentence using trigram model with backoff.
# Sentence starting with 'creep' or 'in the': generates sentences starting with given words.

## Functions
# read_file(path) - Reads text file and returns content as string.
# preprocess(text) - Cleans text, splits into tokens, and adds boundary tokens.
# get_unigram(tokens), get_bigrams(tokens), get_trigrams(tokens) - Generate n-grams.
# get_ngram_frequencies(tokens) - Returns frequency counters for uni-, bi-, and trigrams.
# set_frequencies(uni, bi, tri) - Stores frequencies for prediction.
# predict_next_unigram() - Predict next word using unigram model.
# predict_next_bigram(word) - Predict next word using bigram model with backoff.
# predict_next_trigram(word1, word2) - Predict next word using trigram model with backoff.
# generate_sentence(start_words=None) - Generate sentence using trigram model, starting with optional words.
# user_interaction() - Provides CLI interface for predictions and sentence generation.

## Notes
# The project is designed to handle English text from Project Gutenberg files.
# Sentence generation respects start tokens '<s>' and end tokens '</s>'.
# Backoff ensures that predictions are made even if specific bigrams or trigrams are not found in the text.