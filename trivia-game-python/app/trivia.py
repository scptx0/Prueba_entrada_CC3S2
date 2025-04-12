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
        self.correct_answers = 0
        self.incorrect_answers = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    
    def answer_question (self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False
    
# Funcion principal de ejecucion del juego
def run_quiz ():

    quiz = Quiz()

    # Establecer preguntas del juego
    quiz.add_question(Question("Cuanto es 2 + 2", ["1", "2", "3", "4"], "4"))
    quiz.add_question(Question("Cuanto es 2 + 3", ["2", "3", "4", "5"], "5"))
    quiz.add_question(Question("Cuanto es 2 + 4", ["2", "3", "4", "6"], "6"))
    quiz.add_question(Question("Cuanto es 2 + 5", ["2", "3", "4", "7"], "7"))
    quiz.add_question(Question("Cuanto es 2 + 6", ["2", "3", "4", "8"], "8"))
    quiz.add_question(Question("Cuanto es 2 + 7", ["2", "3", "4", "9"], "9"))
    quiz.add_question(Question("Cuanto es 2 + 8", ["2", "3", "4", "10"], "10"))
    quiz.add_question(Question("Cuanto es 2 + 9", ["2", "3", "4", "11"], "11"))
    quiz.add_question(Question("Cuanto es 2 + 10", ["2", "3", "4", "12"], "12"))
    quiz.add_question(Question("Cuanto es 2 + 11", ["2", "3", "4", "13"], "13"))

    # Bucle principal del juego
    while quiz.current_question_index < 10:
        question = quiz.get_next_question()
        print(f"Pregunta {quiz.current_question_index}: {question.description}")

run_quiz()