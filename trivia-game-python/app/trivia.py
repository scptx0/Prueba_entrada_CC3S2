# Clase que representa una pregunta de trivia
class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return self.correct_answer == answer

# Clase que representa un juego de trivia
class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    
# Funcion principal de ejecucion del juego
def run_quiz ():

    quiz = Quiz()

    # Establecer preguntas del juego
    quiz.add_question(Question("Cuanto es 2 + 2", ["1", "2", "3", "4"], "4"))
    quiz.add_question(Question("Cuanto es 2 + 3", ["2", "3", "4", "5"], "5"))
    quiz.add_question(Question("Cuanto es 2 + 4", ["2", "3", "4", "6"], "6"))
    quiz.add_question(Question("Cuanto es 2 + 5", ["2", "3", "4", "7"], "7"))

    # Imprimir preguntas
    question = quiz.get_next_question()
    while question:
        print(f"Pregunta {quiz.current_question_index}: {question.description}")
        question = quiz.get_next_question()

run_quiz()