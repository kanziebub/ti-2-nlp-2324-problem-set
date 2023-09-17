import math
import preprocess_data
from itertools import chain

class NgramModel:
  def __init__(self, vocab: list[str], train: list[list[str]], test: list[list[str]]) -> None:
    self.vocab = vocab
    self.train = train
    self.test = test
  
  """
  - Fungsionalitas model ini adalah menghasilkan koleksi n-gram model.
  - Seperti 2-gram, artinya di dalam koleksi terdapat pasangan, seperti: '<s> saya', 'saya sedang', 'sedang makan', 'makan nasi', 'nasi kapau'.
  - Expected output berupa dictionary dengan pasangan key berupa n-length token serta value berupa kemunculan n-length token tersebut di dalam corpus.
  - Output format berupa dictionary.
  """
  def generate_n_grams(self, data: list[list[str]], n: int, start_token: str = '<s>', end_token='</s>') -> dict:
    # TODO: Implement based on the given description
    pass
  
  """
  - Fungsionalitas method ini menghitung probabilitas suatu kata given kata/kumpulan kata.
  - Sederhananya, method ini merupakan implementasi dari ekspresi P(w_i|w_1:{i-1}).
  - Perlu diperhatikan bahwa pada parameter terdapat 'laplace_number' yang artinya Anda diharapkan mengimplementasikan add-one (laplace) smoothing.
  - Output format berupa float.
  """
  def count_probability(self, predicted_word: str, given_word: list[str], n_gram_counts, n_plus1_gram_counts, vocabulary_size, laplace_number: float = 1.0) -> float:
    # TODO: Implement based on the given description
    pass
  
  """
  - Silakan Anda menggunakan method ini untuk bermain-main/menguji segala kemungkinan sentence/word generation berdasarkan method count_probability yang telah Anda bangun.
  """
  def probabilities_for_all_vocab(self, given_word: list[str], n_gram_counts, n_plus1_gram_counts, vocabulary, end_token='</s>', unknown_token='<unk>',  laplace_number=1.0):
    given_word = tuple(given_word)
    vocabulary = vocabulary + [end_token, unknown_token]
    vocab_size = len(vocabulary)

    probs = dict()
    for word in vocabulary:
      prob = self.count_probability(word, given_word, n_gram_counts, n_plus1_gram_counts, vocab_size, laplace_number=laplace_number)
      probs[word] = prob
    return probs

  """
  - Fungsionalitas pada method ini adalah untuk mengevaluasi n-gram model Anda menggunakan metrik perplexity.
  """
  def count_perplexity(self, sentence, n_gram_counts, n_plus1_gram_counts, vocab_size, start_token='<s>', end_token = '</s>', laplace_number=1.0):
    # TODO: Implement based on the given description
    pass

def main():
  preprocess = preprocess_data.Preprocess()
  vocab, train, test = preprocess.load_from_pickle()

  model = NgramModel(vocab, train, test)
  flatten_test = list(chain.from_iterable(test))

  """
  EXAMPLE:
  - Silakan berkreasi se-kreatif mungkin menggunakan beragam n-gram model yang Anda inginkan.
  - Anda dibebaskan untuk mengganti/menambah/menghapus contoh kombinasi di bawah ini sesuai dengan kreativitas Anda.
  - Kami sangat menghargai kreativitas Anda terkait Tugas Individu 2 ini.
  """
  unigram_counts = model.generate_n_grams(train, 1)
  bigram_counts = model.generate_n_grams(train, 2)
  trigram_counts = model.generate_n_grams(train, 3)

  perplexity_test_12 = model.count_perplexity(flatten_test, unigram_counts, bigram_counts, len(vocab), laplace_number=1.0)
  print(f"n = 1, Perplexity: {perplexity_test_12:.4f}")

  perplexity_test_23 = model.count_perplexity(flatten_test, bigram_counts, trigram_counts, len(vocab), laplace_number=1.0)
  print(f"n = 2, Perplexity: {perplexity_test_23:.4f}")

  perplexity_test_random = model.count_perplexity(['<s>', 'cagar', 'budaya', 'merupakan', 'aset', 'di', 'indonesia', '</s>'], bigram_counts, trigram_counts, len(vocab), laplace_number=1.0)
  print(f"n = 2, Perplexity: {perplexity_test_random:.4f}")

if __name__ == "__main__":
  main()
