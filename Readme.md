
MYNTRA SCRAPPER
Basic Intro:
1.Empty Folder
2.VScode
3.Environment
4.Requirements.txt
5.Setup.py
COMMANDS:
conda create -p ./env python=3.10 -y
conda activate ./env
pip install -r requirements.txt
create file gitignore
GITHUB CONNECT
1.git add  .
2. git commit -m "This is my Initial commit"
3. git branch -M main
4. git remote add origin https://github.com/gautamMohit2022/myntra_review_project.git
5. git push -u origin main
##Update git ignore by creating new file in github.type .gitignore and the use language and copy the content and paste it in your file.
Pip install ipykernel
After analyzing jupyter notebook.
Create Folders :
Src:
1.Cloud.io(Handles cloud_related i/o(if needed))-__init__.py
2.Constants(Consider any constants used across the project)-__init__.py
3.Data_report(can be used for generating data report)-__init__.py,generate_data_report.py
4.Scrapper(contains all the logic for scraping data)-__init__.py,scrape.py
5.Utils(Helper functions that can be used in different parts o0f project )-__init__.py
File:
exception.py(contains custom exceptions)
__init__.py
New Folders in myntra scrapper:
1.Pages-generate_analysis.py
2. Static\css-main.css,style.css
3.templates-base.html,index.html,results.html
MongoDB:
Mongodbatlas
Create account and password
Copy url paste into constants init file
STREAMLIT-Python Library for creating interactive web applications with case.
MongoDB-No_sql database used to store and large extracted data.
Database_connect-A package used to simplify the connection to mongodb. 
Command-python -m streamlit run "app.py"

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.31.163:8501


  



