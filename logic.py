class Questions:
    def __init__(self):
        self.total = []
        self.count = 0

    def add(self, question):
        self.total.append(question)
        self.count += 1


class Question:
    def __init__(self, text):
        self.text = text
        self.user_answer = 0


with open("questions.txt", "r") as raw_file:
    bulk = raw_file.read()
    questions = Questions()

    for question_text in bulk.split("\n"):
        if question_text == "":
            continue
        question = Question(question_text)
        questions.add(question)


def mainloop(question_bank):
    for question in question_bank:
        print(f"\n{question.text}\n")
        answer = input("0 ile 5 arasinda bir deger girin: ")
        while True:
            try:
                answer = int(answer)

            except:
                print("sadece 0 ile 5 arasi tam sayi girin\n")
                answer = input("0 ile 5 arasinda bir deger girin: ")

            if 0 <= answer <= 5:
                question.user_answer = answer
                break
            else:
                print("girdi deger araligi disinda\n")
                answer = input("0 ile 5 arasinda bir deger girin: ")


mainloop(questions.total)
