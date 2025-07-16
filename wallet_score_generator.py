# # wallet_score_generator.py
# import json
# import pandas as pd
# import sys
# from datetime import datetime
# from joblib import load

# # Load trained XGBoost model
# try:
#     xgb_model = load(r"C:\prem program files\zerutaskprem\xgboost_credit_model.pkl")
#     print("✅ XGBoost model loaded.")
# except:
#     print("❌ ERROR: xgboost_credit_model.pkl not found.")
#     sys.exit(1)

# def load_transactions(json_file):
#     with open(json_file, 'r') as f:
#         return json.load(f)

# def preprocess_transactions(transactions):
#     records = []
#     for item in transactions:
#         wallet = item.get('user', '')
#         action = item.get('action', '').lower()
#         usd_value = float(item.get('usdValue', 0.0))
#         timestamp = pd.to_datetime(item.get('timestamp', None), unit='s')

#         if wallet and usd_value > 0 and timestamp:
#             records.append({
#                 'wallet': wallet,
#                 'action': action,
#                 'usd_value': usd_value,
#                 'timestamp': timestamp
#             })
#     return pd.DataFrame(records)

# def extract_wallet_features(df):
#     wallets = df['wallet'].unique()
#     features = []

#     for wallet in wallets:
#         user_df = df[df['wallet'] == wallet]
#         actions = user_df.groupby('action')['usd_value'].sum().to_dict()
#         txn_count = len(user_df)
#         avg_value = user_df['usd_value'].mean()
#         active_days = user_df['timestamp'].dt.date.nunique()
#         first_txn = user_df['timestamp'].min()
#         last_txn = user_df['timestamp'].max()
#         span = (last_txn - first_txn).days + 1

#         deposit = actions.get('deposit', 0.0)
#         borrow = actions.get('borrow', 0.0)
#         repay = actions.get('repay', 0.0)
#         redeem = actions.get('redeemunderlying', 0.0)
#         liquidation = actions.get('liquidationcall', 0.0)

#         borrow_to_deposit = borrow / deposit if deposit > 0 else 0
#         repay_to_borrow = repay / borrow if borrow > 0 else 0

#         features.append({
#             'wallet': wallet,
#             'total_txn_count': txn_count,
#             'avg_txn_value_usd': avg_value,
#             'active_days': active_days,
#             'first_txn': first_txn,
#             'last_txn': last_txn,
#             'Borrow': borrow,
#             'Deposit': deposit,
#             'Repay': repay,
#             'RedeemUnderlying': redeem,
#             'LiquidationCall': liquidation,
#             'borrow_to_deposit_ratio': borrow_to_deposit,
#             'repay_to_borrow_ratio': repay_to_borrow,
#             'activity_days_span': span
#         })
#     return pd.DataFrame(features)

# def predict_scores(feature_df):
#     X = feature_df.drop(columns=['wallet', 'first_txn', 'last_txn'])
#     X = X[['total_txn_count', 'avg_txn_value_usd', 'active_days',
#            'Borrow', 'Deposit', 'Repay', 'RedeemUnderlying',
#            'LiquidationCall', 'borrow_to_deposit_ratio',
#            'repay_to_borrow_ratio', 'activity_days_span']]  # force correct order
#     predicted_scores = xgb_model.predict(X, validate_features=False)
#     return predicted_scores


# def main(json_input):
#     print("📥 Loading user transactions...")
#     transactions = load_transactions(json_input)

#     print("🔄 Preprocessing data...")
#     df = preprocess_transactions(transactions)

#     print("📊 Extracting wallet-level features...")
#     features_df = extract_wallet_features(df)

#     print("🤖 Predicting credit scores using XGBoost...")
#     features_df['xgboost_score'] = predict_scores(features_df)

#     print("💾 Saving to wallet_scores_output.csv")
#     features_df.to_csv("wallet_scores_output.csv", index=False)
#     print("✅ Done! Scores saved.")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python wallet_score_generator.py <user_transactions.json>")
#     else:
#         main(sys.argv[1])
# wallet_score_generator.py (Streamlit Version)

import streamlit as st
import pandas as pd
import json
from datetime import datetime
from joblib import load

# Load model
@st.cache_resource
def load_model():
    try:
        model = load("xgboost_credit_model.pkl")
        return model
    except:
        st.error("❌ Model file not found. Please ensure 'xgboost_credit_model.pkl' is in the app directory.")
        return None

xgb_model = load_model()

# Helper Functions
def preprocess_transactions(transactions):
    records = []
    for item in transactions:
        wallet = item.get('user', '')
        action = item.get('action', '').lower()
        usd_value = float(item.get('usdValue', 0.0))
        timestamp = pd.to_datetime(item.get('timestamp', None), unit='s')

        if wallet and usd_value > 0 and timestamp:
            records.append({
                'wallet': wallet,
                'action': action,
                'usd_value': usd_value,
                'timestamp': timestamp
            })
    return pd.DataFrame(records)

def extract_features(df):
    wallets = df['wallet'].unique()
    features = []

    for wallet in wallets:
        user_df = df[df['wallet'] == wallet]
        actions = user_df.groupby('action')['usd_value'].sum().to_dict()
        txn_count = len(user_df)
        avg_value = user_df['usd_value'].mean()
        active_days = user_df['timestamp'].dt.date.nunique()
        first_txn = user_df['timestamp'].min()
        last_txn = user_df['timestamp'].max()
        span = (last_txn - first_txn).days + 1

        deposit = actions.get('deposit', 0.0)
        borrow = actions.get('borrow', 0.0)
        repay = actions.get('repay', 0.0)
        redeem = actions.get('redeemunderlying', 0.0)
        liquidation = actions.get('liquidationcall', 0.0)

        borrow_to_deposit = borrow / deposit if deposit > 0 else 0
        repay_to_borrow = repay / borrow if borrow > 0 else 0

        features.append({
            'wallet': wallet,
            'total_txn_count': txn_count,
            'avg_txn_value_usd': avg_value,
            'active_days': active_days,
            'Borrow': borrow,
            'Deposit': deposit,
            'Repay': repay,
            'RedeemUnderlying': redeem,
            'LiquidationCall': liquidation,
            'borrow_to_deposit_ratio': borrow_to_deposit,
            'repay_to_borrow_ratio': repay_to_borrow,
            'activity_days_span': span
        })
    return pd.DataFrame(features)

def predict_scores(feature_df):
    X = feature_df.drop(columns=['wallet'])
    X = X[['total_txn_count', 'avg_txn_value_usd', 'active_days',
           'Borrow', 'Deposit', 'Repay', 'RedeemUnderlying',
           'LiquidationCall', 'borrow_to_deposit_ratio',
           'repay_to_borrow_ratio', 'activity_days_span']]
    predicted_scores = xgb_model.predict(X, validate_features=False)
    return predicted_scores

# Streamlit UI
st.title("🔎 DeFi Wallet Credit Score Predictor")
st.markdown("Upload a JSON file of user transactions to generate credit scores (0-1000).")

uploaded_file = st.file_uploader("📂 Upload JSON File", type="json")

if uploaded_file and xgb_model:
    try:
        transactions = json.load(uploaded_file)
        df = preprocess_transactions(transactions)
        features_df = extract_features(df)
        features_df['xgboost_score'] = predict_scores(features_df)

        st.success("✅ Credit scores predicted!")
        st.dataframe(features_df[['wallet', 'xgboost_score']])

        csv = features_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV", csv, "wallet_scores.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")

