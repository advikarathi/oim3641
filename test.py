from stock import Stock


aapl = Stock(symbol="AAPL", start="2025-09-29", end="2026-09-28")

nlfx = Stock(symbol="NLFX", start="2025-09-29", end="2026-09-28")


print(aapl.data)
fig=aapl.plot_performance()
fig.show()