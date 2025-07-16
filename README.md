💳 DeFi Wallet Credit Scoring System
This project implements a machine learning–based system that assigns a credit score (0–1000) to user wallets by analyzing historical DeFi transaction data from the Aave protocol.

🧠 Objective
✅ Develop a robust machine learning model (XGBoost) to evaluate the creditworthiness of blockchain wallets based only on transaction history, and
✅ Provide a one-step script (wallet_score_generator.py) to process raw user transaction data from a JSON file and output wallet scores.

📁 Project Structure
r
Copy
Edit
zerutaskprem/
├── wallet_score_generator.py        <- Core scoring script (XGBoost-based)
├── xgboost_credit_model.pkl         <- Pre-trained XGBoost model
├── sample_user_data.json            <- Sample user transactions (input)
├── wallet_scores_output.csv         <- Output: Wallet-level scores
├── requirements.txt                 <- Dependencies
└── README.md                        <- You're here!
⚙️ How It Works
1. 💾 Input Format (sample_user_data.json)
Each JSON record should contain:

json
Copy
Edit
{
  "user": "0xabc123...",
  "action": "deposit",
  "usdValue": 12000.0,
  "timestamp": 1628995200
}
user: Wallet address

action: Aave transaction type (e.g., deposit, borrow, repay)

usdValue: USD equivalent value of the transaction

timestamp: Unix timestamp (in seconds)

2. 🛠️ Processing Flow
a. Preprocessing
Load and clean the JSON data

Normalize actions, convert timestamps, remove 0-value txns

b. Feature Extraction (per wallet)
The following behavioral features are extracted:

Feature	Description
total_txn_count	Total number of transactions
avg_txn_value_usd	Mean USD value per transaction
active_days	Unique number of days active
Borrow, Deposit, Repay	Total USD for each action
LiquidationCall	Amount liquidated
borrow_to_deposit_ratio	Ratio of total borrow to deposit
repay_to_borrow_ratio	Ratio of repay to borrow
activity_days_span	Duration (in days) between first and last txn

c. Prediction with XGBoost
The extracted features (except timestamps and wallet) are passed to a trained xgboost_credit_model.pkl model to predict a credit score between 0 (worst) and 1000 (best).

🧪 Model Architecture
Model: XGBoostRegressor

Trained on: Curated and cleaned Aave v2 transaction dataset

Target: Pseudo-credit score generated using a hybrid rule-based logic

Evaluation:

MAE: ~3.5

R²: 0.999

📌 Feature importance and hyperparameter tuning were done via grid search + domain knowledge.

🖥️ Running the Script
Place your input JSON file (e.g., sample_user_data.json) in the same directory.

Run:

bash
Copy
Edit
python wallet_score_generator.py sample_user_data.json
Output will be saved as:

bash
Copy
Edit
wallet_scores_output.csv
Containing columns like:

wallet	Borrow	Deposit	...	xgboost_score

🧩 Extensibility
🔍 Add new features: E.g., frequency of borrowing, slippage analysis, etc.

🧠 Swap models: You can replace the XGBoost model with another (e.g., LightGBM, CatBoost)

📉 Custom training: Use your own dataset and labels to retrain the model using xgb_model.fit()

🛡️ Score Logic Transparency
Scores are learned from a hybrid rule-based + heuristics system, validated with actual wallet behaviors (repayment regularity, liquidation penalties, etc.)

The model places positive weight on:

High repayment ratios

Consistent activity

Low liquidations

Reasonable borrow-to-deposit behavior

📊 Example Output (Snippet)
Wallet	Borrow	Deposit	Repay	Score
0xabc123...	12000	25000	11500	716
0xdef456...	0	3000	0	197

📦 Requirements
Install using:

bash
Copy
Edit
pip install -r requirements.txt
Dependencies:

xgboost

pandas

joblib

👨‍💻 Author
Pream Venkatesh Bagga
B.Tech in CSE (Data Science)
Saraswati College of Engineering, Mumba
➡️ For score distribution and behavioral insights, see [analysis.md](./analysis.md)

## 👨‍💼 Author

**Pream Venkatesh Bagga**

> For questions, contact via LinkedIn or GitHub.
# DeFi-Wallet-Credit-Scoring
