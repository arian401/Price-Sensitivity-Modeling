# 💸 Price Sensitivity Modeling

[![API - Render](https://img.shields.io/badge/API%20(Render)-Live-blue)](https://price-sensitivity-api.onrender.com/docs)  
[![API - HuggingFace](https://img.shields.io/badge/API%20(HuggingFace)-Live-blue)](https://arian401-Price-Sensitivity-Modeling.hf.space/docs)  
[![Streamlit App](https://img.shields.io/badge/Streamlit%20App-Live-green)](https://huggingface.co/spaces/Arian401/Price-Sensitivity-Streamlit-App)  
[![GitHub Actions](https://github.com/arian401/Price-Sensitivity-Modeling/actions/workflows/test.yml/badge.svg)](https://github.com/arian401/Price-Sensitivity-Modeling/actions)

---

## 🎯 Overview

This project predicts whether a customer will **continue buying after a price increase**, helping booking platforms (e.g., Expedia, Kayak) personalize pricing in real-time.

It combines a **FastAPI-based machine learning model**, a **Streamlit frontend**, and a **stub backend** to simulate real-world pricing engines.

---

## 🚀 Live Deployments

| Component         | URL                                                                 |
|------------------|----------------------------------------------------------------------|
| API (Render)      | [https://price-sensitivity-api.onrender.com/docs](https://price-sensitivity-api.onrender.com/docs) |
| API (Hugging Face)| [https://arian401-Price-Sensitivity-Modeling.hf.space/docs](https://arian401-Price-Sensitivity-Modeling.hf.space/docs) |
| UI (Streamlit App)| [https://huggingface.co/spaces/Arian401/Price-Sensitivity-Streamlit-App](https://huggingface.co/spaces/Arian401/Price-Sensitivity-Streamlit-App) |

---

## 📦 Repository Structure

```
.
├── Render/              # FastAPI API backend (Render deployment)
├── HuggingFace/         # FastAPI API for Hugging Face Spaces
├── Streamlit/           # Streamlit frontend
├── RealTime Pricing/    # Flask stub backend to simulate dynamic pricing
├── data/                # Synthetic dataset
├── models/              # Trained model artifacts (.pkl, .json)
├── test_api.py          # CI test to check /predict endpoint
├── train_and_export.py  # Online retraining script
├── .github/workflows/   # GitHub Actions CI pipeline
```

---

## 🛠️ How It Works

- **Data:** Simulated travel customer behavior with 9 features.
- **Model:** Logistic Regression pipeline (scikit-learn), exportable via `joblib`.
- **API:** Receives JSON with 9 features, returns:
  ```json
  {
    "will_buy_after_price_increase": 1,
    "probability": 0.8234
  }
  ```
- **Streamlit App:** Interactive UI to test predictions manually or in batches.
- **Stub Backend:** Simulates an e-commerce pricing server using real-time predictions.

---

## 📊 Sample Input (Customer)

```json
{
  "total_spent": 2005.79,
  "avg_order_value": 629.24,
  "avg_purchase_frequency": 1.1,
  "days_since_last_purchase": 45,
  "discount_behavior": 0.0,
  "loyalty_program_member": 1,
  "days_in_advance": 3,
  "flight_type": "domestic",
  "cabin_class": "economy"
}
```

---

## ✅ Skills Demonstrated

- FastAPI and Pydantic for ML APIs  
- Streamlit dashboarding  
- Docker for reproducible deployment  
- CI integration with GitHub Actions  
- Real-time prediction architecture  
- Model versioning with `joblib` and `.env` config  
- ML engineering + deployment (ready for MLOps projects) ✅

---

## 🧪 CI: Integration Test

Every push to the repo runs `test_api.py` to confirm that:
- The deployed `/predict` endpoint is live
- Response contains expected keys
- Status code = 200

Workflow: [.github/workflows/test.yml](.github/workflows/test.yml)  
Status: [GitHub Actions](https://github.com/arian401/Price-Sensitivity-Modeling/actions)

---

## 🖼️ Streamlit App Preview

![Streamlit App Screenshot](https://huggingface.co/spaces/Arian401/Price-Sensitivity-Streamlit-App/resolve/main/streamlit_screenshot.png)

---

## 📈 Real-World Use Cases

- **Travel platforms:** Expedia, Kayak – optimize ticket prices based on user loyalty
- **Retail apps:** Personalize discounts or upsell prices
- **Subscription services:** Predict churn after price increases

---

## 📩 Contact

**Amin Sokhanvar**  
[LinkedIn Profile](https://www.linkedin.com/in/amin-sokhanvar/)  
Open to MLOps, data science, and API integration projects.
