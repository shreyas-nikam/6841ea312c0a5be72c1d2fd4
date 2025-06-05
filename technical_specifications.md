# Technical Specifications: Cross-Asset Signal Pair Portfolio Analyzer (Streamlit App)

## Overview

This Streamlit application allows users to explore the performance of signal-driven pair portfolios, focusing on the decomposition of returns into their constituent elements as described in the research paper "Investment Base Pairs".  The application uses a synthetic dataset to demonstrate key drivers of pair portfolio performance and facilitate interactive data exploration.  The target audience includes finance professionals, researchers, and students.

## Step-by-Step Generation Process

1. **Data Loading and Preprocessing:** Load the synthetic dataset into a Pandas DataFrame. This dataset should include columns for asset class, signal type, return, volatility, Sharpe ratio, and the five key drivers of pair portfolio performance (own-asset predictability, cross-asset predictability, signal correlation, signal mean imbalance, signal variance imbalance), plus an unexplained effect.  Data cleaning might include handling missing values and outliers.

2. **User Interface Design (Streamlit):** Construct the Streamlit application's user interface using Streamlit's widgets.  This includes:
    * **Asset Class Selection:** A selectbox to choose asset classes (equities, bonds, currencies, commodities).
    * **Signal Type Selection:** A selectbox to choose signal types (value, momentum, carry).
    * **Selectivity Level Input:** A slider or number input to control the selectivity level (percentage of top-performing pairs to include).
    * **Data Display:**  A table to display filtered data showing returns, volatility, Sharpe ratios, and the key drivers.

3. **Interactive Chart Generation:** Use Plotly or similar libraries to create interactive charts:
    * **Line Charts:**  Display trends in average returns, volatility, and Sharpe ratios over time for selected asset classes and signal types.
    * **Bar Charts:** Show the contributions of each key driver to the overall pair portfolio return.
    * **Scatter Plots:** Visualize correlations between key drivers and pair portfolio performance.  Consider using tooltips to show detailed data on hover.

4. **Benchmark Strategy Comparison:** Implement logic to compare the signal-driven pair portfolio performance against a traditional benchmark strategy (e.g., linear weights, quantile sorting).  Allow users to adjust benchmark parameters through the UI.

5. **Real-time Updates:** Ensure that charts and data tables update dynamically as users change selections and input parameters in the Streamlit interface.

6. **Documentation and Tooltips:** Include inline documentation and tooltips to explain the data, visualizations, and parameters.  Link to the "Investment Base Pairs" paper as a reference.

## Important Definitions, Examples, and Formulae

* **Sharpe Ratio:**  (Average Portfolio Return - Risk-Free Rate) / Portfolio Standard Deviation.  Measures risk-adjusted return. *Example:* A Sharpe ratio of 1 indicates that the portfolio generates one unit of excess return for every unit of risk.
* **Five Key Drivers:** These are:
    * **Own-asset predictability:** How well the signal of a single asset predicts its own future returns.
    * **Cross-asset predictability:** How well the signal of one asset predicts the returns of another asset.
    * **Signal Correlation:** The correlation between signals of the asset pairs.
    * **Signal mean imbalance:** The difference in average signal values between the assets.
    * **Signal variance imbalance:** The difference in the volatility of signals between the assets.
* **Unexplained Effect:** Portion of the asset returns that is not explained by the signal.


## Libraries and Tools

* **Streamlit:**  The core framework for building the interactive web application.
* **Pandas:** For data manipulation and preprocessing.
* **Plotly (or similar):** For creating interactive charts and visualizations.  Provides tooltips and other interactive elements.
* **NumPy:**  For numerical computations.
* **SciPy (optional):**  For statistical analysis if needed beyond what Pandas provides.




### Appendix Code

```code
Table A.1: Equity Index Futures
Return (%)
Value
Mom. (×100)
Equity Future
Avg. SD N Avg SD
N
Avg. SD N
Carry (×100)
Avg. SD N
AEX-Index
0.5 6.2 334 -0.1
1.4
294
0.5 2.0
322
0.1 0.5 294
ASX 200
0.4 3.9 280
0.1 1.4
243
0.4 1.2
268
0.2 0.3 243
CAC 40
0.6 5.4 317
0.2
1.3
233
0.6 1.8
305
0.1 0.5 309
DAX
0.6 5.8 394
0.0 1.4
281
0.6 1.8
382
-0.2 0.4 309
Euro Stoxx 50
0.4 5.3 298
0.2 1.3
221
0.3 1.7
286
0.2 0.4 259
FTSE 100
0.4 4.4 465
0.1 1.4 224
0.4 1.2
453
0.1 0.4 309
FTSE MIB
0.4 6.0
232
0.3 1.4
194
0.4 1.9
220
0.2 0.4 194
HANG SENG
0.4 6.2 272
0.2 1.3
309
0.5 1.7
260
0.2 0.7 309
ΝΙΚΚΕΙ 225
0.2 6.0 420
0.2 1.2
246
0.2 1.8
408
0.1 0.2 290
Nasdaq 100 E-Mini
0.8 6.9 291
0.1 1.3
237
0.7 2.2
279
-0.1 0.1 255
OMX Stockholm 30
Russell 2000 E-Mini
0.8 4.8 223
-0.2 1.2
185
0.8 1.5
211
0.2 0.5 185
0.5 5.5 267
-0.2
1.3 230
0.6 1.6 255
0.0 0.7 230
S&P 500
0.5 4.5 312
Swiss Market Index
TSX 60
0.4 4.0
300
0.4 3.9 273 0.2 1.3 250
0.1 1.4 277
-0.1
1.4 219
0.5 1.4
300
0.0 0.2 277
0.4 1.4 288
0.2 0.4 297
0.5 1.2 261
0.1 0.1 250
Notes: Returns are signals are monthly. Value is the earnings/price ratio (3-year z-score); momentum is the
average trailing 12-month return; and carry is the futures roll (spot minus first).


Table A.2: Bond Futures
Return (%)
Value (×100)
Bond Future
Avg.
SD N
Avg SD N
Mom. (×100)
Avg. SD N
Carry (×100)
Avg. SD N
Australia 10Υ
0.2 2.3
465
0.3 0.2
308
0.3 0.7
452
0.1 0.1 308
Canada 10Υ
0.2 1.8 408
0.2 0.2
308
0.3 0.5
395
0.2 0.2 308
Euro Bobl
0.2 0.9 378
0.1 0.4
308
0.2 0.3
365
0.3
0.2 308
Euro Schatz
0.0 0.4
294
0.1 1.0
307
0.0 0.1
281
0.2 0.3 307
France 10Υ
0.2 1.9 137
0.0
0.1 126
0.2
0.6
124
0.3 0.1 126
GB 10Y
0.2 2.2 465
0.1 0.2 308
0.2 0.6
452
0.1 0.2 308
Germany 10Y
0.2 1.6 297
0.1
0.2 308
0.2 0.5
284
0.2 0.1 308
Italy 10Y
0.4
2.7
167
0.2 0.1 157
0.4
0.9
154
0.5 0.2 157
Japan 10Y
0.2
1.4
455
0.1 0.1 308
0.2
0.4
442
0.2 0.1 308
SFE 3Yr
0.0
0.7
264
0.4 0.6 253
0.1 0.2
251
0.1 0.3 253
US 10Y
0.3
1.8
465
0.1 0.2 308
0.3 0.6
452
0.3
0.2 308
US 2Y
0.1 0.5 399
0.0 0.9 308
0.1 0.2 386
0.4
0.5 308
US 5Y
0.2 1.2 424
0.1 0.3 308
0.2 0.4
411
0.4
0.3 308
Notes: Returns are signals are monthly. Value is the real yield; momentum is the average trailing 12-month
return; and carry is the excess yield plus term-structure roll.


Table A.3: Currency Forwards
Return (%)
1M Currency Forward
Avg. SD N Avg SD
Mom. (×100)
Carry (×100)
Avg. SD N Avg. SD N
AUSDollar/USD
0.0 3.4 465
0.1
1.5
305
0.1 1.0 453
0.1 0.2 309
GBPound/USD
-0.2 2.7 417
-0.1
1.4
305
-0.2 0.9
405
0.0 0.1
309
CANDollar/USD
0.0 2.2 417
-0.3
1.5 305
0.0 0.6 405
0.0 0.1 309
Euro/USD
-0.1 2.7 297
0.1 1.4 302
0.0 0.9 285
-0.2 0.2 309
JAPYenUSD
-0.2 3.0 417
-0.2 1.4 305
-0.1 0.9 405
-0.1 0.1 261
NZDollar/USD
0.1 3.3 417
0.2 1.4
305
0.2 1.0
405
0.2 0.2 309
NORKrone/USD
SWEKrona/USD
0.0 3.3 417
0.0 1.4 305
0.0 1.0
405
0.1 0.2 309
Swiss Franc/USD
0.0 3.2 417
0.0 1.3 305
0.0 1.0
405
0.1 0.2 309
0.0 3.0 417
0.1 1.4 305
0.0 1.0
405
0.0 0.1 309
Notes: Returns are signals are monthly. Value is the 5-year real exchange rate reversal (3-year z-score);
momentum is the average trailing 12-month return; and carry is the cash rate differential.


Table A.4: Commodity Futures
Return (%)
Value
Mom. (×100)
Commodity Future
Avg.
SD N Avg SD
N
Avg. SD N
Carry (×100)
Avg. SD N
Aluminum
-0.1 5.7 314
-0.2
0.4
249
0.0 1.9
302
-0.3 0.4 277
Blendstock Gasoline
1.4 10.2 465
-0.4
0.7
309
1.3 2.9
453
0.4 3.6 309
Cocoa
-0.1
7.9 465
-0.2
0.4
309
-0.2 2.0
453
-0.2 0.8 309
Coffee
-0.1 10.3 465
-0.2
0.6
309
-0.1 3.3 453
-0.8 0.8 309
Copper
0.9 7.6 453
-0.5
1.1 309
0.9 2.6
441
-0.1 0.5 309
Corn
-0.2
7.4 465
-0.2 0.6
309
-0.2
2.1
453
-0.7 1.7 309
Cotton
0.3
7.4 465
-0.1 0.4
309
0.3 2.5
453
-0.5 1.4 309
Crude Oil, Brent
1.0
9.2 410
-0.5 0.8
309
0.9 3.1
398
0.0 1.4 309
Feeder Cattle
0.2 4.1 465
-0.2
0.3 309
0.2 1.2
453
-0.3 1.1 309
Gold
0.2 4.4 465
-0.5 0.6
309
0.2 1.2
453
-0.2 0.2 309
Heating Oil
0.9 9.3 465
-0.5 0.8
309
0.8 3.1
453
-0.1
1.9 309
Kansas Wheat
0.0 7.5 465
-0.2 0.5
309
0.1 2.2
453
-0.7 0.8 309
Lead
0.9
8.2 274
-0.7 1.4
209
0.9 2.7
262
0.0 0.5 273
Lean Hogs
-0.2
7.2 465
-0.1 0.3
309
-0.2 2.2
453
-0.7 5.0 309
Live Cattle
0.2 3.9 465
-0.2 0.2
309
0.2 1.1
453
Low Sulphur Gasoil
1.0 9.2 447
-0.5
0.8
309
0.9 3.1
435
Natural Gas
-0.7 14.3 401
-0.3
0.8
309
-0.5 4.5
389
-0.3 1.7 309
Nickel
0.8 10.1 314
-0.6
1.3
249
1.0 3.4
302
0.0 1.5 309
Platinum
0.4 6.4 465
-0.3 0.6
309
0.4 1.8
453
0.0 0.3 309
Silver
0.3 8.0 465
-0.5 0.8
309
0.3 2.1
453
-0.2
0.1 309
Soybean Meal
0.8 7.2 465
-0.2 0.4
309
0.8 1.8
453
0.3 1.3 309
Soybean Oil
0.1 7.2 465
-0.2 0.6 309
0.1 2.2 453
Soybeans
0.4
6.4 465
-0.2 0.5 309
Sugar
0.6
9.4 465
-0.2 0.6
WTI Crude
0.8 10.4 465
-0.4 0.7
309
309
Wheat
-0.3
Zinc
7.6 465 -0.2 0.5 309
0.2 7.6 314 -0.5 0.9 249
0.4 1.8 453
0.6 2.6 453
0.8 3.2 453
-0.2 2.1 453
0.3 2.7 302
-0.4 0.8 309
-0.1 1.2 309
0.1 2.0 309
-0.4 2.1 309
-1.1 0.7 309
-0.2 0.4 277
Notes: Returns are signals are monthly. Value is the 5-year price reversal; momentum is the average trailing
12-month return; and carry is the futures roll (first minus second).

```code
r = Σi=1 Wiri = Σi=1 W[i]r[i]


rij = sign(xi - xj) · (ri - rj).


r = n² - 1{n odd} Σi<j rij


ri = μi + bii xi + bji xj + εi,
rj = μj + bij xi + bjj xj + εj,


E[rij] = (με – μ;) · [1 – 2Φ(Yij)] + Σk=i,j Σ (bki - bkj). [mk(1 – 2Ф(Yij)) + 2Sk · Pk:ij · Ф(Yij)],


θij = UEij + OAij + CAij,


UEij = (με – μ;)[1 – 2Φ(Yij)],
OAij = (biimi - bjjmj) [1 – 2Ф(Yij)] + 2(Yij) [biisi + bjjsj - (bii + bjj)SiSjPij]/√s + s3 - 2SiSjPij,
CAij = (bijmi - bjimj)[1 – 2Ф(Yij)] + 2(Yij)[bijsi + bjisj - (bij + bji)SiSjPij]/√s + s3 - 2SiSjPij,


Avg(rij)t = a + Blij,t + Eij,t,


Avg(rij)t = a + βUE UEij,t + βOA OAij,t + βCA CAij,t + Eij,t,

```