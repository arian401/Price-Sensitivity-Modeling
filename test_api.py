import requests

def test_api_prediction():
    #url = "https://arian401-Price-Sensitivity-Modeling.hf.space/predict/"
    url = "https://price-sensitivity-api.onrender.com/predict/"

    payload = {
        "total_spent": 1000,
        "avg_order_value": 300,
        "avg_purchase_frequency": 1.5,
        "days_since_last_purchase": 30,
        "discount_behavior": 0.1,
        "loyalty_program_member": 1,
        "days_in_advance": 10,
        "flight_type": "domestic",
        "cabin_class": "economy"
    }
    r = requests.post(url, json=payload)
    assert r.status_code == 200
    out = r.json()
    assert "will_buy_after_price_increase" in out
    assert "probability" in out
