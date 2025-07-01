# Open Science Toolbox

To fetch the original data, convert it to a parquet file, and run the analysis in this repository
you can use the [Pixi](https://pixi.sh/latest/) command line tool.

To reproduce the outputs:

```sh
pixi run analyze
```

To view the the results in a notebook:

```sh
pixi run marimo edit scripts/analysis.py
```
