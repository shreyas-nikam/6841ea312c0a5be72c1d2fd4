id: 6841ea312c0a5be72c1d2fd4_documentation
summary: Investment Base Pairs Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Investment Base Pairs Lab Codelab

## Introduction
Duration: 00:05:00

This codelab provides a comprehensive guide to a Streamlit application designed to explore Investment Base Pairs.  The application offers two main sections: "Data Exploration" and "Performance Analysis".  Understanding this application will enhance your skills in data visualization, Streamlit application development, and financial data analysis.  The application uses Plotly for interactive visualizations, making it easy to understand complex financial data.  We'll cover the core concepts and functionalities, guiding you through the code and its implementation.


## Setting up the Development Environment
Duration: 00:10:00

Before starting, ensure you have the necessary libraries installed. You can install them using pip:

```bash
pip install streamlit pandas plotly
```

Clone the repository containing the application code.  The structure is as follows:

```
investment-base-pairs-lab/
├── app.py
└── application_pages/
    ├── page1.py
    └── page2.py

```

Navigate to the project directory in your terminal.


## Understanding the Application Structure
Duration: 00:15:00

The application is built using Streamlit, a Python framework for creating interactive web applications. The main file, `app.py`, acts as the entry point, handling navigation and page routing.  The core logic for each page is encapsulated in separate Python files within the `application_pages` directory.

A simplified architecture diagram:

```
+--+     +--+     +--+
|     app.py      |->| page1.py (Data)|->| Plotly Charts  |
+--+     +--+     +--+
                   \     +--+     +--+
                    \-| page2.py (Performance)|->| Plotly Charts  |
                    \     +--+     +--+
```

`app.py` uses Streamlit's `st.sidebar` to create a navigation menu allowing users to select between "Data Exploration" and "Performance Analysis". Based on user selection, the appropriate page's function is called.


## Data Exploration Page (`page1.py`)
Duration: 00:20:00

This page focuses on visualizing the dataset.  It initially presents a tabular view of the data, including Asset Class, Signal Type, Return, Volatility, Sharpe Ratio, and various predictability and imbalance metrics.

The code uses `pandas` to load and manipulate the data and `plotly.express` to create interactive charts. The user can then select an asset class from a dropdown menu to filter the data and view a scatter plot of Return vs. Volatility, colored by Signal Type. This allows for a visual exploration of the relationship between these key variables for each asset class.

<aside class="positive">
This interactive visualization helps quickly identify potential relationships between return, volatility and signal types for different asset classes.
</aside>


## Performance Analysis Page (`page2.py`)
Duration: 00:15:00

This page analyzes the contribution of different drivers to overall performance.  A bar chart visualizes the contribution of each driver (Own-asset, Cross-asset, Correlation, etc.) to the overall performance. This provides insights into the relative importance of each factor.


## Running the Application
Duration: 00:05:00

To run the application, navigate to the project directory in your terminal and execute the following command:

```bash
streamlit run app.py
```

This will launch the application in your web browser. You can then interact with the navigation menu and explore the data and performance analysis sections.


## Conclusion
Duration: 00:05:00

This codelab has guided you through a Streamlit application for exploring Investment Base Pairs. You've learned about the application's architecture, its use of pandas and Plotly for data manipulation and visualization, and how to run the Streamlit app.  This application provides a powerful and intuitive way to analyze and visualize financial data, and the concepts covered are applicable to a wide range of data science and financial modeling tasks.
