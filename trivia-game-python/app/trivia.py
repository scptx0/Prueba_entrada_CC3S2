# Clase que representa una pregunta de trivia
class Question:
    def __init__(self, description, options, correct_answer, difficulty):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty

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
    quiz.add_question(Question("¿Quién pintó la Mona Lisa?", ["Van Gogh", "Picasso", "Leonardo da Vinci", "Rembrandt"], "Leonardo da Vinci", 2))
    quiz.add_question(Question("¿En qué año llegó el hombre a la Luna?", ["1965", "1969", "1972", "1980"], "1969", 3))
    quiz.add_question(Question("¿En qué continente se encuentra Egipto?", ["Asia", "África", "Europa", "América"], "África", 1))
    quiz.add_question(Question("¿Cuál es el metal más abundante en la corteza terrestre?", ["Hierro", "Aluminio", "Cobre", "Oro"], "Aluminio", 4))
    quiz.add_question(Question("¿Cuál es el país más grande del mundo?", ["China", "Canadá", "Rusia", "Estados Unidos"], "Rusia", 3))
    quiz.add_question(Question("¿Qué científico propuso la teoría de la relatividad?", ["Newton", "Einstein", "Galileo", "Tesla"], "Einstein", 4))
    quiz.add_question(Question("¿Cuál es el océano más grande del mundo?", ["Atlántico", "Pacífico", "Índico", "Ártico"], "Pacífico", 1))
    quiz.add_question(Question("¿Qué país ganó la Copa Mundial de Fútbol en 2018?", ["Brasil", "Alemania", "Francia", "Argentina"], "Francia", 3))
    quiz.add_question(Question("¿Cuál es el idioma más hablado en el mundo?", ["Inglés", "Español", "Chino mandarín", "Hindú"], "Chino mandarín", 2))
    quiz.add_question(Question("¿Cuál es el río más largo del mundo?", ["Nilo", "Amazonas", "Yangtsé", "Misisipi"], "Amazonas", 4))

    bad_streak = 0
    print (f"{"="*40}\nBienvenido al juego de trivia!\n{"="*40}")
    print ("\nEscribe el nombre de la respuesta correcta. ¡Asegurate de escribirla correctamente!\n")

    # Bucle principal del juego
    while quiz.current_question_index < 10:
        question = quiz.get_next_question()

        # Si hay una mala racha de 3 o más respuestas incorrectas, se busca la pregunta más fácil restante
        if bad_streak >= 3:
            remaining_questions = quiz.questions[quiz.current_question_index:]

            if remaining_questions:
                easiest_question = min(remaining_questions, key=lambda q: q.difficulty)
                easiest_index = quiz.questions.index(easiest_question)

                # swap la pregunta más fácil restante con la actual
                quiz.questions[quiz.current_question_index-1], quiz.questions[easiest_index] = \
                    quiz.questions[easiest_index], quiz.questions[quiz.current_question_index-1]

                question = quiz.questions[quiz.current_question_index-1]
        
        # Si hay una pregunta, se muestra
        if question:
            print(f"{"*"*60}\nPregunta {quiz.current_question_index}: {question.description}\n{"*"*60}")
            for idx, option in enumerate(question.options):
                print(f"{idx + 1}) {option}")
            answer = input("Tu respuesta: ")
            if quiz.answer_question(question, answer):
                bad_streak = 0
                print("\n¡Correcto!\n")
            else:
                bad_streak += 1
                print(f"\n¡Incorrecto!. La respuesta correcta es {question.correct_answer}\n")
            
        else:
            break
    print("Juego terminado.")
    print(f"Preguntas contestadas: {quiz.current_question_index}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")

run_quiz()