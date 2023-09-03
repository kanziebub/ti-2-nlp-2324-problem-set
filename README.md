# NLP - Individual Task 2
Develop N-gram Language Model for NLP - Individual Task 2

### How to get the dataset
We offer you two ways to deal with the dataset/corpus
1. You can build it by yourself by running the `build_corpus.py` file.
2. Since building the corpus takes a lot of time, it depends on the processor power and RAM capacity. To save your time, you can download our data here: [Google Drive - idwiki.txt](https://drive.google.com/file/d/1gFQ6Vnb9kJurxFg7-ACsxoI499VhlRFk/view?usp=sharing) then placed it under the `data` folder.

### How to start
```
python -m venv env
source env/Scripts/activate

pip install -r requirements.txt
python main.py
```

### How to debug the python file
Uncomment the conditional statement
```
if __name__ == "__main__":
  main()
```
then run the python file
```
python [filename].py
```

### Reference and Supplement
1. [Scele NLP - Semester Gasal 2023/2024](https://scele.cs.ui.ac.id/course/view.php?id=3653)
2. [Speech and Language Processing (3rd ed. draft) - N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
