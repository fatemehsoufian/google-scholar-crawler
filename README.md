# google-scholar-crawler
This project was a teamwork with my teammate [@alireza-dehghan-nayeri](https://github.com/alireza-dehghan-nayeri)
## Description
The Google Scholar Crawler is a Python project that utilizes [Selenium](https://www.selenium.dev/) and [Pandas](https://pandas.pydata.org/) to crawl Google Scholar and extract information related to a specific keyword. The project allows users to search for a keyword on Google Scholar and retrieve a list of articles related to that keyword.

### Features

- Dynamic interaction with Google Scholar using Selenium
- Retrieval of article information such as titles, publication dates, and citation counts
- Extraction of personal information of the first author with a Google Scholar page
- Storage of data in structured format using Pandas
- Generation of output reports with author information and article details

### Usage

1. Provide a keyword or topic of interest as input.
2. The crawler will initiate a search on Google Scholar using the provided keyword.
3. Articles related to the keyword will be retrieved, including their titles, publication dates, and citation counts.
4. The first author with a Google Scholar page will be identified for each article.
5. The crawler will navigate to the author's page and extract their personal information such as name, affiliation, research interests, and h-index.
6. The extracted data will be stored in a structured format using Pandas data frames.
7. The final output will be a report or file containing the author's personal information and a list of articles written by the author, including their titles, publication dates, and citation counts.
