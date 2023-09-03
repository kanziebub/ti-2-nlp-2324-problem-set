import sys
import gensim
import os.path
import requests

def download(link: str, file_name: str) -> None:
  with open(file_name, 'wb') as f:
    print(f'Downloading {file_name}')
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None: # no content length header
      f.write(response.content)
    else:
      doc_length = 0
      total_length = int(total_length)
      for data in response.iter_content(chunk_size=4096):
        doc_length += len(data)
        f.write(data)
        done = int(50 * doc_length / total_length)
        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
        sys.stdout.flush()

def get_id_wiki(dump_path: str):
  if not os.path.isfile(dump_path):
    url = 'https://dumps.wikimedia.org/idwiki/latest/idwiki-latest-pages-articles.xml.bz2'
    download(url, dump_path)
  return gensim.corpora.WikiCorpus(dump_path, dictionary={})

def extract_text(extracted_path: str, id_wiki) -> None:
  if os.path.isfile(extracted_path):
    return None
  with open(extracted_path, 'w', encoding='utf-8') as f:
    articleNum: int = 0
    for text in id_wiki.get_texts():
      text = ' '.join(text)
      text = text.encode('utf-8', 'ignore').decode('utf-8')
      f.write(text + '\n')
      articleNum += 1
      if articleNum % 1000 == 0:
        print(str(articleNum), 'articles processed')
    print('total:', str(articleNum))
  return None

def make_data_dir() -> None:
  try:
    os.mkdir('./data')
  except OSError as error:
    print(error)

def main():
  make_data_dir()
  extracted_path: str = './data/idwiki.txt'
  dump_path: str = './data/idwiki-latest-pages-articles.xml.bz2'

  print('Retrieving data...')
  id_wiki = get_id_wiki(dump_path)

  print('Extracting text...')
  extract_text(extracted_path, id_wiki)

  print('Corpus is ready on the folder data...')

# if __name__ == "__main__":
#   main()
