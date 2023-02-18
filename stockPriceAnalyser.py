import pandas as pd
import streamlit as st
import datetime
import yfinance as yf 

st.write(
    """
    # Stock Price Analyser

    shown are the stock price of apple company
    """
)

ticker_symbol = st.text_input("Enter stock symbol", "AAPL", key = "placeholder")  #"AAPL"

col1, col2 = st.columns(2)
# start date
with col1:
    start_date = st.date_input("Input the start date",
                            datetime.date(2019,1,1))
# End date
with col2:
    end_date = st.date_input("Input the end date", 
                            datetime.date(2022,12,31))


ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period = "1d", 
                                start = f"{start_date}", 
                                end = f"{end_date}" )

st.write(
f"""
### {ticker_symbol}' stock price info
"""
)
st.dataframe(ticker_df)

## showcasing line charts
st.write(
    """
    ## Daily closing price
    """
)
st.line_chart(ticker_df.Close)

st.write(
"""
Daily volume
"""
)
st.line_chart(ticker_df.Volume)


## 2nd way
col1, col2 = st.columns(2)

with col1:
    st.header("Daily closing price:")
    st.line_chart(ticker_df.Close)

with col2:
    st.header("Daily volume")
    st.line_chart(ticker_df.Volume)