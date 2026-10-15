import pandas as pd

df = pd.read_excel(r"D:\data analytics\archive (2)\Telco_customer_churn.xlsx")

print("shape:",df.shape)

print("\n Columns:")
print(df.columns.tolist())


print("\nFirst 5 Rows:")
print(df.head())

print("\n Data types:")
print(df.dtypes)


print("\n Missing Values:")
print(df.isnull().sum())


print("\n Duplicate Rows:")
print(df.duplicated().sum())

print("\n Unique Values:")
print(df.nunique())

print("\nBlank Total Charges:")
print((df["Total Charges"].str.strip() == "").sum())

print("\nTotal Charges Data Type:")
print(df["Total Charges"].dtype)

print("\nSample Total Charges:")
print(df["Total Charges"].head(10))


print("\nCustomers with Blank Total Charges:")

print(
    df[df["Total Charges"].str.strip() == ""]
    [["CustomerID", "Tenure Months", "Monthly Charges", "Total Charges", "Churn Label"]]
)


print("\nColumn Summary:")
print(df.info())


df = df.drop(columns=["Count", "Country", "State"])

print("\nShape after removing unnecessary columns:")
print(df.shape)

print("\nRemaining Columns:")
print(df.columns.tolist())




df["Total Charges"] = pd.to_numeric(
    df["Total Charges"],
    errors="coerce"
)

print("\nTotal Charges Data Type:")
print(df["Total Charges"].dtype)

print("\nMissing Total Charges:")
print(df["Total Charges"].isnull().sum())


df["Total Charges"] = df["Total Charges"].fillna(0)

print("Missing Total Charges after filling:")
print(df["Total Charges"].isnull().sum())



print("\nChurn Distribution:")
print(df["Churn Label"].value_counts())

print("\nChurn Percentage:")
print(df["Churn Label"].value_counts(normalize=True) * 100)


contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn Label"],
    normalize="index"
) * 100

print("\nChurn Rate by Contract Type:")
print(contract_churn.round(2))


internet_churn = pd.crosstab(
    df["Internet Service"],
    df["Churn Label"],
    normalize="index"
) * 100

print("\nChurn Rate by Internet Service:")
print(internet_churn.round(2))


df["Tenure Group"] = pd.cut(
    df["Tenure Months"],
    bins=[-1, 12, 36, float("inf")],
    labels=["New (0-12)", "Mid-term (13-36)", "Long-term (37+)"]
)

tenure_churn = pd.crosstab(
    df["Tenure Group"],
    df["Churn Label"],
    normalize="index"
) * 100

print("\nChurn Rate by Tenure Group:")
print(tenure_churn.round(2))


payment_churn = pd.crosstab(
    df["Payment Method"],
    df["Churn Label"],
    normalize="index"
) * 100

print("\nChurn Rate by Payment Method:")
print(payment_churn.round(2))



df["Monthly Charges Group"] = pd.cut(
    df["Monthly Charges"],
    bins=[0, 50, 80, float("inf")],
    labels=["Low (<$50)", "Medium ($50-$80)", "High (>$80)"]
)

monthly_churn = pd.crosstab(
    df["Monthly Charges Group"],
    df["Churn Label"],
    normalize="index"
) * 100

print("\nChurn Rate by Monthly Charges:")
print(monthly_churn.round(2))

tech_support_churn = pd.crosstab(
    df["Tech Support"],
    df["Churn Label"],
    normalize="index"
) * 100

print("\nChurn Rate by Tech Support:")
print(tech_support_churn.round(2))

segment_churn = pd.crosstab(
    [df["Contract"], df["Tech Support"]],
    df["Churn Label"],
    normalize="index"
) * 100

print("\nChurn Rate by Contract and Tech Support:")
print(segment_churn.round(2))



churn_reasons = df[df["Churn Label"] == "Yes"]["Churn Reason"].value_counts()

print("\nTop Churn Reasons:")
print(churn_reasons)


senior_churn = pd.crosstab(
    df["Senior Citizen"],
    df["Churn Label"],
    normalize="index"
) * 100

print("\nChurn Rate by Senior Citizen:")
print(senior_churn.round(2))


partner_churn = pd.crosstab(
    df["Partner"],
    df["Churn Label"],
    normalize="index"
) * 100

print("\nChurn Rate by Partner:")
print(partner_churn.round(2))


dependents_churn = pd.crosstab(
    df["Dependents"],
    df["Churn Label"],
    normalize="index"
) * 100

print("\nChurn Rate by Dependents:")
print(dependents_churn.round(2))



gender_churn = pd.crosstab(
    df["Gender"],
    df["Churn Label"],
    normalize="index"
) * 100

print("\nChurn Rate by Gender:")
print(gender_churn.round(2))


df.to_csv("telco_churn_cleaned.csv", index=False)

print("Cleaned dataset exported successfully!")