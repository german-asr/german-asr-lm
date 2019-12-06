# Download all corpora
 python scripts/download.py data/download

# Clean all corpora
 python scripts/normalize.py data/download data/normalized

# Merge all corpora
python scripts/merge.py data/normalized data/merged.txt

# Create character-of-word level data
python scripts/to_characters.py data/merged.txt data/merged_char_of_word.txt
