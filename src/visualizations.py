import matplotlib.pyplot as plt
import seaborn as sns
import os

DATA_DIR = r'C:\Tiago\data engineer\Projetos\credit-portfolio-analysis\data'

def plot_net_margin_by_safra(pl_safra_df):
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=pl_safra_df, x="safra", y="total_net_margin", marker="o", color="#2196F3")
    plt.title("Net Margin by Safra", fontsize=16, fontweight="bold")
    plt.xlabel("Safra", fontsize=12)
    plt.ylabel("Net Margin (R$)", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(DATA_DIR, "net_margin_by_safra.png"), dpi=150)
    plt.show()

def plot_default_rate_by_product(default_df):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=default_df, x="product", y="default_rate", palette="Reds_d")
    plt.title("Default Rate by Product (%)", fontsize=16, fontweight="bold")
    plt.xlabel("Product", fontsize=12)
    plt.ylabel("Default Rate (%)", fontsize=12)
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(os.path.join(DATA_DIR, "default_rate_by_product.png"), dpi=150)
    plt.show()

def plot_sensitivity_analysis(sensitivity_df):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=sensitivity_df, x="scenario", y="total_net_margin", palette="RdYlGn_r")
    plt.title("Sensitivity Analysis - Net Margin vs Default Rate Increase", fontsize=14, fontweight="bold")
    plt.xlabel("Default Rate Increase", fontsize=12)
    plt.ylabel("Total Net Margin (R$)", fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(DATA_DIR, "sensitivity_analysis.png"), dpi=150)
    plt.show()