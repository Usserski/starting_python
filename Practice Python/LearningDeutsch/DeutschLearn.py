import random
def readIO():
    with open('Baza.txt' , 'r' ) as file:
        Polnisch_words = [ ]
        Deutsch_words = [ ]
        for line in file:
        
         parts = line.strip().split('-')
        
         if len(parts)== 2:
            
                Polnisch_words.append(parts[0])
                Deutsch_words.append(parts[1])
        else:
                print(f"Error: Not correct format line in file")

    return (Polnisch_words , Deutsch_words)


def main():
    
    readIO()
    
     
    

main()