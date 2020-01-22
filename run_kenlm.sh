# Train europarl
mkdir -p data/models/kenlm/europarl
scripts/train.sh data/normalized/europarl.txt data/models/kenlm/europarl

# Train full
mkdir -p data/models/kenlm/full
scripts/train.sh data/merged.txt data/models/kenlm/full
build_binary -T -s data/models/kenlm/full/lm_6.arpa  data/models/kenlm/full/lm_6.bin

# Train character-of-word level
mkdir -p data/models/kenlm/full_char_of_word
scripts/train_char_of_word.sh data/merged_char_of_word.txt data/models/kenlm/full_char_of_word
