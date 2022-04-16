#by www.youtube.com/OmegaGamerLol
import time
import random
time.sleep(5)
print('*splash*')
time.sleep(5)
print('?: Huh')
time.sleep(2)
print('?: where am i')
time.sleep(3)
print('?: it is cold down here')
time.sleep(1)
print('?: like')
time.sleep(1.24)
print('?: really cold')
time.sleep(3)
print('you: who are-')
time.sleep(0.25)
print('?: Holy shit holy-')
time.sleep(0.25)
print('?: fuck')
time.sleep(0.25)
print('?: wtf holy yoggeret')
time.sleep(2.5)
print('?: holy shit you scared me')
time.sleep(1.75)
print('?: wait')
time.sleep(3.5)
print('?: who the hell are you')
time.sleep(2)
print('(no seriously, who the hell are you?)')
PlayerName = input()
print('?:' + PlayerName + '?')
time.sleep(2)
print('?: wow')
time.sleep(3)
print('?: that name is a stupid ass name xD')
time.sleep(4)
print('?: Major')
time.sleep(2)
print(PlayerName + ': what?')
time.sleep(2)
print('?: My name is Major')
time.sleep(2)
print('Major: Major Baby')
time.sleep(2)
print('Major: friends call me May May')
time.sleep(2.8)
print('Major: i got turned into a fucking dog man. A friggin furry!')
time.sleep(4)
print('Major: damn witch')
time.sleep(1.5)
print('Major: she turned my mom into a dog 2 months into pregancy')
time.sleep(2)
print(PlayerName + ': who?')
time.sleep(5)
print('Major: Black Kitty')
time.sleep(2)
print(PlayerName + ': who is tha-')
time.sleep(1.2)
print('Major: not important')
time.sleep(3)
print(
    'Major: anyways here is a rock')
time.sleep(2.8)
print(PlayerName + ': what? why would I need that?')
time.sleep(2)
print ('Major: I need you to hunt down some Lesser Mama Kitties. Keep hunting until one drops a key. I saw one with a key. Find one in the basement')
time.sleep(10)
print('2 new portraits unlocked')
print(
    'portraits will be accessible in the folder named "Portraits" in the full game'
)
time.sleep(5)
print('Quest unlocked: The Wells basement')
#Second half
#declaring varibles for later use
import time
import pygame
import math
import random
Monster = random.randint(1, 1000)
Hunt = 69420
Rock = 'Rock'
Damage = 0
#bad coding skill mistake L
#def var 'Player_Health'
#def var 'Monster_= Health'
Monster_Health = int(100)
Player_Health = int(100)
ItemSlot = Rock
time.sleep(3)
print ('                                                                                            Hunt for Lesser Mama Kitty and find a key')
print ('                                                                                            To continue type "c"')
print ('                                                                                            For monster info type "i"                                                                                    ')
Hunt = input()
if Hunt == 'i':
  
  print ('                                                                                            Lesser Mama Kitties are weaker versions of Mama Kitty and much weaker versions of Greater Mama Kitties. Lesser Mama Kitties have 100 Hit points (HP) which is equal to that of the     player ('  + str(PlayerName) + ') with no items. They have a 3/10 chance of spawning. This is the tutorial monster. Fun Fact: a picture of Mama Kitty can be found in the files ') 
  time.sleep(23)
  print ('                                                                                           Hunt for Lesser Mama Kitty and find a key')
print ('                                                                                           Hunt for monster with "h"')
Hunt = input()
while Monster < 700:
  Monster = random.randint(1, 1000)
if Monster < 700:
    while Monster < 700:
      print ('Rehunting (found nothing)...')
    time.sleep(2)
    Monster += 1  
else:
    if Monster > 700:
      print('                                                                                                  You ran into a(n) Lesser Mama Kitty')
    time.sleep(3)
    print ('                                                                                            Type 1 to use your item: ' + str(ItemSlot) +  ' | Your HP: ' +  str(Player_Health) + ' | Opponent HP: ' + str(Monster_Health) )
Fight_1 = input()
if Fight_1 < '2':
  Damage = random.randint(16, 20)
  critical = random.randint(1, 50)
  Monster_Health = Monster_Health - Damage
if critical == 13:
  Monster_Health = Monster_Health - 20%Damage
  time.sleep(2)
  print ('You landed a critcal hit!(adds 20% more damage to your total damage)')
  time.sleep(3)
if Monster_Health > 0:
      print ('You used a rock. The lesser Mama Kitty is at ' + str(Monster_Health) + '. You dealt ' + str(Damage) + ' Damage!')
if Monster_Health < 1:
  print('You knocked out a Lessar Mama Kitty')
else:
  print ( 'Your HP: ' +  str(Player_Health) + ' | Opponent HP: ' + str(Monster_Health) )
  time.sleep (2)
  print('The Lesser Mama Kitty uses her claws')
  MDamage = random.randint(5, 17)
  time.sleep (2)
  print ( str(PlayerName) + 'is now at ' + str(Player_Health) + 'Lesser Mama Kitty does ' + str(MDamage) + ' damage!')
  
time.sleep(15)