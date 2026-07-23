import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

params = {
    "vs_currency": "usd",
    "days": 365
}

response = requests.get(url, params=params)
dados = response.json()

print(dados)

##criando dataframe

df = pd.DataFrame(
    dados["prices"],
    columns=["timestamp", "price"]
)

##converter o timestamp

df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

print(df.head())
print(df.tail())


#preço maximo do bitcoin nos últimos 365 dias
df["price"].max()
print("Preço máximo:", df["price"].max())

#preço minimo do bitcoin nos últimos 365 dias
df["price"].min()
print("Preço mínimo:", df["price"].min())

#qual data foi o mairo preço do bitcoin nos últimos 365 dias
indice = df["price"].idxmax()
print("Data do preço máximo:", df.loc[indice, "timestamp"])

#qual data foi o menor preço do bitcoin nos últimos 365 dias
indice_min = df["price"].idxmin()
print("Data do preço mínimo:", df.loc[indice_min, "timestamp"])

plt.figure(figsize=(12,6))

plt.plot(
    df["timestamp"],
    df["price"]
)

plt.title("Preço do Bitcoin - Últimos 365 dias")
plt.xlabel("Data")
plt.ylabel("Preço em USD")

plt.grid(True)

plt.xticks(rotation=45)

plt.savefig("bitcoin_grafico.png")