from pyspark.sql.functions import col, when, round as spark_round
import pandas as pd

def apply_spark_transformations(df):
    df = df.withColumn(
        "interest_revenue",
        spark_round(col("granted_amount") * col("interest_rate") * 12, 2)
    ).withColumn(
        "expected_loss",
        spark_round(
            when(col("payment_status") == "Inadimplente", col("granted_amount") * 0.80)
            .when(col("payment_status") == "Parcialmente Inadimplente", col("granted_amount") * 0.40)
            .otherwise(0.0), 2
        )
    ).withColumn(
        "net_margin",
        spark_round(col("interest_revenue") - col("expected_loss"), 2)
    )
    return df

def apply_pandas_transformations(df_pandas):
    df_pandas["interest_revenue"] = round(df_pandas["granted_amount"] * df_pandas["interest_rate"] * 12, 2)

    df_pandas["expected_loss"] = df_pandas.apply