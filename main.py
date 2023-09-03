import ngram_lm
import build_corpus
import preprocess_data

def main():
  build_corpus.main()
  preprocess_data.main()
  ngram_lm.main()

if __name__ == "__main__":
  main()
