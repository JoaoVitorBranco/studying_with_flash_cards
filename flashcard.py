import random

class Card:
    question: str
    andswer: str

    def __init__(self, question:str, answer:str):
        self.question = question
        self.answer = answer
    
    def __str__(self):
        return f"P': {self.question} | R: {self.answer}"
    
class CardList:
    cards: list

    def __init__(self, cards:list = []):
        self.cards = cards
    
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

    def import_file(self) -> bool:
        if(len(self.cards) == 0):
            with open('questions.txt', 'r', encoding='utf-8') as f:
                lines = [line for line in f.readlines() if line != "\n"]
                if(len(lines) % 2 != 0):
                    return False
                
                for idx in range(int(len(lines)/2)):
                    question = lines[idx*2].replace("\n", "")
                    answer = lines[idx*2+1].replace("\n", "")
                    self.append(Card(question, answer))
                f.close()

            return True
        else:
            return False


def main():
    # 1: creating list of flash cards
    cardList = CardList()
    print("====== STEP 1 : IMPORT QUESTIONS ======")
    op = input("# Enter 1 to add a card, 2 to view all cards, 3 to stop adding , 4 to remove, 5 to import 'questions.txt': ")
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
            ok = cardList.import_file()
            if not ok:
                print("# You already have cards in your list or the file is wrong formatted")
        op = input("# Enter 1 to add a card, 2 to view all cards, 3 to stop adding , 4 to remove: ")

    # 2: selecting mode to operating
    print("\n\n====== STEP 2 : PRACTICE ======")
    op = input("# Enter 1 to practice, 2 to show all questions, 3 to stop: ")
    while op != "3":
        if op == "1":
            not_full_right = True
            list_of_rights = [False] * len(cardList.cards)
            while(not_full_right):
                print("# You need to answer all questions right to stop this practicing")
                cardList.shuffle()
                for idx, card in enumerate(cardList.cards):
                    if(list_of_rights[idx] == False):
                        print("P: " + card.question)
                        input("# Press enter to see the answer")
                        print("R: " + card.answer)
                        answer = input("# Yay/Nay? ")
                        if(answer.lower() in ["yay", "y", "yes", "sim", "s", "ya"]):
                            list_of_rights[idx] = True
                if(all(list_of_rights)):
                    not_full_right = False
            print("# You have answered all questions right =D")
        elif op == "2":
            cardList.show()
        op = input("# Enter 1 to practice, 2 to show all questions, 3 to stop: ")


if __name__ == '__main__':
    main()
