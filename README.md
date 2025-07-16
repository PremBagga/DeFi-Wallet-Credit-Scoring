# 💳 DeFi Wallet Credit Score Predictor

This project implements a **Streamlit-based web application** that predicts a **credit score (0–1000)** for DeFi wallets based solely on their **historical transaction behavior**, using a trained **XGBoost machine learning model**.

---

## ✅ Features

* Upload your own JSON file of Aave-like user transactions.
* Predict credit scores in real-time using the XGBoost model.
* View processed results in a table.
* Download the results as a CSV file.

---

## ⚙️ Methodology & Architecture

### 1. **Model Choice:**

* Chosen model: `XGBoostRegressor` due to its strong performance with tabular data and handling of nonlinear relationships.
* Trained using historical user-level DeFi transaction features like deposit/borrow/repay amounts, ratios, and activity metrics.

### 2. **Features Used:**

| Feature                                                             | Description                                       |
| ------------------------------------------------------------------- | ------------------------------------------------- |
| `total_txn_count`                                                   | Number of transactions per wallet                 |
| `avg_txn_value_usd`                                                 | Average transaction value (USD)                   |
| `active_days`                                                       | Number of unique days with activity               |
| `Borrow`, `Deposit`, `Repay`, `RedeemUnderlying`, `LiquidationCall` | Total USD value for each action type              |
| `borrow_to_deposit_ratio`                                           | Ratio of borrow to deposit volume                 |
| `repay_to_borrow_ratio`                                             | Ratio of repay to borrow volume                   |
| `activity_days_span`                                                | Span (in days) between first and last transaction |

These are extracted dynamically from uploaded JSON data before prediction.

---

## ♻️ Processing Flow

```
📂 Upload JSON File (user_transactions.json)
    ↓
📊 Preprocessing:
   - Clean and normalize fields: user, action, usdValue, timestamp
   - Convert to Pandas DataFrame
    ↓
📈 Feature Extraction:
   - Group by wallet
   - Aggregate features listed above
    ↓
🤖 Prediction:
   - Load XGBoost model (`xgboost_credit_model.pkl`)
   - Score each wallet (0–1000)
    ↓
📄 Output:
   - View scores in a table
   - Download CSV
```

---

## 📁 Project Structure

```
zerutaskprem/
├── xgboost_credit_model.pkl      # Pretrained XGBoost model
├── wallet_score_generator.py     # Streamlit app (main UI + prediction logic)
├── sample_user_data.json         # Example transaction input file
├── wallet_scores.csv             # Output (after upload)
├── README.md                     # This file
```

---

## 🛆 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```txt
streamlit
pandas
xgboost
joblib
```

---

## 🚀 Running the App

```bash
streamlit run wallet_score_generator.py
```

---

## 📌 Notes

* The model is trained offline and saved as a `.pkl` file (`xgboost_credit_model.pkl`). This app only **loads** and **uses** it.
* The JSON file should follow this structure:

```json
[
  {
    "user": "0xabc123...",
    "action": "deposit",
    "usdValue": 2500,
    "timestamp": 1628985600
  },
  ...
]
```

---

## 🧠 Scoring Logic

* The XGBoost model outputs a **continuous score between 0 and 1000**.
* Higher scores represent wallets with:

  * Active, consistent participation
  * Balanced borrowing and repayment
  * Fewer liquidations
  * Strong financial behavior in the DeFi ecosystem

---

## 📬 Contact

Created by **Prem Venkatesh Bagga**  
*CSE(Data Science) , 9.5 CGPA*
Feel free to reach out for improvements or suggestions!
