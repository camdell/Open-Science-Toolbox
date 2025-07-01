import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell
def _():
    from pandas import read_parquet

    df = read_parquet('data/sacramento_daily_weather.parquet')
    df
    return (df,)


@app.cell
def _(df):
    from matplotlib.pyplot import subplots

    fig, ax = subplots()

    resampled_df = df.set_index('time').resample('YE').mean()
    ax.plot(resampled_df.index, resampled_df['temperature_2m_mean'])
    ax.set_title('Average Annual Temperature in Sacramento, CA')
    ax.set_ylabel('Temperature (°F)')
    ax.set_xlabel('Year')

    from pathlib import Path
    p = Path('results')
    p.mkdir(exist_ok=True)
    fig.savefig(p / 'annual_avg.png')
    fig
    return


if __name__ == "__main__":
    app.run()
