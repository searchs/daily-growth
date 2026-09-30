# Legacy notebook lessons

Curated from the historical `rhema` repository, which contained word-count notebooks, a Bokeh/Pandas visualisation notebook, a large text corpus and an Olympic-medals CSV.

## What remains useful

- keep raw data separate from transformation logic
- turn repeated notebook cells into named functions
- make visualisation inputs explicit and reproducible
- preserve notebooks for exploration, but move reusable logic into modules
- avoid committing multi-megabyte raw datasets when they can be fetched or generated reproducibly

## Migration decision

The 4.6 MB `data.txt`, medals dataset and rendered notebook outputs were not copied. The durable value is the progression from exploratory word counting into tabular analysis and visualisation, not the historical artefacts themselves.

A modern equivalent should use a small fixture dataset, Pandas/Polars for transformation, and a maintained plotting library with tests around the data-preparation layer.
