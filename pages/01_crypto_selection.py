import streamlit as st
import pandas as pd
import datetime as dt
from pycoingecko import CoinGeckoAPI
import seaborn as sns
import matplotlib.pyplot as plt


cg = CoinGeckoAPI()

cg.ping()

privacy_data_by_m_cap = pd.DataFrame(cg.get_coins_markets(vs_currency = 'usd', category = 'privacy-coins')).sort_values('market_cap', ascending=False)
privacy_data_by_m_cap = privacy_data_by_m_cap[['name', 'current_price', 'market_cap', 'circulating_supply']]
payment_data_by_m_cap = pd.DataFrame(cg.get_coins_markets(vs_currency = 'usd', category = 'payment-solutions')).sort_values('market_cap', ascending=False)
payment_data_by_m_cap = payment_data_by_m_cap[['name', 'current_price', 'market_cap', 'circulating_supply']]

privacy_df = privacy_data_by_m_cap.head(5)
payment_df = payment_data_by_m_cap.head(5)

privacy_list = privacy_df.name.tolist()
payment_list = payment_df.name.tolist()

st.markdown('Capitalización Privacy Cryptocurrencies')

fig = plt.figure(figsize=(6,4))
sns.barplot(x = 'name', y = 'market_cap', data = privacy_df)
plt.title("Capitalización Privacy Cryptocurrency")
plt.ylabel("Capitalización")
st.pyplot(fig)



resto_privacy = privacy_data_by_m_cap[['name', 'market_cap']][~(privacy_data_by_m_cap['name'].isin(privacy_list))] # el "~" transforma al is-in en un not-in

privacy_con_resto = privacy_df[['name', 'market_cap']]

privacy_con_resto.loc[len(privacy_con_resto.index)] = ['Resto', resto_privacy['market_cap'].sum()]

fig = plt.figure(figsize=(6,4))
plt.pie(privacy_con_resto.market_cap, labels=privacy_con_resto.name, autopct='%.0f%%')
st.pyplot(fig)

daily_historical = cg.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency = 'usd', days = 'max')

daily_historical_data_frame = pd.DataFrame(data = daily_historical['prices'], columns = ['Date', 'Price'])

daily_historical_data_frame['Date'] = daily_historical_data_frame['Date'].apply(lambda x: dt.datetime.fromtimestamp(x/1000).strftime('%m-%d-%Y'))

daily_historical_data_frame = daily_historical_data_frame.set_index('Date')

daily_historical_data_frame['Price'].plot()


fig = plt.figure(figsize=(6,4))
sns.barplot(x = 'name', y = 'current_price', data = privacy_df)
plt.title("Precio actual Privacy Cryptocurrency")
plt.ylabel("Precio actual")
st.pyplot(fig)

fig = plt.figure(figsize=(6,4))
sns.barplot(x = 'name', y = 'market_cap', data = payment_df)
plt.title("Capitalización Payment Cryptocurrency")
plt.ylabel("Capitalización")
st.pyplot(fig)


resto_payment = payment_data_by_m_cap[['name', 'market_cap']][~(payment_data_by_m_cap['name'].isin(payment_list))]
payment_con_resto = payment_df[['name', 'market_cap']]

payment_con_resto.loc[len(payment_con_resto.index)] = ['Resto', resto_payment['market_cap'].sum()]

fig = plt.figure(figsize=(6,4))
plt.pie(payment_con_resto.market_cap, labels=payment_con_resto.name, autopct='%.0f%%')
st.pyplot(fig)