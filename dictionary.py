import json
import difflib

#Store the data in the JSON file in the variable data
data = json.load(open('data.json', 'r'))

#Method that takes a parameter (word provided by user) and finds it in the dictionary
def search(word):
    
    #if word in data return the definition in the dictionary
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    #else compare using method get_close_matches in order to find the closest word
    else:
        lista = difflib.get_close_matches(word,data)
        
        #lista variable is a list and if the length is 0 then the method couldn't find a closest word
        if len(lista)>0:
            #show to user the most similar word
            answer = input('Did you want to type ' + lista[0] + '? Y/N: ')
            if answer.lower() == 'y':
                return data[lista[0]]
            #if users type N then the program ends
            elif answer.lower() == 'n':
                return 'Try again(Intentalo de nuevo)'
            #if response is different than N or Y program ends    
            else:
                return 'That is not the correct answer, ending program'
                    
        else:
            
            return 'Unable to find the word'
    
while(True):
    w = input('Type a word (type Q to end the program): ')
    w.lower()
    if w == 'q':
        break
    
    #store output in a variable
    output = search(w)
    
    #if the output contains more than one definition will be stored in a list, then we print out every item in that list
    if type(output)==list:
        print('\n')
        for item in output:
            print(  item + '\n')
    else:
        print(output)

#userInput = input('Press any key to finish')
