
# coding: utf-8

# In[1]:

#ハングマンのコード
#自力で全部書けた！！！
secret = ["a","p","p","l","e"]
secret_copy = secret 
word = []
count_correct = 0
count_wrong = 10

for i in range(len(secret)):
    word.append("_")
print(" ".join(word))


while True:
    x = input("アルファベットを入力してください：")
    if x in secret:
        count_correct += 1
        Index = secret.index(x)

        secret_copy[Index] = " "
        word[Index] = x

        print(" ".join(word))
        print("正解です")
        
        if count_correct == len(secret):
            print("クリア！")
            break
    else:
        count_wrong -= 1
        if count_wrong ==0:
            print("はずれです。ゲームオーバー！")
            break
        else:        
            print("はずれです：残り{}回".format(count_wrong))


# In[21]:

#文字列は不変なので、要素への代入は不可

word = "apple"
word[3]="e"


# In[13]:

import random
fruits = ["orange","banana","apple","cherry","grape","melon"]

fruit = fruits[random.randint(0,len(fruits)-1)]
secret = []
for n in range(len(fruit)):
    secret.append(fruit[n])
secret


# １．プログラム を 書き換え て、 答え の 単語 を リスト から ランダム に 選ぶ よう に しよ う。

# In[14]:

import random
fruits = ["orange","banana","apple","cherry","grape","melon"]

fruit = fruits[random.randint(0,len(fruits)-1)]
secret = []
for n in range(len(fruit)):
    secret.append(fruit[n])

secret_copy = secret 
word = []
count_correct = 0
count_wrong = 10

for i in range(len(secret)):
    word.append("_")
print(" ".join(word))


while True:
    x = input("アルファベットを入力してください：")
    if x in secret:
        count_correct += 1
        Index = secret.index(x)

        secret_copy[Index] = " "
        word[Index] = x

        print(" ".join(word))
        print("正解です")
        
        if count_correct == len(secret):
            print("クリア！")
            break
    else:
        count_wrong -= 1
        if count_wrong ==0:
            print("はずれです。ゲームオーバー！")
            break
        else:        
            print("はずれです：残り{}回".format(count_wrong))


# In[ ]:



