# 📈 Financial Sentiment Analysis App

An end-to-end machine learning project that analyzes financial text (like tweets or headlines) and classifies them into **Positive**, **Negative**, or **Neutral** sentiments.  
Includes a deployed interactive web app built with **Dash** and styled with **Bootstrap**.

---

## 🚀 Features

- Cleaned and preprocessed real-world financial tweet data
- Handled imbalanced classes with undersampling
- Vectorized text using TF-IDF
- Built a Logistic Regression model using scikit-learn
- Tuned hyperparameters using GridSearchCV
- Combined vectorizer and model into a Pipeline
- Interactive Dash app for real-time predictions
- Bootstrap-styled prediction cards with color-coded output

---

## 🧠 Technologies Used

- Python  
- pandas, numpy  
- scikit-learn  
- Dash (Plotly)  
- Bootstrap CSS  
- pickle  

---

## 📊 Model Overview

- Input: Preprocessed financial tweet  
- Output: Predicted sentiment (`Positive`, `Negative`, or `Neutral`)  
- Model used: `LogisticRegression()`  
- Text encoding: `TfidfVectorizer()`  

---

## 📂 Project Structure

financial-sentiment-analysis/
│
├── app.py                  # Dash app code
├── sentiment_pipeline.pkl  # Saved scikit-learn pipeline (TF-IDF + model)
├── README.md               # Project description and instructions

## 💻 How to Run the App Locally
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/financial-sentiment-analysis.git
cd financial-sentiment-analysis

2️⃣ Install Required Packages
pip install dash scikit-learn pandas

3️⃣ Run the App
python app.py

🧪 Example Usage
✅ Input:
Apple stock rises after strong earnings report! 

✅ Predicted Output:
Predicted Sentiment: Positive

📬 Contact
Created by: Siddharth Kumar
LinkedIn: linkedin.com/in/siddharth-kumar-89a318246

🪪 License
This project is licensed under the MIT License.