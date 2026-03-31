COVID-19 Interactive Dashboard

Project Overview

This project is an interactive COVID-19 dashboard built using Flask, Pandas, and Plotly. It allows users to explore trends in COVID-19 metrics such as new cases, deaths, and vaccinations across different countries over time. The dashboard dynamically updates based on user selections without requiring a page reload.

Features

Select country and metric using dropdown menus

Interactive time-series visualization using Plotly

Dynamic updates using Flask API (/data route)

Insight generation explaining trends and patterns

Smooth user experience without page reload


Technologies Used

Flask (backend framework)

Pandas (data processing and cleaning)

Plotly (data visualization)

HTML, CSS, JavaScript (frontend)

Data Processing

Missing values in new_vaccinations were filled with 0 to preserve dataset structure
Data was sorted by date for correct chronological visualization
A 7-day rolling average was computed to smooth fluctuations
Monthly aggregations were created for additional analysis

Insights & Analysis

The dashboard highlights trends such as spikes in cases, vaccination rollouts, and mortality patterns. It emphasizes that correlation does not imply causation, as trends may be influenced by reporting delays, policy changes, or real-world events. Death data often lags behind case data, and vaccination spikes may result from batch reporting.

How to Run the Project

Clone the repository:
git clone https://github.com/your-username/your-repo.git

Navigate into the project folder:
cd your-repo

Install dependencies:
pip install flask pandas plotly

Run the application:
flask run

or
python app.py
Open in browser:
http://127.0.0.1:5000/

API Endpoint

/data?country=Canada&metric=new_cases

Returns JSON data used to dynamically update the chart.

Project Structure

project/
│── app.py

│── templates/

│ └── index.html

│── static/

│ └── styles.css

│── cleaned_covid_data.csv

│── COVID_Country_Sample.csv

Learning Outcomes
Data cleaning and preprocessing with Pandas

Building a Flask web application

Creating interactive visualizations with Plotly

Handling API requests and dynamic updates

Designing a responsive dashboard interface

Author

Jason Noronha
