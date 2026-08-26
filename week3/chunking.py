from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter
)

text = """
 Machine Learning is a branch of Artificial Intelligence.
It allows computers to learn from data.
Deep Learning is a subset of Machine Learning.
RAG combines LLMs with external knowledge.
Vector databases store embeddings.
"""

fixed = CharacterTextSplitter(
    separator="",
    chunk_size=100,
    chunk_overlap=0
)

print("\n==================== FIXED SIZE ===================")

for i, chunk in enumerate(fixed.split_text(text),1):
    print(f"\nchunk {i}:")
    print(chunk)
    print("_______________________")


    # ===============================
# 2. PARAGRAPH CHUNKING
# ===============================

paragraph = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=100,
    chunk_overlap=0
)

print("\n========== PARAGRAPH ==========")

for i, chunk in enumerate(paragraph.split_text(text), 1):
    print(f"\nChunk {i}:")
    print(chunk)
    print("-------------------------")


    # =========================================
# 3. RECURSIVE CHUNKING
# =========================================

recursive = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

print("\n========== RECURSIVE ==========")

for i, chunk in enumerate(recursive.split_text(text), 1):
    print(f"\nChunk {i}:")
    print(chunk)
    print("-------------------------")