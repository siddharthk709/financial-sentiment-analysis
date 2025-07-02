#!/usr/bin/env python
# coding: utf-8

# In[3]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pickle

# Load the trained pipeline
with open('sentiment_pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

# Map your model's labels to readable classes
label_map = {
    -1: 'Neutral',
     0: 'Negative',
     1: 'Positive'
}

# Choose display colors
color_map = {
    'Positive': 'green',
    'Negative': 'red',
    'Neutral': 'orange'
}

# Initialize Dash app
external_stylesheets = ['https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css']
app = dash.Dash(__name__)
server = app.server  # for deployment (Heroku, Render, etc.)

# App layout
app.layout = html.Div(style={'fontFamily': 'Arial'}, children=[
    html.H1("📊 Financial Sentiment Classifier", style={'textAlign': 'center'}),

    html.Div([
        dcc.Textarea(
            id='input-text',
            value='Enter a financial tweet or message here...',
            style={'width': '100%', 'height': 100, 'fontSize': 16}
        ),
        html.Br(),
        html.Button('Analyze Sentiment', id='submit-button', n_clicks=0, style={'marginTop': '10px'}),
        html.Div(id='output-sentiment', className='card text-white bg-success mb-3', style={'maxWidth': '400px', 'margin': 'auto', 'padding': '20px'})

    ], style={
        'width': '60%',
        'margin': 'auto',
        'padding': 30,
        'border': '2px solid #007BFF',
        'borderRadius': '10px',
        'backgroundColor': '#F9FAFB',
        'boxShadow': '2px 2px 8px #888888'
    })
])

# Callback for prediction
@app.callback(
    Output('output-sentiment', 'children'),
    Input('submit-button', 'n_clicks'),
    State('input-text', 'value')
)

    if n_clicks > 0 and text.strip():
        pred = pipeline.predict([text])[0]
        sentiment = label_map.get(pred, "Unknown")
        color = color_map.get(sentiment, 'black')
        return html.Span(f"Predicted Sentiment: {sentiment}", style={'color': color})
    return ""

# Run app
if __name__ == '__main__':
    app.run(debug=True)
def predict_sentiment(n_clicks, text):


# In[5]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pickle

#  Load your saved pipeline (TF-IDF + model)
with open('sentiment_pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

#  Mapping label → sentiment
label_map = {
    -1: 'Neutral',
     0: 'Negative',
     1: 'Positive'
}

#  Choose Bootstrap color classes for each sentiment
color_map = {
    'Positive': 'success',  # Green
    'Negative': 'danger',   # Red
    'Neutral': 'warning'    # Yellow/Orange
}

#  Use external Bootstrap stylesheet
external_stylesheets = ['https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server  # For deployment

#  App layout
app.layout = html.Div([
    html.Div([
        html.H2("📊 Financial Sentiment Classifier", className='text-center text-primary mt-4 mb-4'),

        dcc.Textarea(
            id='input-text',
            value='Enter a financial tweet or comment...',
            className='form-control mb-3',
            style={'height': '100px'}
        ),

        html.Button('Analyze Sentiment', id='submit-button', n_clicks=0, className='btn btn-primary'),

        html.Div(id='output-card', className='mt-4')
    ], className='container')
])

#  Callback to predict sentiment and update card
@app.callback(
    Output('output-card', 'children'),
    Input('submit-button', 'n_clicks'),
    State('input-text', 'value')
)
def predict_sentiment(n_clicks, text):
    if n_clicks > 0 and text.strip():
        pred = pipeline.predict([text])[0]
        sentiment = label_map.get(pred, "Unknown")
        card_color = color_map.get(sentiment, "secondary")  # default gray
        return html.Div([
            html.Div([
                html.Div([
                    html.H5("Predicted Sentiment", className="card-title"),
                    html.P(sentiment, className="card-text", style={'fontSize': '22px'})
                ], className=f"card-body text-white bg-{card_color}")
            ], className="card text-center", style={'maxWidth': '400px', 'margin': 'auto'})
        ])
    return ""

#  Run the app
if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




