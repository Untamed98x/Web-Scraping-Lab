Extract information from the given web site
You will extract the data from the below web site: 
In [1]:

#this url contains the data you need to scrape
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
The data you need to scrape is the name of the programming language and average annual salary.
It is a good idea to open the url in your web broswer and study the contents of the web page before you start to scrape.
Import the required libraries
In [5]:

from bs4 import BeautifulSoup
​
Download the webpage at the url
In [6]:

import requests
​
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
​
# Send a GET request to the URL
response = requests.get(url)
​
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the HTML content
    html_content = response.content
    # Print the first 500 characters of the HTML content
    print(html_content[:500].decode('utf-8'))  # Decoding the content from bytes to string
else:
    print("Failed to retrieve the webpage.")
​
<!doctype html>
<html lang="en">
<head>
<title>
Salary survey results of programming languages
</title>
<style>
table, th, td {
  border: 1px solid black;
}
</style>
</head>

<body>
<hr />
<h2>Popular Programming Languages</h2>
<hr />
<p>Finding out which is the best language is a tough task. A programming language is created to solve a specific problem. A language which is good for task A may not be able to properly handle task B. Comparing programming language is never easy. What we can do, ho
Create a soup object
In [7]:

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')
​
# Now you can start extracting information from the parsed HTML
# For example, let's find the title of the webpage
title_tag = soup.title
title_text = title_tag.get_text()
​
print(f"Webpage Title: {title_text}")
Webpage Title: 
Salary survey results of programming languages

Scrape the Language name and annual average salary.
In [9]:

# Find all the rows in the table (skip the header row)
table = soup.find('table')
rows = table.find_all('tr')[1:]
​
# Loop through each row and extract language name and annual average salary
for row in rows:
    columns = row.find_all('td')
    language = columns[1].get_text()
    salary = columns[3].get_text()
    print(f"Language: {language}, Average Salary: {salary}")
Language: Python, Average Salary: $114,383
Language: Java, Average Salary: $101,013
Language: R, Average Salary: $92,037
Language: Javascript, Average Salary: $110,981
Language: Swift, Average Salary: $130,801
Language: C++, Average Salary: $113,865
Language: C#, Average Salary: $88,726
Language: PHP, Average Salary: $84,727
Language: SQL, Average Salary: $84,793
Language: Go, Average Salary: $94,082
Save the scrapped data into a file named popular-languages.csv
In [12]:

import csv
# Create a CSV file and write the data
with open('popular-languages.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write header
    csvwriter.writerow(['Language', 'Average Salary'])
    
    # Loop through each row and extract language name and annual average salary
    for row in rows:
        columns = row.find_all('td')
        language = columns[1].get_text()
        salary = columns[3].get_text()
        
        # Write data to the CSV file
        csvwriter.writerow([language, salary])
​
print("Data saved to 'popular-languages.csv'")
Data saved to 'popular-languages.csv'
In [15]:

df = pd.read_csv('popular-languages.csv')
​
# Display the first few rows of the DataFrame
print(df.head())
     Language Average Salary
0      Python       $114,383
1        Java       $101,013
2           R        $92,037
3  Javascript       $110,981
4       Swift       $130,801
