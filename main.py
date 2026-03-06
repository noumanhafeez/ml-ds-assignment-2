# main.py

from source.pipeline import run_pipeline
from source.user_pipeline import user_interaction  # import from the new file

if __name__ == "__main__":
    file_path = 'gutenberg.txt'

    # Run the full NLP pipeline
    run_pipeline(file_path)

    # Start user interaction
    user_interaction()