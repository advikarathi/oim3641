import os

from fastapi import FastAPI, HTTPException
from supabase import create_client

app = FastAPI()

# The publishable key: read-only under the table's row-level security rules
supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_PUBLISHABLE_KEY"]
)


@app.get("/")
def test():
    return "FastAPI is running"


@app.get("/analyze/{symbol}")
def analyze(symbol: str):
    response = (
        supabase.table("stock_records")
        .select("*")
        .eq("ticker", symbol.upper())
        .order("created_at", desc=True)
        .limit(1)
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=404, detail=f"No data for {symbol.upper()}")

    row = response.data[0]
    signal = "Bullish" if row["final_price"] > row["initial_price"] else "Bearish"

    return {
        "ticker": row["ticker"],
        "initial_price": row["initial_price"],
        "final_price": row["final_price"],
        "percent_change": row.get("percent_change"),
        "signal": signal,
        "as_of": row["created_at"],
    }


@app.get("/history/{symbol}")
def history(symbol: str):
    response = (
        supabase.table("stock_records")
        .select("ticker, initial_price, final_price, percent_change, created_at")
        .eq("ticker", symbol.upper())
        .order("created_at")
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=404, detail=f"No data for {symbol.upper()}")

    return response.data
