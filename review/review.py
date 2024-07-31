import json
def review(forget, remember):
    for word in list(forget.keys()):
        print(word)
        forget, remember = choose(forget,remember,word)
    return forget, remember
        
def choose(forget,remember,word):
    while True:
        choice = int(input(""))
        try:
            if choice == 0:
               print(forget[word])
               return forget, remember
            elif choice == 1:
               forget, remember = remove(forget, remember, word)
               return forget,remember
            break
        except ValueError:
            pass
               
def remove(source, destination, word):
    meaning = source.pop(word)
    destination[word]=meaning
    return source,destination
def read_in():
    with open ("forget.json", "r", encoding="UTF-8") as f:
        forget = json.load(f)
    with open ("remember.json", "r",encoding="UTF-8") as r:
        remember = json.load(r)
    return forget,remember
    
def main():
   forget, remember = read_in()
   while len(forget) != 0:
        forget,remember = review(forget,remember)

if __name__ == "__main__":
    main()