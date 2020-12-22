import sqlite3
import random
from io import StringIO
import shutil
import argparse

f = StringIO()  # this is 
def record_log(message):
    f.write(message + "\n")  # creates a file-like object based upon the given string and it keeps adding strings to the same constructor f

class Card():
    def __init__(self):
        self.card_term = None
        self.card_definition = None
        self.card_store = {}
        self.mistake_store = {}  # term, mistake count

    def add(self):  # add a unique term-definition pair
        # num_cards = int(input("Input the number of cards:\n", ))
        num_cards = 1
        for i in range(1, num_cards + 1):
            print(f"The term for card #{i}")
            record_log(f"The term for card #{i}")
            while True:
                term = input()
                record_log(term)
                if term in self.card_store.keys():
                    print(f'The term "{term}" already exists. Try again:')
                    record_log(f'The term "{term}" already exists. Try again:')
                else:
                    break
            
            print(f"The definition for card #{i}")
            record_log(f"The definition for card #{i}")
            while True:
                definition = input()
                record_log(definition)
                if definition in self.card_store.values():
                    print(f'The definition "{definition}" already exists. Try again:')
                    record_log(f'The definition "{definition}" already exists. Try again:')
                else:
                    break    
            
            self.card_term = term
            self.card_definition = definition
            self.card_store[self.card_term] = self.card_definition
            self.mistake_store[self.card_term] = 0

            print(self.card_store)
            print(self.mistake_store)
            print(f'The pair "({term}: "{definition})" has been added')
            record_log(f'The pair "({term}: "{definition})" has been added')
            
    def remove(self):
        term_rem = input("Which card?\n", )
        record_log("Which card?\n" + term_rem)
        
        if term_rem in self.card_store:
            del self.card_store[term_rem]
            print("The card has been removed.")
            record_log("The card has been removed.")

        if term_rem in self.mistake_store:
            del self.mistake_store[term_rem]
            print("The card has been removed.")
            record_log("The card has been removed.")

        else:
            print(f'can\'t remove "{term_rem}": there is no such card.')
            record_log(f'can\'t remove "{term_rem}": there is no such card.')
            
    def imp(self, file=None):
        if file != None:
            file_name = file
        else:
            file_name = input("File name:\n", )
            record_log("File name:\n" + file_name)
        try:
            conn = sqlite3.connect(f"{file_name}", uri=True)  # this opens a read only copy of the database but if database doesn't exit, it returns an error
            # the ?mode=ro makes it read only
            #mode=ro
            # mode=rw
            # mode=rwc
            # mode=memory
            # The mode query parameter determines if the new database is opened read-only, read-write, read-write and created if it does not exist, or that the database is a pure in-memory database that never interacts with disk, respectively.
            cur = conn.cursor()
            query = 'SELECT * FROM todo'
            cur.execute(query)
            count = 0
            for i in cur.fetchall():
                self.card_store[i[0]] = i[1]
                self.mistake_store[i[0]] = i[2]
                count += 1
            if count < 2:
                print(f'{count} card have been loaded.')
                record_log(f'{count} card have been loaded.')
            else:
                print(f'{count} cards have been loaded.')
                record_log(f'{count} cards have been loaded.')
            conn.commit()

        except sqlite3.OperationalError as err:
            print("File not found.")
            record_log("File not found.")

    def export(self, file=None):
        if file != None:
            file_name = file
        else:
            file_name = input("File name:\n", )
            record_log("File name:\n" + file_name)

        conn = sqlite3.connect(f"{file_name}")
        cur = conn.cursor()
        query = f"CREATE TABLE IF NOT EXISTS todo (term text, definition text, mistake integer)"
        cur.execute(query)
        conn.commit()
        # cursor object now creates a database where I can start storing info
        count = 0
        for k, v in self.card_store.items():
            print("at export", self.card_store)
            cur.execute("insert into todo values (:term, :definition, :mistake)", {"term": k, "definition": v, "mistake": 0})
            count += 1
            conn.commit()

        for k, v in self.mistake_store.items():
            print("at export", self.mistake_store)
            cur.execute('UPDATE todo SET mistake = :mistake where term = :term', {"term": k, "mistake": v})
            conn.commit()

        if count < 2:
            print(f'{count} card have been saved')
            record_log(f'{count} card have been saved')
        else:
            print(f'{count} cards have been saved')
            record_log(f'{count} cards have been saved')
        
    def ask(self):
        num_asks = int(input("How many times to ask:\n", ))
        record_log("How many times to ask:\n" + str(num_asks))
        
        while num_asks > 0:
            term = random.choice(list(self.card_store.keys()))
            definition = self.card_store[term]
            answer = input(f'Print the definition of "{term}"\n')
            record_log(answer)
        
            if answer == definition:
                print("Correct!")
                record_log("Correct!")

            elif answer != definition:
                self.mistake_store[term] += 1

                if answer in self.card_store.values():
                    for k, v in self.card_store.items():
                        if v == answer:
                            print(f'Wrong. The right answer is {definition}, but your definition is correct for "{k}"')
                            record_log(f'Wrong. The right answer is {definition}, but your definition is correct for "{k}"')
        
                else:
                    print(f'Wrong. The right answer is "{definition}"')
                    record_log(f'Wrong. The right answer is "{definition}"')
            num_asks -= 1


def main():
    card = Card()
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--import_from", help="import from a file")
    # parser.add_argument("--export_to", help="export to a file")
    # args = parser.parse_args()

    while True:
        inp = input("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n", )
        record_log(inp)
        
        if inp == "add":
            card.add()
        
        elif inp == "remove":
            card.remove()
        
        elif inp == "import":
            card.imp()
        
        elif inp == "export":
            card.export()
        
        elif inp == "ask":
            card.ask()
        
        elif inp == "log":
            file_name = input("File name:\n", )
            record_log("File name:\n" + file_name)
            
            with open(file_name, "w") as log:
                f.seek(0)  # change the stream position, a position of 0 starting at the top of the file
                shutil.copyfileobj(f, log)  # this transfers the content from one file to another
            
            print("The log has been saved.")
            record_log("The log has been saved.")
        
        elif inp == "hardest card":
            if len(list(card.mistake_store.values())) != 0:
                max_mistake = max(list(card.mistake_store.values()))
                max_mistake_term = []
                
                for k, v in card.mistake_store.items():
                    if v == max_mistake:
                        max_mistake_term.append(k)
                
                if len(max_mistake_term) == 1:        
                    print(f"The hardest card is {max_mistake_term[0]}. You have {max_mistake} errors answering it")
                    record_log(f"The hardest card is {max_mistake_term[0]}. You have {max_mistake} errors answering it")
                
                elif len(max_mistake_term) == 0:
                    print("There are no cards with errors.")
                    record_log("There are no cards with errors.")
                
                else:
                    max_mistake_term_string = ", ".join(max_mistake_term)
                    print(f"The hardtest cards are {max_mistake_term_string}")
                    record_log(f"The hardtest cards are {max_mistake_term_string}")
            else:
                print("There are no cards with errors.")
                record_log("There are no cards with errors.")

        elif inp == "reset stats":
            card.mistake_store = {}
            print("Card statistics have been reset.")
            record_log("Card statistics have been reset.")
        elif inp == "exit":
            print("bye bye!")
            record_log("bye bye!")
            break


if __name__ == "__main__":
    main()