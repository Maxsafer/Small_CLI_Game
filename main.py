import threading
import time
import replit
from getkey import getkey
import random

class KeyboardThread(threading.Thread):

  def __init__(self, input_cbk = None, name='keyboard-input-thread'):
    self.input_cbk = input_cbk
    super(KeyboardThread, self).__init__(name=name)
    self.start()

  def run(self):
    while True:
      try:
        #self.input_cbk(input()) #waits to get input + Return
        self.input_cbk(getkey())
      except:
        exit()


def my_callback(inp):
  #evaluate the keyboard input
  #print('You Pressed:', inp)
  global letter
  letter = inp

#start the Keyboard thread
kthread = KeyboardThread(my_callback)
letter = ''
templist = ''
upList = ''
list1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
list2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
list3 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
list4 = [' ',' ',' ',' ',' ','▣',' ',' ',' ',' ',' ']
list5 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
list6 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
list7 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
lists = [list1,list2,list3,list4,list5,list6]
gamePoints = 0
exit = True

def printG():
  print(f'Points: {gamePoints}')
  print("_______________________")
  # print("|",list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8],list1[9],list1[10],"|")
  # print("|",list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7],list2[8],list2[9],list2[10],"|")
  # print("|",list3[0],list3[1],list3[2],list3[3],list3[4],list3[5],list3[6],list3[7],list3[8],list3[9],list3[10],"|")
  # print("|",list4[0],list4[1],list4[2],list4[3],list4[4],list4[5],list4[6],list4[7],list4[8],list4[9],list4[10],"|")
  # print("|",list5[0],list5[1],list5[2],list5[3],list5[4],list5[5],list5[6],list5[7],list5[8],list5[9],list5[10],"|")
  # print("|",list6[0],list6[1],list6[2],list6[3],list6[4],list6[5],list6[6],list6[7],list6[8],list6[9],list6[10],"|")
  # print("|",list7[0],list7[1],list7[2],list7[3],list7[4],list7[5],list7[6],list7[7],list7[8],list7[9],list7[10],"|")
  for list in lists:
    print("|",' '.join(map(str, list)),"|")
  print("-----------------------")

def movexr(list):
  global gamePoints
  position = list.index('▣')
  if list[position + 1] == 'o':
    gamePoints += 1
  list[position] = ' '
  list[position + 1] = '▣'
  
def movexl(list):
  global gamePoints
  position = list.index('▣') - 1
  if position < 0:
    exit()
  else:
    if list[position] == 'o':
      gamePoints += 1
    list[position + 1] = ' '
    list[position] = '▣'

def moveyu(list,listUp):
  global gamePoints
  position = list.index('▣')
  if listUp[position] == 'o':
      gamePoints += 1
  listUp[position] = '▣'
  list[position] = ' '
  
def moveyd(list,listUp):
  global gamePoints
  position = list.index('▣')
  if listUp[position] == 'o':
      gamePoints += 1
  listUp[position] = '▣'
  list[position] = ' '

#Objectives
def newObjective():
  if all('o' not in list for list in lists):
  # if 'o' not in list1 and 'o' not in list2 and 'o' not in list3 and 'o' not in list4 and 'o' not in list5 and 'o' not in list6 and 'o' not in list7:
    indNum = random.randint(0, len(list1) - 1)
    listX = lists[random.randint(0, len(lists) - 1)]
    if listX[indNum] != '▣':
      listX[indNum] = 'o'

#Driver code
while exit == True:
  newObjective()
  replit.clear()
  for x,list in enumerate(lists):
    if '▣' in list:
      templist = f'list{x+1}'
  # if '▣' in list1:
  #   templist = 'list1'
  # elif '▣' in list2:
  #   templist = 'list2'
  # elif '▣' in list3:
  #   templist = 'list3'
  # elif '▣' in list4:
  #   templist = 'list4'
  # elif '▣' in list5:
  #   templist = 'list5'
  # elif '▣' in list6:
  #   templist = 'list6'
  # elif '▣' in list7:
  #   templist = 'list7'
  printG()
  if gamePoints > 1:
    time.sleep(1/gamePoints+(1/gamePoints)/2)
  else:
    time.sleep(1)
  try:
    if letter == 'd':
      movexr(eval(templist))
      
    elif letter == 'a':
      movexl(eval(templist))
      
    elif letter == 'w':
      position = int(templist[-1]) - 1
      upList = (f'list{position}')
      moveyu(eval(templist),eval(upList))
        
    elif letter == 's':
      position = int(templist[-1]) + 1
      upList = (f'list{position}')
      moveyd(eval(templist),eval(upList))
  except:
    print('You lost')
    exit = False