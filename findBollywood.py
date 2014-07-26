from bs4 import BeautifulSoup
import requests

def findMatch(year,noOfWords,noOfLetters):
    #noOfLetters is a list that should have no of letters in each word
    #year = str(year)
    movieList=[]
    newList=[]
    r = requests.get('http://en.wikipedia.org/wiki/List_of_Bollywood_films_of_'+year)
    link = r.text.encode('ascii','ignore')
    r.close()
    soup = BeautifulSoup(link)
    findTable = soup.findAll('table',{'class':'wikitable'})
    #print findTable
    for tables in findTable:
        movieGrid = tables.select('tr td i')
        #print movieGrid
        for name in movieGrid:
            movieList.append(name.text)
        filteredList = filter(lambda x:len(x.split(' '))==noOfWords,movieList)
        movieList=[]
        if noOfLetters:
            for each in filteredList:
                value = True
                iterator = 0
                movieName = each.split(' ')
                for split in movieName:
                    if len(split)==int(noOfLetters[iterator]) or len(split.replace('!','').replace('.','').replace('-',''))==int(noOfLetters[iterator]): #removie !,.,- from string and find if it matches with provided length
                        value = value and True
                    else:
                        value = False
                    iterator = iterator+1
                if value:
                    movieName = each.encode('ascii','ignore')
                    newList.append(movieName)
        
    print newList

if __name__=='__main__':
    uInput = 'y'
    while uInput == 'y':
        year=str(raw_input('enter the year: '))
        noOfWords=int(raw_input('enter no of words: '))
        noOfLetters = raw_input('input no of letters in each word separated by comma: ')
        noOfLetters = noOfLetters.split(',')
        print 'Year: '+year
        print 'No of Words: '+str(noOfWords)
        print 'No of Letters: '+','.join(noOfLetters)
        findMatch(year,noOfWords,noOfLetters)
        raw_input()
        uInput = raw_input('do you want to continue: y/n: ').lower()
    
    
