```markdown
# Technical Specifications: Cross-Asset Signal Pair Portfolio Analyzer (Streamlit App)

## Overview

This Streamlit application allows users to explore the performance of signal-driven pair portfolios, focusing on the decomposition of returns into their constituent elements as described in the research paper "Investment Base Pairs".  The app uses a synthetic dataset mimicking real-world financial data to demonstrate key drivers of pair portfolio performance.  It's designed for finance professionals, researchers, and students interested in portfolio construction and asset pricing.


## Step-by-Step Generation Process

**1. Data Loading and Preprocessing:**

*   Load the synthetic dataset into a Pandas DataFrame.  The dataset should contain columns representing asset classes (equities, bonds, currencies, commodities), signal types (value, momentum, carry), average returns, volatility, Sharpe ratios, and the five key drivers of pair portfolio performance (own-asset predictability, cross-asset predictability, signal correlation, signal mean imbalance, signal variance imbalance) as well as the unexplained effect.
*   Implement data cleaning and preprocessing steps as needed (e.g., handling missing values, outlier detection and treatment, data type conversions).

**2. User Interface Design (Streamlit):**

*   Use Streamlit's `st.sidebar` to create a user-friendly input section.
*   Include `st.selectbox` widgets for asset class, signal type selection.
*   Use `st.slider` widgets to allow users to adjust selectivity levels for portfolio construction (e.g., top x% of pairs).
*   Implement data filtering capabilities using `st.text_input` for searching and `st.number_input` to set numerical filters.
*   Use `st.markdown` to provide clear explanations and descriptions of the input parameters and the application's functionality.  Include inline documentation and tooltips.

**3. Data Processing and Calculation:**

*   Based on user selections from the sidebar widgets, filter and subset the dataset.
*   Calculate relevant performance metrics (average returns, volatility, Sharpe ratios) for selected portfolios.  This will require using appropriate financial functions (e.g., calculating Sharpe ratio).
*   Create a summary DataFrame containing these calculations for display.

**4. Visualization (Plotly):**

*   Utilize Plotly to create interactive charts.
*   Generate line charts to display trends in average returns, volatility, and Sharpe ratios over time for selected portfolios.
*   Generate bar charts to compare performance metrics (average return, volatility, sharpe ratio) across different asset classes and signal types.
*   Generate scatter plots to show the relationship between the key drivers and pair portfolio performance.
*   Use Plotly's annotation features to add explanations to charts, and hover tooltips to provide detailed data points when mousing over chart components.

**5. Output and Display (Streamlit):**

*   Use Streamlit's `st.dataframe` to display the summary DataFrame.
*   Use Streamlit's `st.plotly_chart` to display the interactive charts.
*   Ensure that visualizations update dynamically in real-time as users adjust input parameters.

**6.  Concept Explanation:**

*   Use `st.markdown` to clearly explain the decomposition of pair strategy returns into their constituent elements (own-asset predictability, cross-asset predictability, etc.). Emphasize how this visualization clarifies the heterogeneous drivers of pair strategy portfolio performance and illustrates the paper's key insight of utilizing base pairs for portfolio construction.  Provide references to relevant sections in the paper "Investment Base Pairs" where appropriate.

## Important Definitions, Examples, and Formulae

*   **Sharpe Ratio:**  A measure of risk-adjusted return, calculated as (Rp - Rf) / σp, where Rp is the portfolio return, Rf is the risk-free rate, and σp is the portfolio standard deviation.
*   **Selectivity:** The percentage of top-performing signal pairs included in the portfolio.  For example, a selectivity of 10% would only include the top 10% of pairs based on a relevant metric (e.g., predicted return, Sharpe ratio).
*   **Five Key Drivers of Pair Portfolio Performance:** The paper "Investment Base Pairs" details five key drivers; these are included in the synthetic dataset and used for visualization.  Definitions and further explanation should come from the paper.

## Libraries and Tools

*   **Streamlit:**  For building the interactive web application.
*   **Pandas:** For data manipulation and analysis.
*   **Plotly:** For creating interactive charts and visualizations.
*   **NumPy:**  For numerical operations.


```


### Appendix Code

```code
Table A.1: Equity Index Futures
Return (%)
Value
Mom. (×100)
Carry (×100)
Equity Future
Avg. SD N Avg SD N Avg. SD N Avg. SD N
AEX-Index
0.5 6.2 334 -0.1 1.4 294 0.5 2.0 322 0.1 0.5 294
ASX 200
0.4 3.9 280 0.1 1.4 243 0.4 1.2 268 0.2 0.3 243
CAC 40
0.6 5.4 317 0.2 1.3 233 0.6 1.8 305 0.1 0.5 309
DAX
0.6 5.8 394 0.0 1.4 281 0.6 1.8 382 -0.2 0.4 309
Euro Stoxx 50
0.4 5.3 298 0.2 1.3 221 0.3 1.7 286 0.2 0.4 259
FTSE 100
0.4 4.4 465 0.1 1.4 224 0.4 1.2 453 0.1 0.4 309
FTSE MIB
0.4 6.0 232 0.3 1.4 194 0.4 1.9 220 0.2 0.4 194
HANG SENG
0.4 6.2 272 0.2 1.3 309 0.5 1.7 260 0.2 0.7 309
NIKKEI 225
0.2 6.0 420 0.2 1.2 246 0.2 1.8 408 0.1 0.2 290
Nasdaq 100 E-Mini
0.8 6.9 291 0.1 1.3 237 0.7 2.2 279 -0.1 0.1 255
OMX Stockholm 30
0.8 4.8 223 -0.2 1.2 185 0.8 1.5 211 0.2 0.5 185
Russell 2000 E-Mini
0.5 5.5 267 -0.2 1.3 230 0.6 1.6 255 0.0 0.7 230
S&P 500
0.5 4.5 312 0.1 1.4 277 0.5 1.4 300 0.0 0.2 277
Swiss Market Index
0.4 4.0 300 0.4 1.4 288 0.2 0.4 297 0.5 1.2 261
TSX 60
0.4 3.9 273 0.2 1.3 250 0.5 1.2 261 0.1 0.1 250
Notes: Returns are signals are monthly. Value is the earnings/price ratio (3-year z-score); momentum is the
average trailing 12-month return; and carry is the futures roll (spot minus first).

Table A.2: Bond Futures
Return (%)
Value (×100)
Mom. (×100)
Carry (×100)
Bond Future
Avg. SD N Avg SD N Avg. SD N Avg. SD N
Australia 10Υ
0.2 2.3 465 0.3 0.2 308 0.3 0.7 452 0.1 0.1 308
Canada 10Υ
0.2 1.8 408 0.2 0.2 308 0.3 0.5 395 0.2 0.2 308
Euro Bobl
0.2 0.9 378 0.1 0.4 308 0.2 0.3 365 0.3 0.2 308
Euro Schatz
0.0 0.4 294 0.1 1.0 307 0.0 0.1 281 0.2 0.3 307
France 10Υ
0.2 1.9 137 0.0 0.1 126 0.2 0.6 124 0.3 0.1 126
GB 10Y
0.2 2.2 465 0.1 0.2 308 0.2 0.6 452 0.1 0.2 308
Germany 10Y
0.2 1.6 297 0.1 0.2 308 0.2 0.5 284 0.2 0.1 308
Italy 10Y
0.4 2.7 167 0.2 0.1 157 0.4 0.9 154 0.5 0.2 157
Japan 10Y
0.2 1.4 455 0.1 0.1 308 0.2 0.4 442 0.2 0.1 308
SFE 3Yr
0.0 0.7 264 0.4 0.6 253 0.1 0.2 251 0.1 0.3 253
US 10Y
0.3 1.8 465 0.1 0.2 308 0.3 0.6 452 0.3 0.2 308
US 2Y
0.1 0.5 399 0.0 0.9 308 0.1 0.2 386 0.4 0.5 308
US 5Y
0.2 1.2 424 0.1 0.3 308 0.2 0.4 411 0.4 0.3 308
Notes: Returns are signals are monthly. Value is the real yield; momentum is the average trailing 12-month
return; and carry is the excess yield plus term-structure roll.

Table A.3: Currency Forwards
Return (%)
Value
Mom. (×100)
Carry (×100)
1M Currency Forward
Avg. SD N Avg SD N Avg. SD N Avg. SD N
AUSDollar/USD
0.0 3.4 465 0.1 1.5 305 0.1 1.0 453 0.1 0.2 309
GBPound/USD
-0.2 2.7 417 -0.1 1.4 305 -0.2 0.9 405 0.0 0.1 309
CANDollar/USD
0.0 2.2 417 -0.3 1.5 305 0.0 0.6 405 -0.1 0.1 309
Euro/USD
-0.1 2.7 297 0.1 1.4 302 0.0 0.9 285 -0.1 0.1 309
JAPYenUSD
-0.2 3.0 417 -0.2 1.4 305 -0.1 0.9 405 -0.1 0.1 261
NZDollar/USD
0.1 3.3 417 0.2 1.4 305 0.2 1.0 405 0.2 0.2 309
NORKrone/USD
0.0 3.3 417 0.0 1.4 305 0.0 1.0 405 0.1 0.2 309
SWEKrona/USD
0.0 3.2 417 0.0 1.3 305 0.0 1.0 405 0.1 0.2 309
Swiss Franc/USD
0.0 3.0 417 0.1 1.4 305 0.0 1.0 405 0.0 0.1 309
Notes: Returns are signals are monthly. Value is the 5-year real exchange rate reversal (3-year z-score);
momentum is the average trailing 12-month return; and carry is the cash rate differential.

Table A.4: Commodity Futures
Return (%)
Value
Mom. (×100)
Carry (×100)
Commodity Future
Avg. SD N Avg SD N Avg. SD N Avg. SD N
Aluminum
-0.1 5.7 314 -0.2 0.4 249 0.0 1.9 302 -0.3 0.4 277
Blendstock Gasoline
1.4 10.2 465 -0.4 0.7 309 1.3 2.9 453 0.4 3.6 309
Cocoa
-0.1 7.9 465 -0.2 0.4 309 -0.2 2.0 453 -0.2 0.8 309
Coffee
-0.1 10.3 465 -0.2 0.6 309 -0.1 3.3 453 -0.8 0.8 309
Copper
0.9 7.6 453 -0.5 1.1 309 0.9 2.6 441 -0.1 0.5 309
Corn
-0.2 7.4 465 -0.2 0.6 309 -0.2 2.1 453 -0.7 1.7 309
Cotton
0.3 7.4 465 -0.1 0.4 309 0.3 2.5 453 -0.5 1.4 309
Crude Oil, Brent
1.0 9.2 410 -0.5 0.8 309 0.9 3.1 398 0.0 1.4 309
Feeder Cattle
0.2 4.1 465 -0.2 0.3 309 0.2 1.2 453 -0.3 1.1 309
Gold
0.2 4.4 465 -0.5 0.6 309 0.2 1.2 453 -0.2 0.2 309
Heating Oil
0.9 9.3 465 -0.5 0.8 309 0.8 3.1 453 -0.1 1.9 309
Kansas Wheat
0.0 7.5 465 -0.2 0.5 309 0.1 2.2 453 -0.7 0.8 309
Lead
0.9 8.2 274 -0.7 1.4 209 0.9 2.7 262 0.0 0.5 273
Lean Hogs
-0.2 7.2 465 -0.1 0.3 309 -0.2 2.2 453 -0.7 5.0 309
Live Cattle
0.2 3.9 465 -0.2 0.2 309 0.2 1.1 453 -0.1 0.3 309
Low Sulphur Gasoil
1.0 9.2 447 -0.5 0.8 309 0.9 3.1 435 -0.3 1.7 309
Natural Gas
-0.7 14.3 401 -0.3 0.8 309 -0.5 4.5 389 -2.1 4.6 309
Nickel
0.8 10.1 314 -0.6 1.3 249 1.0 3.4 302 0.0 1.5 309
Platinum
0.4 6.4 465 -0.3 0.6 309 0.4 1.8 453 0.0 0.3 309
Silver
0.3 8.0 465 -0.5 0.8 309 0.3 2.1 453 -0.2 0.1 309
Soybean Meal
0.8 7.2 465 -0.2 0.4 309 0.8 1.8 453 0.3 1.3 309
Soybean Oil
0.1 7.2 465 -0.2 0.6 309 0.1 2.2 453 -0.1 1.2 309
Soybeans
0.4 6.4 465 -0.2 0.5 309 0.4 1.8 453 -0.2 1.2 309
Sugar
0.6 9.4 465 -0.2 0.6 309 0.6 2.6 453 -0.1 0.4 309
WTI Crude
0.8 10.4 465 -0.4 0.7 309 0.8 3.2 453 -0.4 2.1 309
Wheat
0.6 9.0 465 -0.2 0.5 309 0.6 2.6 453 -0.4 1.1 309
Zinc
-0.3 7.6 314 -0.5 0.9 249 0.3 2.7 302 -0.2 0.4 277
Notes: Returns are signals are monthly. Value is the 5-year price reversal; momentum is the average trailing
12-month return; and carry is the futures roll (first minus second).

Avg(rij)t = a + Blij,t + Eij,t,

r = ∑i=1 Wiri

rij = sign(xi - xj) · (ri - rj).

ri = Mi + biixi + bjiXj + Ei,
rj = µj + bijxi + bjjxj + Ej,

E[rij] = (με – μ;) · [1 – 2Φ(Yij)]
+ Σ ∑(bki - bkj). [mk(1 – 2Ф(Yij)) + 2Sk · Pk:ij · Ф(Yij)],
k=i,j

Oij = UEij + OAij + CAij,

E[rij Xi > Xj] = (με - μj) +
Σ(bki - bkj). [mk + Sk. Pk:ij (-Yij)].
k=i,j

θij = UEij + OAij + CAij,
```