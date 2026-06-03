from fuzzywuzzy import fuzz
def check_name_similarity(name1, name2):
    score = fuzz.ratio(
        name1.lower(),
        name2.lower()
    )
    return score