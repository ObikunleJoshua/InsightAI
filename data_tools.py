import pandas as pd

def generate_dataset_summary(df):

    summary = {}

    summary["rows"] = df.shape[0]
    summary["columns"] = df.shape[1]

    summary["column_names"] = list(df.columns)

    summary["missing_values"] = int(df.isnull().sum().sum())

    if "Sales" in df.columns:
        summary["total_sales"] = round(df["Sales"].sum(), 2)
        summary["average_sales"] = round(df["Sales"].mean(), 2)

    if "Profit" in df.columns:
        summary["total_profit"] = round(df["Profit"].sum(), 2)
        summary["average_profit"] = round(df["Profit"].mean(), 2)

    if "Region" in df.columns and "Sales" in df.columns:
        summary["top_regions"] = (
            df.groupby("Region")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
            .to_dict()
        )

    if "Category" in df.columns and "Sales" in df.columns:
        summary["top_categories"] = (
            df.groupby("Category")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .to_dict()
        )

    return summary