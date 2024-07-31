import json
class Dictionary:
    def __init__(self,forget,remember):
        self.forget = forget
        self.remember = remember

    def choose(self,word):  
        while True:
            try:
                choice = int(input(""))
                if choice == 0:
                    print(self.forget[word])
                elif choice == 1:
                    meaning = self.forget.pop(word)
                    self.remember[word] = meaning
                break
            except ValueError:
                pass

    def review(self):
        while len(self.forget) != 0:
            for word in list(self.forget.keys()):
                print(word)
                self.choose(word)
                
def read_in():
    with open ("forget.json", "r", encoding="UTF-8") as f:
        forget = json.load(f)
    with open ("remember.json", "r",encoding="UTF-8") as r:
        remember = json.load(r)
    return forget,remember
    
def main():
    forget, remember = read_in()
    dictionary = Dictionary(forget, remember)
    dictionary.review()

if __name__ == "__main__":
    main()
