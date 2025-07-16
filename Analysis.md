# analysis.md

## 🔢 Credit Score Distribution & Behavioral Analysis (Aave V2 Wallets)

This analysis provides insight into how the credit scores (0 to 1000) were distributed across wallets, and what behaviors were most common among low- and high-scoring wallets.

---

## 📊 Score Distribution

Wallets were bucketed into the following score ranges:

| Score Range | # Wallets | Percentage |
| ----------- | --------- | ---------- |
| 0 - 100     | 2         | 1.9%       |
| 100 - 200   | 5         | 4.8%       |
| 200 - 300   | 3         | 2.9%       |
| 300 - 400   | 2         | 1.9%       |
| 400 - 500   | 2         | 1.9%       |
| 500 - 600   | 1         | 1.0%       |
| 600 - 700   | 3         | 2.9%       |
| 700 - 800   | 2         | 1.9%       |
| 800 - 900   | 2         | 1.9%       |
| 900 - 1000  | 2         | 1.9%       |
| **Total**   | 24        | 100%       |

> ⬆️ Most wallets fell into **lower score buckets** (100–300), indicating a prevalence of low-engagement, bot-like, or passive users.

---

## 💳 Low-Scoring Wallet Behavior (0-300)

**Common Patterns:**

* ❌ Only 1-2 total transactions
* ❌ One-time deposit or redeem activity
* ❌ No `repay` or `borrow`
* ❌ Short activity span (1 day)

**Interpretation:** These wallets likely represent:

* Airdrop hunters
* Bots or short-term testers
* Users not committed to long-term lending/borrowing

**Example Wallet:**

```csv
wallet,total_txn_count,Deposit,Repay,Borrow,pseudo_score
0x000...d4b6,1,1.98e9,0.0,0.0,200
```

---

## 🌟 High-Scoring Wallet Behavior (800-1000)

**Common Patterns:**

* ✅ 50+ transactions across time
* ✅ Used `deposit`, `borrow`, and `repay` actively
* ✅ `repay_to_borrow_ratio` close to 1.0
* ✅ `borrow_to_deposit_ratio` under 1.0 (responsible lending)
* ✅ Spread usage over 30+ days

**Interpretation:** These wallets represent:

* Responsible long-term users
* Stable liquidity providers and borrowers
* High-value contributors to protocol stability

**Example Wallet:**

```csv
wallet,total_txn_count,Deposit,Borrow,Repay,repay_to_borrow_ratio,pseudo_score
0x000...cb13,25,1.83e22,1.16e10,1.16e10,~1.0,1000
```

---

## 🤝 Mid-Scoring Wallets (500-700)

* ✅ Engaged with the protocol
* ⚠️ Often borrowed more than repaid
* ❌ Shorter active spans or fewer repay events
* May represent newer users or occasional usage

---

## 🔄 Insights for DeFi Credit Risk

| Behavior                   | Score Impact    |
| -------------------------- | --------------- |
| Only deposited/redeemed    | Negative        |
| Borrowed but didn’t repay  | Strong Negative |
| Repay > Borrow             | Positive        |
| Long-term consistent usage | Strong Positive |
| Large, risky single txns   | Slight Negative |

---

## 🚀 Conclusion

This score-based analysis enables:

* Lenders to **segment wallets** by trustworthiness
* Protocols to reward good behavior with **better terms**
* Safer DeFi environments based on actual **on-chain activity**

> The scoring engine is extendable and can incorporate more data sources in future versions.

---

**Next:** View the [README.md](./README.md) for model architecture and pipeline.
