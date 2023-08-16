import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
from pycoingecko import CoinGeckoAPI
import mplfinance as mpf
st.set_option('deprecation.showPyplotGlobalUse', False)

# venv/Scripts/Activate.ps1
# streamlit run .\Introducción.py

cg = CoinGeckoAPI()

st.markdown("# Análisis de Criptomonedas")

st.markdown("""Para analizar estas monedas vamos a utilizar las siguientes KPIs junto a un diagrama de velas:
1. Moving Averages.
2. Average True Range
3. Relative Strength Index
""")

# Obtenemos las listas de las mejor capitalizadas
privacy_data_by_m_cap = pd.DataFrame(cg.get_coins_markets(vs_currency = 'usd', category = 'privacy-coins')).sort_values('market_cap', ascending=False)
privacy_data_by_m_cap = privacy_data_by_m_cap[['id', 'name', 'current_price', 'market_cap', 'circulating_supply']]
privacy_df = privacy_data_by_m_cap.head(7)
privacy_name_list = privacy_df.name.tolist()
privacy_id_list = privacy_df.id.tolist()

payment_data_by_m_cap = pd.DataFrame(cg.get_coins_markets(vs_currency = 'usd', category = 'payment-solutions')).sort_values('market_cap', ascending=False)
payment_data_by_m_cap = payment_data_by_m_cap[['id', 'name', 'current_price', 'market_cap', 'circulating_supply']]
payment_df = payment_data_by_m_cap.head(3)
payment_name_list = payment_df.name.tolist()
payment_id_list = payment_df.id.tolist()

id_tuple = tuple(privacy_id_list + payment_id_list)

# selección de moneda
moneda = st.selectbox('Moneda: ', id_tuple)
dias = st.selectbox("Rango de días: ", ('180', '365'))

# Preparado del data frame según moneda elegida
# La granularidad es de 4 días para la versión gratuita de la API CoinGecko
ohlc_data = cg.get_coin_ohlc_by_id(id=moneda, vs_currency='usd', days=dias)
ohlc_data_frame = pd.DataFrame(data = ohlc_data, columns = ['Date', 'Open', 'High' ,'Low', 'Close'])
ohlc_data_frame['Date'] = ohlc_data_frame['Date'].apply(lambda x: dt.datetime.fromtimestamp(x/1000).strftime('%m-%d-%Y %H:%M:%S'))
ohlc_data_frame['Date'] = pd.to_datetime(ohlc_data_frame['Date'])
ohlc_data_frame = ohlc_data_frame.set_index('Date')



st.markdown("""## Moving Averages:
Las Moving Averages son una herramienta fundamental en el análisis técnico de los mercados financieros. Son utilizadas para suavizar las fluctuaciones
de los precios de los activos y ayudar a identificar tendencias.
""")

if st.checkbox('Mas info', key='1'):
    st.markdown("""Una media móvil se calcula tomando el promedio de un conjunto de precios durante un período de tiempo específico. A medida que
el tiempo avanza, la media "se mueve" al incluir nuevos precios y eliminar los más antiguos. Esto permite obtener una perspectiva más clara y suave 
de la evolución de los precios, lo que puede facilitar la identificación de patrones y tendencias.

Las medias móviles son útiles por varias razones:

1. **Identificación de tendencias**: Las medias móviles suavizan las fluctuaciones diarias, lo que permite ver más claramente si hay una tendencia alcista,
bajista o lateral en el mercado.

2. **Señales de compra y venta**: Los cruces entre diferentes medias móviles (por ejemplo, la cruz de una media móvil de corto plazo sobre una de largo plazo)
a menudo se consideran señales de compra o venta. Por ejemplo, cuando una media móvil de corto plazo cruza por encima de una de largo plazo, puede indicar un 
posible aumento en el precio.

3. **Soporte y resistencia dinámicos**: Las medias móviles también pueden actuar como niveles de soporte o resistencia, ayudando a determinar posibles puntos 
de entrada o salida en una posición.

4. **Filtrado de ruido**: En mercados volátiles, los precios pueden tener movimientos bruscos. Las medias móviles pueden ayudar a filtrar este ruido y
proporcionar una visión más clara de la tendencia.
""")

periodo = st.selectbox("Período: ", ('4', '8', '12'))

fig = mpf.plot(
        ohlc_data_frame,
        type='candle',
        mav=int(periodo),
        style='charles',
        title=f'{moneda.upper()} con MA',
        ylabel='Precio USD',
        )

st.pyplot(fig)

st.markdown('---')

st.markdown("""## Average True Range:
El ATR se utiliza principalmente para medir la volatilidad del precio de un activo financiero en un período de tiempo determinado. A diferencia de otros indicadores
que solo se basan en cambios de precios, el ATR también tiene en cuenta las brechas o gaps en los precios, lo que lo hace un indicador más completo para evaluar la
volatilidad real del mercado.
""")

if st.checkbox('Mas info', key='2'):
    st.markdown("""El cálculo del ATR implica varios pasos:

1. Calcula el rango verdadero (TR) para cada día:
   - TR = Max(Alta - Baja, |Alta - Cierre_previo|, |Baja - Cierre_previo|)

2. Calcula un promedio móvil exponencial (EMA) del TR durante un período de tiempo especificado. El valor típico es 14 días.

3. El valor resultante del EMA del TR es el ATR.

El ATR se expresa en la misma unidad que el precio del activo y se utiliza principalmente para:

1. **Evaluar la volatilidad**: Cuanto mayor sea el valor del ATR, mayor será la volatilidad percibida en el activo. Una alta volatilidad puede indicar movimientos de precios más amplios, lo que puede ser tanto una oportunidad como un riesgo, según el enfoque de inversión.

2. **Establecer niveles de stop-loss y take-profit**: Los traders e inversores utilizan el ATR para determinar niveles adecuados de stop-loss y take-profit. Un stop-loss ajustado a la volatilidad actual puede ayudar a proteger las ganancias y limitar las pérdidas en caso de movimientos bruscos.

3. **Identificar cambios en la volatilidad**: Un aumento repentino en el ATR puede indicar un cambio en la volatilidad y posiblemente el inicio de una tendencia o un movimiento importante en el mercado.

4. **Comparar la volatilidad entre activos**: El ATR permite comparar la volatilidad entre diferentes activos, lo que puede ser útil al decidir en qué activos invertir.
""")

# Agregado de comlumna ATR
def wwma(values, n):
    return values.ewm(alpha=1/n, adjust=False).mean()

def atr(df, n=14):
    data = df.copy()
    high = data['High']
    low = data['Low']
    close = data['Close']
    data['tr0'] = abs(high - low)
    data['tr1'] = abs(high - close.shift())
    data['tr2'] = abs(low - close.shift())
    tr = data[['tr0', 'tr1', 'tr2']].max(axis=1)
    atr = wwma(tr, n)
    return atr

ohlc_data_frame['ATR'] = atr(ohlc_data_frame)

atr = mpf.make_addplot(ohlc_data_frame["ATR"])

fig = mpf.plot(
            ohlc_data_frame,
            type='candle',
            figratio=(18,10),
            addplot = atr,
            style='charles',
            title=f"{moneda.upper()} con ATR",
            ylabel='Precio USD',
            )

st.pyplot(fig)

st.markdown('---')

st.markdown("""## Relative Strength Index:
Es un indicador técnico utilizado para evaluar la velocidad y el cambio de los movimientos de los precios.
""")

if st.checkbox('Mas info', key='3'):
    st.markdown("""Fue desarrollado por J. Welles Wilder en la década de 1970 y se considera uno de los indicadores más populares y efectivos.

El RSI es un oscilador que oscila entre 0 y 100 y se calcula utilizando la siguiente fórmula básica:

RSI = 100 - (100 / (1 + RS))

Donde: RS (Relative Strength) es la relación entre el promedio de ganancias durante un período determinado y el promedio de pérdidas durante ese mismo período.
Se calcula de la siguiente manera:

RS = Promedio de ganancias / Promedio de pérdidas

El RSI se utiliza para:

1. **Identificar condiciones de sobrecompra y sobreventa**: El RSI se utiliza a menudo para identificar cuándo un activo financiero está sobrecomprado
(RSI por encima de cierto umbral, como 70) o sobrevendido (RSI por debajo de cierto umbral, como 30). Estas condiciones extremas pueden indicar posibles
puntos de reversión en el precio.

2. **Confirmar tendencias**: El RSI puede ayudar a confirmar la dirección de la tendencia en el mercado. Por ejemplo, en una tendencia alcista, los
valores del RSI que se mantienen principalmente por encima de 50 pueden indicar que la tendencia alcista tiene impulso.

3. **Divergencias**: Las divergencias entre el RSI y el precio pueden señalar posibles cambios en la dirección del precio. Por ejemplo, si el precio
alcanza un nuevo máximo pero el RSI no sigue, podría indicar una debilidad en la tendencia alcista.

4. **Evaluación de fuerza y momentum**: El RSI mide la velocidad y magnitud de los movimientos de los precios. Un RSI alto puede indicar un impulso
alcista fuerte, mientras que un RSI bajo puede señalar un impulso bajista.

5. **Establecimiento de stop-loss y take-profit**: Los traders pueden usar los niveles de sobrecompra y sobreventa del RSI para determinar niveles
adecuados de stop-loss y take-profit.

Es importante destacar que, aunque el RSI es una herramienta valiosa, no es infalible y debe usarse en conjunto con otras formas de análisis y
consideraciones. Además, el RSI puede dar señales falsas en mercados especialmente volátiles. Siempre es recomendable realizar un análisis integral
y utilizar múltiples indicadores y enfoques antes de tomar decisiones comerciales basadas en el RSI.
""")

# Agregado de RSI
ohlc_data_frame['change'] = ohlc_data_frame['Close'].diff()
ohlc_data_frame['gain'] = ohlc_data_frame.change.mask(ohlc_data_frame.change < 0, 0.0)
ohlc_data_frame['loss'] = -ohlc_data_frame.change.mask(ohlc_data_frame.change > 0, -0.0)

def rma(x, n):
    """Running moving average"""
    a = np.full_like(x, np.nan)
    a[n] = x[1:n+1].mean()
    for i in range(n+1, len(x)):
        a[i] = (a[i-1] * (n - 1) + x[i]) / n
    return a

ohlc_data_frame['avg_gain'] = rma(ohlc_data_frame.gain.to_numpy(), 14)
ohlc_data_frame['avg_loss'] = rma(ohlc_data_frame.loss.to_numpy(), 14)

ohlc_data_frame['rs'] = ohlc_data_frame.avg_gain / ohlc_data_frame.avg_loss
ohlc_data_frame['RSI'] = 100 - (100 / (1 + ohlc_data_frame.rs))
ohlc_data_frame = ohlc_data_frame.drop(['change', 'gain', 'loss', 'avg_gain', 'avg_loss', 'rs'], axis=1)

rsi = mpf.make_addplot(ohlc_data_frame["RSI"])

fig = mpf.plot(
            ohlc_data_frame,
            type='candle',
            figratio=(18,10),
            addplot = rsi,
            style='charles',
            title=f"{moneda.upper()} con RSI",
            ylabel='Precio USD',
            )

st.pyplot(fig)