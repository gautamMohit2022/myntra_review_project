 Myntra Product Review Scraper & Analyzer
This project helps you scrape customer reviews and ratings for any product listed on Myntra, stores that data in a MongoDB database, and lets you analyze the reviews using a simple and interactive web interface built with Streamlit.

Why I Built This?
When we shop online, we often have to read through tons of reviews to figure out if a product is good. This project solves that by:

Automatically collecting all reviews for any Myntra product

Organizing them neatly into a table

Storing them safely in a database (MongoDB)

Showing the insights (like rating, price, comments) on a clean web app

What This Project Does?
 You enter the product name (like “Nike shoes”)
 It goes to Myntra, collects review data
 Stores the data in MongoDB
 Shows a table of all reviews
 Lets you download or analyze them easily


Tools & Technologies Used?
| Tool / Library    | What it’s used for                    |
| ----------------- | ------------------------------------- |
| **Python**        | Main programming language             |
| **Selenium**      | For automating the browser & scraping |
| **BeautifulSoup** | For reading HTML content              |
| **MongoDB Atlas** | To store all the reviews              |
| **Pandas**        | To manage and analyze review data     |
| **Streamlit**     | For the front-end / UI                |
| **Git & GitHub**  | Version control and code sharing      |


How to Set It Up?
Follow these simple steps to run the project on your own system:

1. Set Up the Environment
conda create -p ./env python=3.10 -y
conda activate ./env

2.Install All Requirements
pip install -r requirements.txt

3️.Connect MongoDB
Create an account at MongoDB Atlas
Make a cluster and get the connection string
Paste that URL in this file:
src/constants/__init__.py
Like this:
MONGODB_URL_KEY = "your-mongodb-url-here"

4.Start the Web App
python -m streamlit run app.py


Project Structure:
myntra_scrapper/
│
├── app.py                  ← Main Streamlit app
├── requirements.txt        ← List of required Python libraries
├── setup.py                ← (Optional) for pip packaging
├── src/                    ← All the backend logic
│   ├── scrapper/           ← Scraping code using Selenium
│   ├── cloud_io/           ← MongoDB insert and retrieve
│   ├── constants/          ← MongoDB URLs, database name etc.
│   ├── data_report/        ← Optional analysis notebook
│   └── utils/              ← Helper functions (if needed)
├── pages/                  ← Extra pages for analysis
├── static/ & templates/    ← CSS or HTML files (if needed)
└── data.csv                ← Auto-generated file with reviews


Git & GitHub Workflow

Initial Setup
1.git init
2.git add .
3.git commit -m "Initial commit"
4.git branch -M main
5.git remote add origin https://github.com/gautamMohit2022/myntra_review_project.git
6.git push -u origin main

Regular Workflow
1.git add .
2.git commit -m "Fixed bugs / Added features"
3.git pull origin main --rebase
4.git push origin main

Screenshots:

 ![Search](https://github.com/user-attachments/assets/cdb988fe-055c-4231-a7f5-942efbb7cc3a)  
 ![Reviews](https://github.com/user-attachments/assets/03b3f900-3d56-472b-b7f7-03b67219e7c9) 
 ![Ratings](https://github.com/user-attachments/assets/f9ce0b4b-6877-4b0e-a36a-380bd6ff0228) 
 ![Screenshot 2025-07-03 142850](https://github.com/user-attachments/assets/ceaa8e96-eca4-41be-a9fd-5b073b4d4b6f)




















