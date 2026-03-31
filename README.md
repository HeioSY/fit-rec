# 🥗 Fit-Reç — Diet Decision Support System

A personalized daily meal planning application that uses machine learning to recommend nutrition-balanced menus based on user profile and goals.

## 📸 Overview

Fit-Reç calculates a user's daily caloric and macronutrient needs using the Harris-Benedict BMR formula, then recommends a full day's menu (breakfast, lunch, dinner, snack) by training a Decision Tree classifier on a real food dataset.

## ✨ Features

- **BMR & Calorie Calculation** — Harris-Benedict formula with activity level adjustment
- **Macro Distribution** — Automatic protein / fat / carbohydrate breakdown
- **ML-Powered Menu Recommendation** — Decision Tree model trained on 5 food group datasets
- **Vitamin Tracking** — Compares daily vitamin intake against RDA values
- **Interactive Web UI** — Built with Streamlit; inputs height, weight, age, gender, and goal
- **Visual Reports** — Macro progress bar charts and vitamin intake graphs

## 🛠️ Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat)

## 📁 Project Structure

```
fit-rec/
├── Src/
│   ├── app.py               # Streamlit web application
│   ├── main.py              # CLI entry point
│   ├── calculations.py      # BMR & macro calculations
│   ├── data_processing.py   # Data loading, cleaning, model training
│   ├── menu_recommender.py  # ML-based meal recommendation engine
│   ├── vitamin_tracker.py   # Vitamin intake tracking
│   ├── plots.py             # Visualization functions
│   └── models/
│       └── decision_tree.pkl  # Trained model
└── Data/
    ├── FOOD-DATA-GROUP1.csv
    ├── FOOD-DATA-GROUP2.csv
    ├── FOOD-DATA-GROUP3.csv
    ├── FOOD-DATA-GROUP4.csv
    └── FOOD-DATA-GROUP5.csv
```

## 🚀 Getting Started

### Requirements

```bash
pip install streamlit pandas scikit-learn matplotlib
```

### Run the Web App

```bash
cd Src
streamlit run app.py
```

### Run CLI Version

```bash
cd Src
python main.py
```

## 🧠 How It Works

1. User enters their height, weight, age, gender, and goal (lose / maintain / gain weight)
2. BMR is calculated using the Harris-Benedict equation
3. Daily calorie target is adjusted based on activity level and goal
4. A Decision Tree classifier trained on food macro data recommends suitable foods
5. Foods are distributed across 4 meals with appropriate portion sizes
6. Vitamin intake is compared against daily RDA values and visualized

---

> Developed as a university project — Gazi University, MIS Department
