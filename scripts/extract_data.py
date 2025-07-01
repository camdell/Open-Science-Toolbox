import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Extract Data from Open Meteo Web Response

    ## Original Data Overview
    """
    )
    return


@app.cell
def _():
    from json import load

    with open('data/sacramento_weather.json') as f:
        data = load(f)

    data.keys()
    return (data,)


@app.cell
def _(data):
    data['daily']['temperature_2m_mean'][:5]
    return


@app.cell
def _(data):
    import pandas as pd

    df = (
        pd.DataFrame(data['daily'])
        .assign(
            time=lambda d: pd.to_datetime(d['time'], format='%Y-%m-%d')
        )
    )

    df
    return (df,)


@app.cell
def _(df):
    df.to_parquet('data/sacramento_daily_weather.parquet')
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
