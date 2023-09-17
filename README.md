# NLP - Individual Task 2
Develop N-gram Language Model for NLP - Individual Task 2

### How to get the dataset
You can access it straight to the folder data. There is a file named idwiki-corpus.txt that consists of 100 sentences that are ready to use.

### How to tokenize the sentence using Aksara
You can refer to the [repository - ir-nlp-csui/aksara](https://github.com/ir-nlp-csui/aksara/blob/main/docs/source/user_guide/tokenize_text.rst)

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

### References and Supplements
1. [Scele NLP - Semester Gasal 2023/2024](https://scele.cs.ui.ac.id/course/view.php?id=3653)
2. [Aksara](https://github.com/ir-nlp-csui/aksara)
3. [Speech and Language Processing (3rd ed. draft) - N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
