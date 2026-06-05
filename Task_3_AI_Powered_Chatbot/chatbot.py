from fuzzywuzzy import fuzz
from knowledge_base import knowledge_base


def get_response(user_message):

    best_score = 0
    best_answer = None

    for question in knowledge_base:

        score = fuzz.ratio(
            user_message.lower(),
            question.lower()
        )

        if score > best_score:

            best_score = score
            best_answer = knowledge_base[question]

    if best_score > 70:

        return best_answer

    return "Sorry, I don't understand your question."