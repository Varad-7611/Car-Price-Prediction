# 🚗 Car Price Prediction using Machine Learning

This project predicts the **price of a car** based on input features such as company, model, year, fuel type, transmission, and more using a **Machine Learning Regression Model**.

---

## 📊 Description

In the automobile resale market, determining a fair price for a used car is challenging. This machine learning project uses historical car listings to train a model that can predict car prices with reasonable accuracy.

---

## 🧰 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn (for EDA)
- Jupyter Notebook
- Streamlit (optional GUI)


---

## 📁 Dataset Features

The dataset includes:

- `Company` – Car brand (e.g., Toyota, Honda)
- `Model` – Model name
- `Year` – Year of manufacture
- `Fuel Type` – Petrol, Diesel, CNG, Electric, etc.
- `Transmission` – Manual or Automatic
- `Owner` – First, Second, Third, etc.
- `Kilometers Driven` – Number of kilometers driven
- `Price` – Target variable (car's selling price)

---

## 🧠 Machine Learning Model

We use a **Random Forest Regressor** due to its performance on regression tasks and ability to handle both categorical and numerical features.

Other possible models:
- Linear Regression
- Decision Tree Regressor
- XGBoost Regressor

---

## 🚀 Workflow

1. **Data Preprocessing**: Handle null values, encode categorical variables, scale numerical features.
2. **Model Training**: Split data into training and testing sets and train a regression model.
3. **Model Evaluation**: Use R² Score, MAE, and RMSE to evaluate performance.
4. **Prediction**: Input car details to get a price prediction.
5. **Deployment**: Deploy model with Flask API or Streamlit app.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/car-price-prediction.git
cd car-price-prediction
