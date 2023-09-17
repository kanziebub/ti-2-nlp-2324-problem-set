import pickle
import numpy as np
from aksara import MultiwordTokenizer

class Preprocess:
  def __init__(self) -> None:
    self.data: list[str] = None
    self.train_data: list[str] = None
    self.test_data: list[str] = None
  
  """
  - Parameter num_of_data merupakan jumlah data yang ingin Anda proses.
  - Anda diberikan keleluasaan sesuai dengan computing power yang Anda miliki.
  - Tidak ada keharusan menggunakan keseluruhan ~400,000 kalimat. Namun, pastikan jumlah kalimat jangan terlalu sedikit.
  """
  def load_data(self) -> list[str]:
    with open('./data/idwiki-corpus.txt', 'r', encoding='utf-8') as f:
      data = f.readlines()
    self.data = data
    return self.data
  
  """
  - Fungsionalitas method di bawah ini adalah melakukan pembersihan kalimat dari simbol newline ('\n').
  - Di samping itu, method diharapkan dapat melakukan trimming whitespace pada awal dan akhir kalimat.
  - Output format yang diharapkan berupa list of strings.
  """
  def split_sentences(self, data: list[str]) -> list[str]:
    # TODO: Implement based on the given description
    pass
  
  """
  - Fungsionalitas method di bawah ini adalah melakukan tokenisasi pada kalimat.
  - Sebelum mengerjakan method ini, pastikan Anda telah melakukan eksplorasi pada dataset.
  - Character/kata pada dataset tidak seluruhnya ascii/latin. Lakukan penanganan/filtering terhadap character/kata non-ascii.
  - Perlu diperhatikan bahwa n-gram merupakan case-sensitive model. Kata "saya" dan "Saya" merupakan dua hal yang berbeda. Silakan Anda tentukan penanganan yang Anda rasa terbaik.
  - Output format yang diharapkan adalah list of lists of strings.
  """
  def tokenize_sentences(self, data: list[str]) -> list[list[str]]:
    # TODO: Implement based on the given description
    pass
  
  def get_tokenized_data(self, data: list[str]) -> list[list[str]]:
    splitted: list[str] = self.split_sentences(data)
    tokenized: list[str] = self.tokenize_sentences(splitted)
    return tokenized
  
  def train_test_split(self, data: list[list[str]]):
    tokenized = self.get_tokenized_data(data)
    np.random.seed(42)
    np.random.shuffle(tokenized)

    total_samples = len(tokenized)
    train_size = int(.8 * total_samples)  # 80% for training
    test_size = int(.2 * total_samples)   # 20% for testing

    self.train_data = tokenized[:train_size]
    self.test_data = tokenized[total_samples - test_size:]
    return self.train_data, self.test_data

  """
  - Fungsionalitas pada method di bawah ini adalah menghitung kemunculan kata di dalam corpus.
  - Output format yang diharapkan berupa dictionary dengan pasangan key berupa kata/token dan value berupa jumlah kemunculan kata/token tsb.
  """
  def word_map(self, data: list[list[str]]) -> dict:
    # TODO: Implement based on the given description
    pass
  
  """
  - Fungsionalitas pada method di bawah ini adalah melakukan filtering terhadap kata yang kemunculannyna di bawah threshold/batasan tertentu.
  - Misalkan Anda menetapkan setiap kata yang kemunculannya di bawah 5 tidak perlu diproses (threshold = 5).
  - Anda diharapkan memanfaatkan fungsionalitas method word_map yang telah diimplementasikan sebelumnya.
  - Expected output berupa kumpulan kata yang kemunculannya di atas atau sama dengan (greater than or equal to) threshold.
  - Output format berupa list of strings.
  """
  def filter_vocab_by_threshold(self, data: list[list[str]], num_threshold: int) -> list[str]:
    # TODO: Implement based on the given description
    pass
  
  """
  - Fungsionalitas pada method ini adalah mengganti kata-kata yang kemunculannya di bawah threshold menjadi simbol <unk>.
  - Simbol <unk> melambangkan kata tersebut merupakan OOV (Out of Vocabulary).
  - Anda diharapkan memahami alur method ini dengan memanfaatkan method preprocess_raw_data.
  - Output format berupa list of lists of strings.
  """
  def handle_oov_with_unk(self, data: list[list[str]], vocab: list[str], unknown_token='<unk>') -> list[list[str]]:
    # TODO: Implement based on the given description
    pass
  
  def preprocess_raw_data(self, train, test, threshold):
    vocab = self.filter_vocab_by_threshold(train, threshold)
    train_handled = self.handle_oov_with_unk(train, vocab)
    test_handled = self.handle_oov_with_unk(test, vocab)
    return vocab, train_handled, test_handled
  
  def save_to_pickle(self, vocab: list[str], train: list[list[str]], dev: list[list[str]], test: list[list[str]]) -> None:
    filename = {'vocab': vocab, 'train': train, 'dev': dev, 'test': test}
    for key, value in filename.items():
      with open(f'./data/idwiki-{key}.pkl', 'wb+') as f:
        pickle.dump(value, f)
  
  def load_from_pickle(self):
    with open('./data/idwiki-vocab.pkl', 'rb') as f:
      vocab = pickle.load(f)
    with open('./data/idwiki-train.pkl', 'rb') as f:
      train = pickle.load(f)
    with open('./data/idwiki-test.pkl', 'rb') as f:
      test = pickle.load(f)
    return vocab, train, test
  
def main():
  preprocess = Preprocess()

  print('Loading data...')
  """
  EXAMPLE:
  - Pada contoh ini digunakan sebanyak 10,000 kalimat.
  - Silakan Anda atur sesuai dengan kebutuhan Anda.
  """
  data = preprocess.load_data()

  print('Splitting data...')
  train, test = preprocess.train_dev_test_split(data)

  """
  EXAMPLE:
  - Pada contoh ini ditetapkan threshold sebesar 3.
  - Artinya setiap kata yang kemunculannya di bawah 3 akan dihilangkan dari koleksi.
  """
  print('Pre-processing data...')
  vocab, train_handled, test_handled = preprocess.preprocess_raw_data(train, test, 3)

  print('Saving data...')
  preprocess.save_to_pickle(vocab, train_handled, test_handled)
  print('Finish!')

if __name__ == "__main__":
  main()
