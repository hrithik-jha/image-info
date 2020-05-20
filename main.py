from processing.distancing import createClusters
from model.predict import predictGenre



def run1():
    createClusters()
    #for i in files:
    #    predictGenre(i)

def run():
    print('''
    DEPRACATED METHOD
    ''')

if __name__ == "__main__":
    run()