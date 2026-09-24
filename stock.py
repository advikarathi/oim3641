import numpy as np
import pandas as pd
import plotly.express as px
import yfinance as yf

class Stock:
    def __init__(self, symbol, start, end, ma_window: int = 10):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.ma_window = ma_window
        self.data, self.message = self.get_data()

    def get_data(self):
        try:
            data = yf.download(self.symbol,
                               start=self.start,
                               end=self.end,
                               progress=False,
                               multi_level_index=False)
            if data.empty:
                return None, f"No data found for {self.symbol}"
            data = self._calc_returns(data)
            data = self._calc_ma(data, self.ma_window)
            return data, f"Sucessfully downloaded for {self.symbol}"
        except Exception as e:
            return None, f"failed due to {e}"

    def _calc_returns(self, df : {__setitem__,__getitem__,dropna}):
        df['change'] = df['Close'] - df['Close'].shift(1)
        df['return'] = np.log(df['Close']).diff().round(4)
        return df.dropna()

    def _calc_ma(self, df : {__setitem__,__getitem__},window):
        df['MA'] = df['Close'].rolling(window=window).mean()
        return df

    def plot_return_dist(self):
        """return plotly histogram showing dist of daily returns"""
        mean_return = self.data['return'].mean()
        fig = px.histogram(self.data['return'],
                           nbins=35,
                           title=f'Distribution of Daily Returns for {self.symbol}',
                           labels={'value':"Return", 'count': 'Frequency'})

        fig.update_traces(marker_line_color= 'rgb(255,0,0)',
                          marker_line_width=0.5)
        fig.add_vline(x=mean_return,
                      line_dash="dash",
                      line_color="red",
                      annotation_text=f"Mean: {mean_return: .2F}",
                      annotation_position="top right")
        return fig


# --- For development testing only ---
def main():
    test = Stock(symbol='AAPL', start="2025-09-24", end="2026-09-23")
    print(test.data)
    #print(test.message)
    fig = test.plot_return_dist()
    fig.show()


if __name__ == '__main__':
    main()
