# README.md

## 📊 DeFi Wallet Credit Scoring - Aave V2

This project builds a machine learning model to generate credit scores (0-1000) for wallets interacting with the Aave V2 DeFi lending protocol. The scores reflect the reliability and behavior of users based solely on historical transaction-level data.

---

## 🧱 Problem Statement

Given raw transaction data (actions like `deposit`, `borrow`, `repay`, `redeemUnderlying`, and `liquidationCall`), assign a **credit score between 0 and 1000** to each wallet.

* High scores → responsible behavior (good repayments, consistent usage)
* Low scores → risky, one-shot, bot-like, or exploitative usage

---

## 🔧 Solution Overview

### Step 1: Feature Engineering

Transaction JSON is flattened and aggregated per wallet into the following features:

* `total_txn_count`
* `avg_txn_value_usd`
* `active_days`, `activity_days_span`
* Total `Deposit`, `Borrow`, `Repay`, `RedeemUnderlying`, `LiquidationCall`
* Derived Ratios: `borrow_to_deposit_ratio`, `repay_to_borrow_ratio`

### Step 2: Pseudo Credit Score (Rule-Based)

A robust scoring logic mimicking real-world credit systems:

* Rewards:

  * Large deposits
  * Good repay-to-borrow ratio
  * Long-term, consistent activity
  * Diverse protocol usage
* Penalties:

  * Borrowing without repaying
  * One-shot deposit + redeem
  * Very high borrow-to-deposit ratio

Final scores are clamped between 0 and 1000.

### Step 3: ML Model Training

We used two models:

* ✅ **Random Forest Regressor**
* ✅ **XGBoost Regressor** (best performance)

These models were trained using the engineered features and pseudo-scores as labels.

---

## 🛠️ Project Architecture

```
user_transactions.json  -->  flatjson.py  -->  features.csv
                                         -->  rule_based_score()
                                         -->  ML model (XGBoost/RandomForest)
                                         -->  Predict scores
```

---

## ⚡ Quick Start

### 1. Flatten JSON and Extract Features:

```bash
python flatjson.py
```

### 2. Train Models:

```bash
python train_model.py
```

### 3. Predict Scores for New Wallets:

```bash
python predict.py
```

---

## 📄 Files & Modules

* `flatjson.py` — parse & flatten JSON to generate features per wallet
* `rule_based_score.py` — apply rule-based logic for pseudo-scores
* `train_model.py` — trains RF and XGBoost models on wallet features
* `predict.py` — uses trained model to assign scores to new data
* `wallet_features_with_pseudo_score.csv` — intermediate data file
* `random_forest_credit_model.pkl` & `xgboost_credit_model.pkl`
* `analysis.md` — score distribution, wallet behavior insights

---

## 🎯 Results Summary

| Model         | MAE      | R² Score  |
| ------------- | -------- | --------- |
| Random Forest | 5.12     | 0.997     |
| XGBoost       | **3.57** | **0.999** |

---

## 🚀 Future Improvements

* Use true on-chain credit events for label supervision
* Add token volatility & asset prices
* Integrate cross-protocol behavior (e.g., Compound, Lido)

---
➡️ For score distribution and behavioral insights, see [analysis.md](./analysis.md)

## 👨‍💼 Author

**Pream Venkatesh Bagga**

> For questions, contact via LinkedIn or GitHub.
# DeFi-Wallet-Credit-Scoring
