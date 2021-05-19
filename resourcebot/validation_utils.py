""" utils to validate requests """
import Levenshtein

class valUtils:

    def get_distance(text1,text2):
        return Levenshtein.distance(text1,text2)


if __name__ == "__main__":
    pass

