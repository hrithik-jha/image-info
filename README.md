# Thumbnail Personalization

## Running
### With Pipeline
`python main.py`

### Without Pipeline
`cd video-extraction`\
`python vid2img.py`\
`cd ..`\
`cd processing`\
`python distancing.py`\
Check out result.

To do: ML Model testing.

Workflow

  - Train a neural network to identify the genre from the image. [Refrence](https://towardsdatascience.com/building-a-movie-genre-classifier-using-a-dataset-created-using-google-images-4752f75a1d79)
  - manually get different kinds of thumbnails for a few movies.
  - According to the user's prefrence of genres the neural network will classify the genre for a particaular movie and show the thumbnail     most suitable for the user.
