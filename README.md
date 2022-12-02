# Web-Scrapping
## Agenda:
To Scrap data from a bunch of websites and to do text analysis on the scrapped data.

## Tools used:
- Programming Language - Python
- Text editor - Visual Studio Code

## Libraries Used:
- Pandas
- Selenium (from selenium I have imported the webdriver)
- Beautifulsoup
- os

## Procedures:
1. As a preliminary step I have installed all necessary libraries and imported them.
2. I have read the csv file containing the URL links of websites to be scrapped and stored it in a variable called **data**.
3. The dataframe **data** has two columns **URL ID** and **URL**.
4. I have created a for loop that fetches the **URL** stored in the dataframe  **data** scrap's the data from the website and stores in the text file format.
5. The data to be scrapped are in the **h1** tag and **div** tag under the **class**  **entry-title** and **td-post-content** respectively.
6. I have used **beautifulsoup** library also known as **bs4** for scrapping and I have used the **lxml** parser.





