import time
String='Hello! How are you?'
wordcount=len(String.split())
a= "Y"
while a != "N":
    t0=time.time()
    print(String)
    inputtext=str(input('Enter the sentence:'))
    t1=time.time()
    accuracy=len(set(inputtext.split())&set(String.split()))
    accuracy=accuracy/wordcount
    timetaken=t1-t0
    wpm=wordcount/timetaken
    print("WPM",wpm*100,"Accuracy",accuracy*100,"Timetaken",timetaken)
    a = input("Do you want to continue Y or N? ")