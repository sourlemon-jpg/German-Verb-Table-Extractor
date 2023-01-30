# German-Verb-Table-Extractor

A python script that scrapes verb conjugation information from websites and saves it to a text file.
### Required Libraries
The following libraries need to be installed to run the script:

    -requests
    -bs4 (BeautifulSoup)
    -tabulate
    -colorama

To install these libraries, run the following command:
> pip install requests bs4 tabulate colorama

### Usage
The script takes a German verb as input and makes a GET request to the website to scrape verb conjugation information. The information is then saved to a text file named "dieFolgen.txt".

To run the script, simply execute the following command in the terminal:
> python germanVerbTable.py

### Output
The script outputs the conjugated form of the verb in two tenses: Präsens and Perfekt. The output is saved to the text file "dieFolgen.txt" and also displayed on the terminal.
