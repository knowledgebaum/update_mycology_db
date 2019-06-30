# Update Mycology Database
# Description
The goal of this project is to scrape an old mycology database and output it into  an SQL database.  
# Installation
1. Install virtualenv into your system. Its tempting to start with pyenv, Pipenv or poetry though virtualenv is good.
2. create virtualenv using `virtualenv --python=python3.7 venv`
3. activate your virtualenv. You will need to do this everytime you restart your terminal MacOS or linux `source venv/bin/activate` for windows see the docs
4. install dependencies into virtualenv `pip install -r requirements.txt`

# Usage
Run runner_matchmaker_regex.py to scrape the datafiles.


# Notes
The change that you needed to do is to read the contents of the actual file. Not the name. 
