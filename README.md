# kata_word_search
This application will solve a word search puzzle. It will search the puzzle grid and locate each of the words to be found. It will output each word found, along with the grid coordinates of each letter in the word.

The program requires an input.txt file which adheres to the input requirements.

## Input Requirements
- The first line of text will consist of the list of words to be found
- The following lines will consist of a list of single characters, A-Z. 
- All lines in the file except the first will have the same length
- The number of rows will match the number of characters in a line. Thus, the puzzle grid will always be a square.
- All words in the list will always be present in the grid.
- Words may be located horizontally, vertically, diagonally, and both forwards and backwards.
- Words will never "wrap" around the edges of the grid.

## Installing and Running
- Clone the repository at "https://github.com/kevinhamlin/kata_word_search.git"
- In your terminal/shell, navigate to the project's root directory.
- Activate a virtual enviornment (eg, "source ./venv/Scripts/activate").
- Install test requirements:
  - pip install -Ur test_requirements.txt
- Pytest and Mock will be installed in the virtual environment.

- Run the program with app.py

## Running
- After cloning the repository, navigate to the project's root directory and run app.py
  - Depending on your version of python: `python3 app.py` or `python app.py`
  
 ## Built With
 - [PyCharm](https://www.jetbrains.com/pycharm/) - IDE
 - [PyTest](https://docs.pytest.org/en/latest/) - Testing Framework for Python
 - [mock](https://pypi.org/project/mock/0.8.0/) - Testing Library for Python
