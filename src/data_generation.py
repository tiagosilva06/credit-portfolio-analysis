import random
from datetime import datetime, timedelta

def generate_portfolio(n=10000, seed=42):
    random.seed(seed)

    products = ["Cartão de Crédito", "Empréstimo Pessoal", "Consignado", "Financiamento"]
    employment_status = ["Employed", "Self-Employed", "Unemployed"]
    payment_status = ["Adimplente", "Inadimplente", "Parcialmente Inadimplente"]

    data = []
    for i in range(n):
        safra = datetime(2022, 1, 1) + timedelta(days=random.randint(0, 730))
        product = random.choice(products)
        age = random.randint(18, 75)
        income = round(random.uniform(1500, 25000), 2)
        amount = round(random.uniform(1000, 50000), 2)
        interest_rate = round(random.uniform(0.015, 0.08), 4)
        status = random.choice(payment_status)
        employment = random.choice(employment_status)

        data.append({
            "client_id": i + 1,
            "safra": safra.strftime("%Y-%m"),
            "product": product,
            "age": age,
            "employment_status": employment,
            "monthly_income": income,
            "granted_amount": amount,
            "interest_rate": interest_rate,
            "payment_status": status
        })

    return data