### Environment Setup ###
1. [Install python 3.8.1](https://www.python.org/downloads/release/python-381/)
2. [Install poetry](https://python-poetry.org/docs/)
3. [Install pre-commit](https://pre-commit.com/)
4. Run `git clone https://github.com/OscarFMBG/3d-scanning.git <your desired destination>`
5. Run `[python -m] pre-commit install`
6. Run `poetry install` in the directory that you cloned the repository into. 
   (You may need to make sure poetry can find the path to your python version.)
   
### Running Tests ###
`[python -m] pytest`
