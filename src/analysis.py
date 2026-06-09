import pandas as pd

def pl_by_safra(df_pandas):
    return df_pandas.groupby("safra").agg(
        total_clients=("client_id", "count"),
        total_granted=("granted_amount", "sum"),
        total_revenue=("interest_revenue", "sum"),
        total_loss=("expected_loss", "sum"),
        total_net_margin=("net_margin", "sum"),
        avg_interest_rate=("interest_rate", "mean")
    ).reset_index().round(2)

def default_rate_by_product(df_pandas):
    result = df_pandas.groupby("product")["payment_status"].apply(
        lambda x: (x == "Inadimplente").sum() / len(x) * 100
    ).reset_index()
    result.columns = ["product", "default_rate"]
    return result.round(2)

def sensitivity_analysis(df_pandas):
    scenarios = [0, 10, 20, 30, 40, 50]
    results = []

    for increase in scenarios:
        adjusted_loss = df_pandas.apply(
            lambda row: round(row["granted_amount"] * 0.80, 2) * (1 + increase/100) if row["payment_status"] == "Inadimplente"
            else round(row["granted_amount"] * 0.40, 2) * (1 + increase/100) if row["payment_status"] == "Parcialmente Inadimplente"
            else 0.0, axis=1
        )
        adjusted_margin = (df_pandas["interest_revenue"] - adjusted_loss).sum()
        results.append({"scenario": f"+{increase}%", "total_net_margin": round(adjusted_margin, 2)})

    return pd.DataFrame(results)