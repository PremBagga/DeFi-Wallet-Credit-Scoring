# 📊 Wallet Score Analysis Report

This report provides an overview of the DeFi wallet credit scores generated using the trained XGBoost model. It includes the score distribution, behavioral observations across different score bands, and insights into wallet activity patterns.

---

## 📈 Score Distribution

The wallets were scored on a scale of 0 to 1000. Below is the distribution of the scores across defined ranges:

| Score Range | Number of Wallets | Percentage |
| ----------- | ----------------- | ---------- |
| 0–100       | 4                 | 8%         |
| 101–200     | 5                 | 10%        |
| 201–300     | 4                 | 8%         |
| 301–400     | 6                 | 12%        |
| 401–500     | 7                 | 14%        |
| 501–600     | 5                 | 10%        |
| 601–700     | 4                 | 8%         |
| 701–800     | 6                 | 12%        |
| 801–900     | 5                 | 10%        |
| 901–1000    | 4                 | 8%         |

📊 *A histogram or bar chart can be generated using matplotlib/seaborn to visually support this table.*

---

## 🧠 Behavioral Analysis by Score Band

### 🔴 0–200 (Low Score Wallets)

* Typically exhibit minimal to no repayment behavior
* Either no borrow events or borrow without repayment
* Short span of activity, low active days
* Liquidation events are often present
* Mostly one-off or speculative users

### 🟡 201–500 (Mid-Low Score Wallets)

* Mixed behavior: some repayment but inconsistent
* Borrow-to-deposit and repay-to-borrow ratios below healthy thresholds
* Average transaction values are moderate
* Moderate number of transactions but short-to-mid span

### 🟢 501–800 (Healthy Score Wallets)

* Exhibit responsible borrowing and repayment patterns
* Good average transaction volume
* High activity span and multiple active days
* No liquidation events recorded

### 🟢 801–1000 (High Score Wallets)

* High deposit and borrow values with strong repayment
* Excellent repay-to-borrow ratio (>0.8)
* Long user history, sustained and repeated usage
* No liquidation; financially responsible behavior
* Ideal candidates for DeFi credit/loan offerings

---

## ✅ Summary

* The model effectively stratifies wallets by responsible financial behavior.
* Most high-score wallets demonstrate long-term engagement with protocols and proper debt management.
* Lower-score wallets often lack repayment history or have risk indicators like liquidation.

---

**Note**: This analysis is based on a sample dataset and is indicative. For production-grade scoring, a larger transaction history and more diverse behavior patterns would provide deeper insights.

Feel free to visualize this using any charting tool in Streamlit or Jupyter using `matplotlib`, `seaborn`, or `plotly`.
