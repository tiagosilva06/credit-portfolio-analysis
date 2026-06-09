import matplotlib.pyplot as plt
import seaborn as sns

def plot_net_margin_by_safra(pl_safra_df):
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=pl_safra_df, x="safra", y="total_net_margin", marker="o", color="#2196F3")
    plt.title("Net Margin by Safra", fontsize=16, fontweight="bold")
    plt.xlabel("Safra", fontsize=12)
    plt.ylabel("Net Margin (R$)", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/net_margin_by_safra.png", dpi=150)
    plt.show()

def plot_default_rate_by_product(default_df):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=default_df, x="product", y="default_rate", palette="Reds_d")
    plt.title