import string
import unicodedata

TEXT = """In 2026, we teach “intro-to-AI” with hands-on labs—no hype. Students ask: “Why tokens?”
Because models read pieces, not words. E.g., ‘ChatGPT-5’ ≠ ‘Chat’, ‘GPT’, ‘5’ in all schemes.
We track loss/accuracy, compare char/word/BPE, and test a URL: https://example.org/a/b?c=42.
Café prices rose 3.7%—blame supply-chain weirdness (and ☕ demand)."""

print(TEXT)

#Step 1: lowercase, remove punctuation, split by whitespace.
lowercase_text = TEXT.lower()

cleaned_text = "".join(
    char
    for char in lowercase_text
    if char not in string.punctuation
    and not unicodedata.category(char).startswith("P")
)

word_tokens = cleaned_text.split()

print("Word tokens:", word_tokens)
print("Length after tokenization:", len(word_tokens))

# Verify that the text is lowercase and punctuation was removed.
assert lowercase_text == lowercase_text.lower()
assert not any(
    char in string.punctuation
    or unicodedata.category(char).startswith("P")
    for char in cleaned_text
)
assert word_tokens == cleaned_text.split()
#Step 2: Build a vocabulary
# Get the unique tokens and sort them.
word_vocab = sorted(set(word_tokens))

# Map each token to a numerical ID.
word_to_id = {
    word: index for index, word in enumerate(word_vocab)
}

# Map each numerical ID back to its token.
id_to_word = {
    index: word for word, index in word_to_id.items()
}

print("Vocabulary:", word_vocab)
print("Vocabulary size:", len(word_vocab))
print("Word-to-ID mapping:", word_to_id)

# Verify that every vocabulary token can be converted back correctly.
assert len(word_vocab) == len(set(word_tokens))
assert all(
    id_to_word[word_to_id[word]] == word
    for word in word_vocab
)
#Step 3: Numericalize
# Replace each word token with its vocabulary ID.
word_ids = [word_to_id[word] for word in word_tokens]

print("Token IDs:", word_ids)
print("Number of token IDs:", len(word_ids))

# Check that every token has an ID and every ID is valid.
assert len(word_ids) == len(word_tokens)
assert all(0 <= index < len(word_vocab) for index in word_ids)

#Step 4: Decode
# Replace each numerical ID with its corresponding token.
decoded_tokens = [id_to_word[index] for index in word_ids]

print("Decoded tokens:", decoded_tokens)

# Check that decoding reproduces the original word tokens.
assert decoded_tokens == word_tokens
print("Decoding check passed.")

#Step 5: Rejoin and reconstruct
# Join the decoded tokens with one space between them.
reconstructed_text = " ".join(decoded_tokens)

print("Reconstructed text:", reconstructed_text)
print("Length after tokenization:", len(word_tokens))

# Verify that the reconstructed text matches the processed tokens.
assert reconstructed_text == " ".join(word_tokens)
print("Reconstruction check passed.")

# Display a final summary.
print("\nWORD TOKENIZER SUMMARY")
print("Total tokens:", len(word_tokens))
print("Unique tokens:", len(word_vocab))
print("Decoding matches tokens:", decoded_tokens == word_tokens)
