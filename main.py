from processing.distancing import createClusters
from model.predict import predictGenre

def run():
    files = createClusters()
    for i in files:
        predictGenre(i)

if __name__ == "__main__":
    run()