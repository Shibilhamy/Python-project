import time
print(' There are total 4 questions. There is total 2 minutes to answer all the questions.'
      '\n You have to answer all of them. each answer has 1 point and no negative marks.' 
      '\n You have total 30 seconds to complete the quiz.')

remaining_time=120
def quit():
    if remaining_time<=0:
        print('-TIME OUT-')
        print('your total score is',point)
        print('remaining time',remaining_time)
        exit()


point=0
print()
print('Quiz starts in 5 seconds')
print()
time.sleep(5)
print('que 1:-Who is known as the "King of Pop"?','\n A) Elvis Presley',
        '\n B) Michael Jackson',
        '\n C) Prince',
        '\n D) Madonna')
current_time=time.time()
print()
user=input('Ans:-')
curr_time=time.time()
if user=='B':
    point=point+1
    print('Correct')
else:
    print('Wrong Answer')
    print('The correct answer is option B) Michael Jackson')
a=int(curr_time-current_time)
remaining_time=remaining_time-a
print('Remainig time =',remaining_time,'seconds')
quit()

print()
print('que2:-Which actress played the character Hermione Granger in the "Harry Potter" film series?',
      '\n A) Emma Stone',
'\n B) Emma Roberts',
'\n C) Emma Watson',
'\n D) Emma Thompson')
current_time=time.time()
print()
user=input('Ans:-')
curr_time=time.time()
if user=='C':
    point=point+1
    print('Correct')
else:
    print('wrong Answer')
    print('The correct answer is option C) Emma Watson')
b=int(curr_time-current_time)
remaining_time=remaining_time-b
print('Remainig time =',remaining_time,'seconds')
quit()

print()
print('que3:-Which actor played the character of Tony Stark in the Marvel Cinematic Universe?',
      '\n A) Chris Evans',
'\n B) Chris Hemsworth',
'\n C) Robert Downey Jr',
'\n D) Mark Ruffalo')
current_time=time.time()
print()
user=input('Ans:-')
curr_time=time.time()
if user=='C':
    print('Correct ')
    point=point+1
else:
    print('Wrong Answer')
    print('The correct answer is option C) Robert Downey Jr')
c=int(curr_time-current_time)
remaining_time=remaining_time-c
print('Remainig time =',remaining_time,'seconds')
quit()

print()
point=point/3*100
print('Score is',point,'%')