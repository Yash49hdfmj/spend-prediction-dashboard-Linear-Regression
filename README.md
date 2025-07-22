# E-Commerce Spending Prediction Dashboard

This project predicts yearly customer spending based on their activity on an e-commerce platform. It includes data exploration, regression modeling (Linear, Ridge, and Lasso), evaluation, and a deployment-ready **Streamlit dashboard**.

---

## Tech Stack & Libraries

* **Languages:** Python 3
* **Libraries:**

  * Data Handling: `pandas`, `numpy`
  * Visualization: `matplotlib`, `seaborn`
  * Modeling: `scikit-learn`, `statsmodels`, `joblib`
  * App Interface: `streamlit`

---

## Dataset

* **Source:** `Ecommerce Customers.csv`
* **Features Used:**

  * `Avg. Session Length`
  * `Time on App`
  * `Time on Website`
  * `Length of Membership`
  * `Yearly Amount Spent` (target)

---

## 📊 Exploratory Data Analysis (EDA)

* **Scatterplots** to explore relationships (e.g. Time on App vs Yearly Spending)
* **Barplots** to analyze binned behavior
* **Pairplots & Jointplots** for pairwise feature insights
* **Distribution plots** for residual analysis

---

## Modeling

###  Linear Regression (OLS)

* Performed using both `scikit-learn` and `statsmodels`
* Extracted coefficients and evaluated performance (R² score)

### Ridge & Lasso Regression

* Added regularization to improve generalization
* Used pipelines with standard scaling
* Compared metrics: MAE, MSE, RMSE, R2

### ⚖ Multicollinearity Check

* Used **Variance Inflation Factor (VIF)** to ensure no multicollinearity among features

---

##  Model Evaluation

* **Metrics Used:**

  * Mean Absolute Error (MAE)
  * Mean Squared Error (MSE)
  * Root Mean Squared Error (RMSE)
  * R² Score
* **Plots:**

  * Actual vs Predicted
  * Residual distribution
  * Normal Q-Q plot

---

