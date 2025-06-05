
# Investment Base Pairs Lab - Streamlit App

This repository contains a Streamlit application for exploring the performance of signal-driven pair portfolios.  The application demonstrates the decomposition of returns as described in the research paper "Investment Base Pairs" using a synthetic dataset.

## Business Logic

The application allows users to interactively explore the relationship between different asset classes, signal types, and the five key drivers of pair portfolio performance:

1. **Own-asset predictability:**  How well a signal for a single asset predicts its own future returns.
2. **Cross-asset predictability:** How well the signal of one asset predicts the returns of another.
3. **Signal correlation:** The correlation between the signals of pairs of assets.
4. **Signal mean imbalance:** The difference in average signal values between paired assets.
5. **Signal variance imbalance:** The difference in the volatility of signals between paired assets.

Users can select asset classes, signal types, and view interactive charts showing the contribution of each driver to overall portfolio return.  A comparison with benchmark strategies is also possible.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **(Optional) Build and run with Docker:**
   ```bash
   docker build -t investment-base-pairs .
   docker run -p 8501:8501 investment-base-pairs
   ```  Then access the app at `http://localhost:8501`.

##  Key Formulae

*(Insert key formulae here from the technical specifications)*

## References

* Investment Base Pairs Research Paper (Link to paper)


