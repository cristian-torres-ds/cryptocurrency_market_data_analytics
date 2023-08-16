import streamlit as st
import pandas as pd
import datetime as dt
from pycoingecko import CoinGeckoAPI
import seaborn as sns
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

# venv/Scripts/Activate.ps1
# streamlit run .\Introducción.py


st.markdown("# Selección de Criptomonedas")

st.markdown("""Para seleccionar estas 7 monedas de tipo Privacy y 3 de tipo Payment, nos vamos a enfocar enfrcar en su capitalización.

La capitalización es el valor total de todas las monedas en circulación, las criptomonedas con una alta capitalización de mercado suelen ser
más estables y tienen más liquidez.

Pienso que reducir la relación **"risk-reward"** en un mercado tan volatil, es importante, por eso nos vamos a enfocar en esta variable para
la elección de las 10 monedas a analizar.
""")

cg = CoinGeckoAPI()
cg.ping()

tipo = st.selectbox('Tipo de moneda', ('Privacy', 'Payment'))

if tipo == 'Privacy':

    st.markdown("### Privacy Cryptocurrencies")

    privacy_data_by_m_cap = pd.DataFrame(cg.get_coins_markets(vs_currency = 'usd', category = 'privacy-coins')).sort_values('market_cap', ascending=False)
    privacy_data_by_m_cap = privacy_data_by_m_cap[['id', 'name', 'current_price', 'market_cap', 'circulating_supply']]

    privacy_df = privacy_data_by_m_cap.head(7)

    name_list = privacy_df.name.tolist()
    id_list = privacy_df.id.tolist()

    st.write(f"Las mejor capitalizadas son: {name_list[0]}, {name_list[1]}, {name_list[2]}, {name_list[3]}, {name_list[4]}, {name_list[5]}, {name_list[6]}")

    st.markdown("---")

    # Barplot market cap Privacy
    fig = plt.figure(figsize=(6,4))
    sns.barplot(x = 'name', y = 'market_cap', data = privacy_df)
    plt.title("Capitalización Privacy Cryptocurrencies")
    plt.ylabel("Capitalización")
    st.pyplot(fig)

    st.markdown("---")

    # Pie plot Privacy
    resto_privacy = privacy_data_by_m_cap[['name', 'market_cap']][~(privacy_data_by_m_cap['name'].isin(name_list))] # el "~" transforma al is-in en un not-in
    privacy_con_resto = privacy_df[['name', 'market_cap']]
    privacy_con_resto.loc[len(privacy_con_resto.index), :] = ['Resto', resto_privacy['market_cap'].sum()]

    fig = plt.figure(figsize=(6,4))
    plt.pie(privacy_con_resto.market_cap, labels=privacy_con_resto.name, autopct='%.0f%%')
    plt.title("Porcentaje de mercado de monedas elegidas vs resto.")
    st.pyplot(fig)

    st.markdown("---")

    # Historial de capitalización
    id_tuple = tuple(id_list)

    moneda = st.selectbox('Moneda', id_tuple)

    daily_historical = cg.get_coin_market_chart_by_id(id=moneda, vs_currency='usd', days='max')
    daily_historical_data_frame = pd.DataFrame(data = daily_historical['prices'], columns = ['Date', 'Price'])
    daily_historical_data_frame['Date'] = pd.to_datetime(daily_historical_data_frame['Date'], unit='ms')
    daily_historical_data_frame = daily_historical_data_frame.set_index('Date')

    fig = plt.figure(figsize=(6,4))
    plt.plot(daily_historical_data_frame['Price'])
    plt.title(f"Precio histórico {moneda}")
    plt.ylabel("Precio en USD")
    plt.xticks(rotation=45)
    st.pyplot(fig)

else:
    st.markdown("### Payment Cryptocurrencies")

    payment_data_by_m_cap = pd.DataFrame(cg.get_coins_markets(vs_currency = 'usd', category = 'payment-solutions')).sort_values('market_cap', ascending=False)
    payment_data_by_m_cap = payment_data_by_m_cap[['id', 'name', 'current_price', 'market_cap', 'circulating_supply']]

    payment_df = payment_data_by_m_cap.head(3)

    name_list = payment_df.name.tolist()
    id_list = payment_df.id.tolist()

    st.write(f"Las mejor capitalizadas son: {name_list[0]}, {name_list[1]}, {name_list[2]}")

    st.markdown("---")

    # Barplot market cap Payment
    fig = plt.figure(figsize=(6,4))
    sns.barplot(x = 'name', y = 'market_cap', data = payment_df)
    plt.title("Capitalización Payment Cryptocurrencies")
    plt.ylabel("Capitalización")
    st.pyplot(fig)

    st.markdown("---")

    # Pie plot Payment
    resto_payment = payment_data_by_m_cap[['name', 'market_cap']][~(payment_data_by_m_cap['name'].isin(name_list))] # el "~" transforma al is-in en un not-in
    payment_con_resto = payment_df[['name', 'market_cap']]
    payment_con_resto.loc[len(payment_con_resto.index), :] = ['Resto', resto_payment['market_cap'].sum()]

    fig = plt.figure(figsize=(6,4))
    plt.pie(payment_con_resto.market_cap, labels=payment_con_resto.name, autopct='%.0f%%')
    plt.title("Porcentaje de mercado de monedas elegidas vs resto.")
    st.pyplot(fig)

    st.markdown("---")

    # Historial de capitalización
    id_tuple = tuple(id_list)

    moneda = st.selectbox('Moneda', id_tuple)

    daily_historical = cg.get_coin_market_chart_by_id(id=moneda, vs_currency='usd', days='max')
    daily_historical_data_frame = pd.DataFrame(data = daily_historical['prices'], columns = ['Date', 'Price'])
    daily_historical_data_frame['Date'] = pd.to_datetime(daily_historical_data_frame['Date'], unit='ms')
    daily_historical_data_frame = daily_historical_data_frame.set_index('Date')

    fig = plt.figure(figsize=(6,4))
    plt.plot(daily_historical_data_frame['Price'])
    plt.title(f"Precio histórico {moneda}")
    plt.ylabel("Precio en USD")
    plt.xticks(rotation=45)
    st.pyplot(fig)