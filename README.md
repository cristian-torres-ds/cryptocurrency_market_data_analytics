<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº2** </h1>
# <h1 align=center> Cristian Gabriel Torres </h1>

# <h1 align=center>**`Cryptocurrency Market Data Analytics`**</h1>


¡Bienvenidos a mi último proyecto individual de la etapa de labs! En esta ocasión, debo hacer un trabajo situándome en el rol de un ***Data Analyst***.

<p align='center'>
<img src = 'https://www.clarin.com/img/2023/06/14/WJlAYJhAg_360x240__1.jpg' height = 200>
<p>


## **Descripción del problema -contexto y rol a desarrollar-**

### **Contexto**

En los últimos años, el mercado de las criptomonedas ha experimentado un crecimiento exponencial y una creciente adopción a nivel mundial. La aparición del Bitcoin en 2009 marcó el inicio de una revolución financiera que ha llevado a la creación de miles de criptomonedas diferentes con diversas funcionalidades y tecnologías subyacentes.

Con el aumento del interés en el mercado de criptomonedas, cada vez más inversores, empresas y entusiastas buscan comprender mejor el comportamiento y la evolución de estos activos digitales. Sin embargo, la naturaleza altamente volátil y compleja de las criptomonedas presenta desafíos significativos para aquellos que desean tomar decisiones informadas sobre inversiones o simplemente para comprender mejor cómo funcionan estos mercados emergentes.

El análisis y la exploración de datos desempeñan un papel crucial en la obtención de información valiosa dentro del vasto conjunto de datos disponibles sobre criptomonedas. En este contexto, es clave el uso de una valiosa fuente de datos actualizados que proporcionen información sobre una amplia variedad de criptomonedas, incluidos precios, volúmenes de negociación, capitalización de mercado, información histórica y más.


### **Rol a desarrollar**

Te sitúas en el puesto de Analista de Datos en una empresa de servicios financieros que se ha interesado en el mercado de criptomonedas debido a su crecimiento exponencial y el potencial de oportunidades de inversión para los clientes. La empresa te ha asignado la tarea de realizar un análisis exhaustivo utilizando datos de la API CoinGecko para entender mejor el mercado de criptomonedas y presentar tus hallazgos y recomendaciones en un informe detallado.

La fuente de información entregada por la empresa posee un conjunto de aproximadamente 4000 monedas y el tiempo estipulado para obtener tus análisis es corto, por lo que se te ha solicitado que acotes tu trabajo en al menos 10 criptomonedas, y en base a estas presentes tus análisis y recomendaciones.

Considera además que la elección de estas monedas queda a tu criterio, pero debes dejar claro el porqué de tu elección y el sustento de ésta. Por ejemplo, podrías seleccionar las criptomonedas con mayor capitalización de mercado, aquellas que han experimentado un mayor crecimiento reciente, o incluso algunas que son innovadoras en términos de tecnología o caso de uso.

Por último, asegúrate de destacar el impacto y las recomendaciones basadas en los resultados del análisis. Estos podrían incluir posibles estrategias u oportunidades de inversión, la gestión del riesgo, optimización de la cartera, sugerencias sobre cómo seguir monitoreando el mercado de criptomonedas, entre otros.

---

#### Acotación: Todo lo explicado en las siguientes líneas se puede ver mas completo y de forma interactiva en el [deploy](dufbasnfkjnasnfsanfnlkñsanflkñnakñsjnfkñjsanfksñjnasn).

## **EDA (Exploratory Data Analysis)**

Dada la gran cantidad de criptomonedas en el mercado, lo primero que se hizo fue investigar las principales categorías, para informarnos y poder ir enfocándonos en las que más atractivas nos parecen.

En el [notebook introducción](https://github.com/cristian-torres-ds/henry_proyecto_individual_2/blob/main/Introducci%C3%B3n.ipynb) se explican con palabras propias algunas de las principales categorías de criptomonedas y por que decidimos elegir las de tipo Payment y Privacy.


## **KPIs (Key Performance Indicator)**

En el [notebook selección de cripto](https://github.com/cristian-torres-ds/henry_proyecto_individual_2/blob/main/1_crypto_selection.ipynb) explicamos por que usamos Capitalización (Market Cap) para seleccionar las 10 monedas.

En el [notebook análisis de cripto](https://github.com/cristian-torres-ds/henry_proyecto_individual_2/blob/main/2_crypto_analysis.ipynb) investigamos las monedas seleccionadas y vemos si es conveniente invertir en ellas, vamos a usar un gráfico de velas, que es fundamental para poder hacer un primer anális, al que le vamos a complementar con las siguientes KPIs:

1. Moving Averages: Son una herramienta fundamental en el análisis técnico de los mercados financieros. Son utilizadas para suavizar las fluctuaciones de los precios de los activos y ayudar a identificar tendencias.

2. Average True Range: Se utiliza principalmente para medir la volatilidad del precio de un activo financiero en un período de tiempo determinado. A diferencia de otros indicadores que solo se basan en cambios de precios, el ATR también tiene en cuenta las brechas o gaps en los precios, lo que lo hace un indicador más completo para evaluar la volatilidad real del mercado.

3. Relative Strength Index: Es un indicador técnico utilizado para evaluar la velocidad y el cambio de los movimientos de los precios.

En el notebook solo está anilizada una moneda, en el [Deploy](jkdsakgbkjsdñkg) se puede interactuar y ver las KPIs de todas las monedas en tiempo real, así como también hay una explicación detallada complementaria de cada uno de los KPIs.


## **Conclusión Personal**

Bueno, me hubiera gustado terminar este README recomendando alguna de las 10 criptomonedas elegidas.

Pero despues de analizar exhaustivamente cada una de las monedas llegué a la conclusión de que están todas con una tendencia negativa, por lo que no podría recomendar invertir en ninguna de ellas.

Tal vez alguien experto en el tema podría ver algo que yo no.

Quisiera aclarar que traté de elegir tipos de monedas que me parecieron interesante, tratando de alejarme de las más populares. 

Pero el lado positivo es que el código está bastante prolijo y facilmente se podría modificar para analizar otras monedas a parte de las que elegí.

Saludos!!!