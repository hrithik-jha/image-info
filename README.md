# Thumbnail Personalization

## Running
Currently all facets of the program are set for 3 clusters. \
If the number of clusters has to be changes, change should be introduced in `processing/distancing.py`, `model/predict.py` and the shell scripts in processing.

## Steps
1. Run the `vid2img.py` program to partition video into frames.
2. Execute `processing/distancing.py` to perform frame clustering and create individual file clusters.
3. Find the predictions using `model/predict.py` for all files in a cluster. Output can be sanitised.

## To-do
Allow more than 3 properties to show and choose the ones which are different for each cluster.
