# Sentiment-Analysis

![Netflix Icon](https://www.google.com/url?sa=i&url=https%3A%2F%2Ficon-icons.com%2Ficon%2FNetflix-macOS-BigSur%2F189917&psig=AOvVaw1CPX9Qb46TOvE7z_Kwdd2e&ust=1698911151573000&source=images&cd=vfe&ved=0CBIQjRxqFwoTCOi9uK-nooIDFQAAAAAdAAAAABAE)

Netflix Sentiment Analysis is a Streamlit web application that allows users to analyze the sentiment of descriptions for Netflix movie and TV show titles. The app provides an interactive interface to check the sentiment of your own description and explore sentiment trends within Netflix content.

Features

- Check Sentiment: Enter your own description to check its sentiment (Positive, Neutral, or Negative).

- Filter by Title Type: Choose to analyze all Netflix titles, movies, or TV shows.

- Select Movie or TV Show: Pick a specific title from the filtered list for sentiment analysis.

- Interactive Chart: Visualize sentiment trends over the years with an interactive grouped bar chart.

  Usage
  
1. Install the required Python packages using pip install -r requirements.txt.

2. Run the Streamlit app with the following command:
   ```bash
   streamlit run app.py
   ```
   
3. Access the app through your web browser.

4. Enter your description, select title type, and choose a specific title from the sidebar to view sentiment analysis results.

5. Explore sentiment trends with the interactive chart.

Data Source

The app uses data from the Netflix Titles dataset, which is not included in this repository. You can obtain the dataset from [Netflix Titles on Kaggle](https://www.kaggle.com/shivamb/netflix-shows).

Dependencies

- Python
- Streamlit
- Pandas
- Plotly Express
- TextBlob

  

