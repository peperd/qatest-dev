# Pet Project: Selenium - testing bot https://qatest-dev.indvp.com/
![GitHub all releases](https://img.shields.io/github/downloads/peperd/qatest-dev/total?logo=Github)
![GitHub pull requests](https://img.shields.io/github/issues-pr/peperd/qatest-dev?logo=GIthub)
![GitHub repo size](https://img.shields.io/github/repo-size/peperd/qatest-dev?logo=Github)
![visitors](https://visitor-badge.glitch.me/badge?page_id=https://github.com/peperd/qatest-dev&left_color=green&right_color=red)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/scrapy)
![Selenium](https://img.shields.io/badge/Selenium4.0-webdriver-green?style=plastic&logo=Selenium)
![unittest](https://img.shields.io/badge/unittest-yelloegreen?style=plastic&logo=unittest)
![Black](https://img.shields.io/badge/code_style-black-black)

This bot performs actions of: </br> 
- checks all website pages on presence `Page not found` message on source page and save results to `.txt` file, 
- checks all website pages on presence `Lorem ipsum` message on source page and save results to `.txt` file, 
- checks all website pages on presence `Image not found` message on source page and save results to `.txt` file


## Getting Started

1. Download or clone repository </br> `https://github.com/peperd/qatest-dev.git`
2. Install venv </br> `$ pip install virtualenv`
3. Install selenium </br> `$ pip install -U selenium`
4. Install requests </br> `$ python -m pip install requests`
5. Run `run.py` </br> `$ python3 run.py`
6. run.py will open `https://qatest-dev.indvp.com/` in Chrome browser and run tests
7. As result will be generated `Image_not_found.txt`, `Lorem_text.txt`, `Page_not_found.txt` files
where will be placed all test results


### Prerequisites
1. You need `python 3.7+` to be installed
2. Required environment variables: `export CHROME_DRIVER_PATH="<path to chrome driver>"`

## Built With

![Python](https://img.shields.io/badge/Python-3.9-informational?style=for-the-badge&logo=Python)
![Selenium](https://img.shields.io/badge/Selenium-4.0-green?style=for-the-badge&logo=Selenium)

