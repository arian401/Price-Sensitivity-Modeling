"""
Local stub backend that mimics a booking‑platform server.

• Builds synthetic customer features (9 fields expected by your FastAPI API)
• Sends them to the Hugging Face predictor
• If the model says the customer will still buy after a 10 % price rise,
  it returns the price increased by 10 %.
"""

import os, random, requests
from flask import Flask, jsonify
from dotenv import load_dotenv

# ─────── Load env vars (.env must sit in the same folder) ────────
load_dotenv()
API_URL = os.getenv(
    "PRICE_API",
    "https://arian401-price-optimization.hf.space/predict/",  # fallback
)

app = Flask(__name__)

# -----------------------------------------------------------------
# Helper: create one synthetic customer record
# -----------------------------------------------------------------
def build_customer() -> dict:
    return {
        "total_spent": round(random.uniform(50, 5000), 2),
        "avg_order_value": round(random.uniform(20, 800), 2),
        "avg_purchase_frequency": round(random.uniform(0.2, 5), 2),
        "days_since_last_purchase": random.randint(1, 365),
        "discount_behavior": round(random.uniform(0, 1), 2),
        "loyalty_program_member": random.choice([0, 1]),
        "days_in_advance": random.randint(0, 180),
        "flight_type": random.choice(["domestic", "international"]),
        "cabin_class": random.choice(["economy", "business"]),
    }


# -----------------------------------------------------------------
# POST /simulate-booking  → returns price quoted to this customer
# -----------------------------------------------------------------
@app.post("/simulate-booking")
def simulate_booking():
    customer = build_customer()
    original_price = round(random.uniform(100, 1500), 2)

    # --- Call the predictor --------------------------------------------------
    try:
        r = requests.post(API_URL, json=customer, timeout=10)
        r.raise_for_status()
        result = r.json()
        prediction = result.get("will_buy_after_price_increase")
        prob = result.get("probability")
    except Exception as exc:
        return jsonify({"error": f"API error – {exc}"}), 502

    # --- Business rule -------------------------------------------------------
    if prediction == 1:                                # willing to pay more
        shown_price = round(original_price * 1.10, 2)  # +10 %
        action = "Price increased by 10 %"
    else:
        shown_price = original_price
        action = "Keep original price"

    # --- Response ------------------------------------------------------------
    return jsonify(
        {
            "customer_features": customer,
            "original_price": original_price,
            "shown_price": shown_price,
            "probability": prob,
            "action": action,
        }
    )

if __name__ == "__main__":
    # For direct python stub_backend.py run (useful in some IDEs)
    app.run(debug=True)
