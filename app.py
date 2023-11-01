import streamlit as st
import pandas as pd
import plotly.express as px
from textblob import TextBlob

# Set page title and icon
st.set_page_config(
    page_title="Netflix Sentiment Analysis", page_icon=":movie_camera:"
)

# Load the Netflix dataset
@st.cache_data
def load_data():
    df = pd.read_csv('netflix_titles.csv')
    return df

df = load_data()

# Apply custom CSS for improved style
st.markdown(
    """
    <style>
    body {
        background-color: #80ced6;  /* Set the background color */
    }
    .stApp {
        background-color: gray;  /* Set the app background color */
    }
    .st-bd {
        font-family: "Times New Roman", Times, serif;  /* Change the font family */
        color: #333;  /* Set text color */
    }
    .css-19tk1mt {
        max-width: 1200px;  /* Set max width for content */
    }
    .css-1bd8bfl {
        padding: 1rem;  /* Add padding around content */
    }
    .css-5oo0f6 {
        text-align: center;  /* Center-align text */
    }
    .css-1aumxnt {
        background-color: #80ced6;  /* Set a background color for the sidebar */
        border-radius: 10px;  /* Add rounded corners to the sidebar */
        padding: 1rem;
    }
    .stSelectbox {
        background-color: #80ced6;  /* Set background color for select boxes */
        border-radius: 5px;  /* Add rounded corners to select boxes */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# User input for sentiment analysis
st.header("Check Sentiment of Your Description")
user_description = st.text_area("Enter a description:")
if user_description:
    testimonial = TextBlob(user_description)
    polarity = testimonial.sentiment.polarity
    sentiment = 'Positive' if polarity > 0 else ('Neutral' if polarity == 0 else 'Negative')
    st.write(f"Sentiment: {sentiment}")

# Sidebar for filtering by title type
st.sidebar.header("Filter by Title Type")
title_type = st.sidebar.radio("Select Title Type", ["All", "Movie", "TV Show"])

if title_type != "All":
    filtered_df = df[df['type'] == title_type]
else:
    filtered_df = df

# Dropdown for selecting specific movie or TV show
st.sidebar.header("Select Movie or TV Show")
selected_title = st.sidebar.selectbox("Choose Title", filtered_df['title'].unique())

if selected_title:
    selected_df = filtered_df[filtered_df['title'] == selected_title]
else:
    selected_df = filtered_df

# Sentiment Analysis Of Netflix Content
sentiments = []
for description in selected_df['description']:
    testimonial = TextBlob(description)
    polarity = testimonial.sentiment.polarity
    sentiment = 'Positive' if polarity > 0 else ('Neutral' if polarity == 0 else 'Negative')
    sentiments.append(sentiment)

selected_df['Sentiment'] = sentiments

# Create an interactive sentiment analysis chart with custom colors
colors = {'Negative': 'red', 'Neutral': 'blue', 'Positive': 'green'}
st.title("Sentiment Analysis of Netflix Content")
st.write("Select title type and specific title from the sidebar to see sentiment analysis results.")

# Create a grouped bar chart for sentiment analysis
sentiment_data = selected_df.groupby(['release_year', 'Sentiment']).size().reset_index(name='Total Count')
sentiment_data = sentiment_data[sentiment_data['release_year'] > 2005]

# Use a grouped bar chart
sentiment_chart = px.bar(sentiment_data, x='release_year', y='Total Count', color='Sentiment',
                        title='Sentiment Analysis of Content on Netflix',
                        color_discrete_map=colors, barmode='group')
st.plotly_chart(sentiment_chart)

# Display the filtered data
st.header("Filtered Data")
st.write(selected_df)
