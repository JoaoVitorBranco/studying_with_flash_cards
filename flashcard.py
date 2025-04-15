import random
import os

class Card:
    question: str
    andswer: str

    def __init__(self, question:str, answer:str):
        self.question = question
        self.answer = answer
    
    def __str__(self):
        return f"P: {self.question} | R: {self.answer}"
    
class CardList:
    cards: list

    def __init__(self, cards:list = []):
        self.cards = cards

    def clean(self):
        self.cards = []

    def append(self, card:Card):
        self.cards.append(card)
    
    def remove(self, index:int) -> bool:
        try:
            self.cards.pop(index)
            return True
        except:
            return False
    def show(self):
        print("[", end="")
        if(len(self.cards) > 0):
            for idx, card in enumerate(self.cards[0:len(self.cards)-1]):
                print(f"\n\t{idx}) " + str(card), end="; ")
            print(f"\n\t{len(self.cards)-1}) "+ str(self.cards[-1]) + "\n]")
        else:
            print("]")

    def shuffle(self):
        random.shuffle(self.cards)

    def import_file(self, file_name: str) -> bool:
        with open("questions/"+file_name+".txt", 'r', encoding='utf-8') as f:
            lines = [line for line in f.readlines() if line != "\n"]
            if(len(lines) % 2 != 0):
                return False
            
            for idx in range(int(len(lines)/2)):
                question = lines[idx*2].replace("\n", "")
                answer = lines[idx*2+1].replace("\n", "")
                self.append(Card(question, answer))
            f.close()

        return True

def generate_cardlist():
    cardList = CardList()
    TERMINAL_QUESTION_STRING = "# Enter 1 to add a card, 2 to view all cards, 3 to start practicing mode , 4 to remove, 5 to import a package of questions, 6 exam import (import all questions): "
    print("====== STEP 1 : IMPORT QUESTIONS ======")
    op = input(TERMINAL_QUESTION_STRING)
    while op != "3":

        if op == "1":
            question = input("# Enter question: ")
            answer = input("# Enter answer: ")
            cardList.append(Card(question, answer))

        elif op == "2":
            cardList.show()

        elif op == "4":
            cardList.show()
            question = int(input("# Enter the index of the card that you want to remove: "))
            ok = cardList.remove(question)
            if not ok:
                print("# Invalid index")

        elif op == "5":
            list_of_questions = [question.replace('.txt', '') for question in os.listdir("questions/")]
            questions_name = ''
            while(questions_name not in list_of_questions):
                questions_name = input(f"# Enter the name of the package folder that you want to import. Select one of those files {list_of_questions}: ")
            list_of_questions = [question.replace('.txt', '') for question in os.listdir("questions/" + questions_name)]
            questions_name = ''
            while(questions_name not in list_of_questions):
                questions_name = input(f"# Enter the name of the package file that you want to import. Select one of those files {list_of_questions}: ")
            cardList.clean()
            ok = cardList.import_file(questions_name)
            if not ok:
                print("# You already have cards in your list or the file is wrong formatted")
    
        elif op == "6":
            cardList.clean()
            list_of_questions = [question.replace('.txt', '') for question in os.listdir("questions/")]
            questions_name = ''
            while(questions_name not in list_of_questions):
                questions_name = input(f"# Enter the name of the package folder that you want to import. Select one of those files {list_of_questions}: ")
            list_of_questions = [questions_name + "/" + question.replace('.txt', '') for question in os.listdir("questions/"+questions_name)]
            for question in list_of_questions:
                cardList.import_file(question)
        op = input(TERMINAL_QUESTION_STRING)
    return cardList

def main():
    # 1: creating list of flash cards
    cardList = generate_cardlist()

    # 2: selecting mode to operating
    print("\n\n====== STEP 2 : PRACTICE ======")
    TERMINAL_PRACTICE_STRING = "# Enter 1 to practice, 2 to show all questions, 3 to stop, 4 to import new cardlist: "
    op = input(TERMINAL_PRACTICE_STRING)
    while op != "3":
        if op == "1":
            cardList.shuffle()
            not_full_right = True
            list_of_rights = [False] * len(cardList.cards)
            while(not_full_right):
                print("# You need to answer all questions right to stop this practicing")
                cardlist_len = len([card_is_right for card_is_right in list_of_rights if not card_is_right])
                idx_card_round = 0
                for idx, card in enumerate(cardList.cards):
                    if(list_of_rights[idx] == False):
                        print(f"\nP ({idx_card_round+1}/{cardlist_len}): " + card.question)
                        input("# Press enter to see the answer")
                        print("R: " + card.answer)
                        answer = input("# Yay/Nay? ")
                        if(answer.lower() in ["yay", "y", "yes", "sim", "s", "ya"]):
                            list_of_rights[idx] = True
                        idx_card_round += 1
                if(all(list_of_rights)):
                    not_full_right = False
                print(f"\n# You got {list_of_rights.count(True)}/{len(list_of_rights)} right answers")
            print("# You have answered all questions right =D\n")
        elif op == "2":
            cardList.show()
        elif op == "4":
            cardList = generate_cardlist()
        op = input(TERMINAL_PRACTICE_STRING)


if __name__ == '__main__':
    main()
