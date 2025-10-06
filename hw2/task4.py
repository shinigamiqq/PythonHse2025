import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('loan_data.csv')

print("Первые 5 строк:")
print(data.head())

print(f"\nКолечество строк 9578 и столбцов 14\n")
print(data.info())

print(f"\nПропущенные значения")
print(data.isna())
print(data.isna().sum())

print(f"\nОписательная статистика по числовым столбцам")
print(data.describe())

print(f"\nСредняя процентная ставка по кредиту")
print(data["int.rate"].mean())

print(f"\nКоличество клиентов, соответствующие условиями кредита")
print(data["credit.policy"].count())

print(f"\nРазличие среднего логарифма дохода заемщиков, соотвествующих/несоотвествующих условиям выдачи кредитов")
mean_credit_ok = data[data["credit.policy"] == 1]["log.annual.inc"].mean()
mean_credit_not_ok = data[data["credit.policy"] == 0]["log.annual.inc"].mean()
print(mean_credit_ok)
print(mean_credit_not_ok)
print(f"\nРазница: {mean_credit_ok - mean_credit_not_ok}")

print(f"\nМедианный ежемесячный платеж")
print(data["installment"].median())

print(f"\nКоличество уникальных значений `not.fully.paid`")
print(data["not.fully.paid"].unique().__len__())

data["annual.inc"] = np.exp(data["log.annual.inc"])
print("\nПервые 5 строк после добавления annual.inc:")
print(data[["log.annual.inc", "annual.inc"]].head())

print(f"\nГруппировка по `credit.policty` и `not.fully.paid`")
print(data.groupby(by=["credit.policy", "not.fully.paid"]).agg(
    clients_count=("credit.policy", "count"),
    mean_installment=("installment", "mean"),
    median_installment=("installment", "median"),
    mean_annual_inc=("annual.inc", "mean")
))

print(f"\nТоп-10 клиентов по уровню дохода, которые не удовлетворяют условиям выдачи кредита")
print(data[data["credit.policy"] == 0].sort_values(by="annual.inc", ascending=False).head(10))

print(f"\nВыбросы переменной `annual.inc`")
Q1 = data["annual.inc"].quantile(0.25)
Q3 = data["annual.inc"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data[(data["annual.inc"] < lower_bound) | (data["annual.inc"] > upper_bound)]

print(f"Q1 = {Q1:.2f}")
print(f"Q3 = {Q3:.2f}")
print(f"IQR = {IQR:.2f}")
print(f"Нижняя граница = {lower_bound:.2f}")
print(f"Верхняя граница = {upper_bound:.2f}")
print(f"Количество выбросов: {len(outliers)}")

print(f"\nРаспределения переменных `annual.inc` и `log.annual.inc`")
plt.style.use("seaborn-v0_8-whitegrid")
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(data["annual.inc"], bins=40, kde=True, color="skyblue")
plt.title("Распределение годового дохода (annual.inc)")
plt.xlabel("annual.inc")
plt.ylabel("Количество клиентов")

plt.subplot(1, 2, 2)
sns.histplot(data["log.annual.inc"], bins=40, kde=True, color="salmon")
plt.title("Распределение логарифма годового дохода (log.annual.inc)")
plt.xlabel("log.annual.inc")
plt.ylabel("Количество клиентов")

plt.tight_layout()
plt.show()
