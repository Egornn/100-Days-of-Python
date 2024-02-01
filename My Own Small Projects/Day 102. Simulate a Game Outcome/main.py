import random   

NAMES = ['Egor', 'Ilya', 'Misha', 'Pasha']
POINTS = {
    1:[1,0,0,0],
    2:[1,0,0,0],
    3:[2,1,0,0],
    4:[2,1,0,0],
    5:[3,2,1,0],
    6:[4,2,1,0],
    7:[5,3,1,0],
    8:[6,3,1,0],
    }

game_data = [[0,0,0,0] for _ in range(len(POINTS))]
    
for i in range(len(game_data)):
    if i == 0:
        game_data[i] = POINTS[i+1]
    else: 
        new_score  =  random.shuffle(POINTS[i+1]) 
        game_data[i]= [x+y for x,y in zip(game_data[i-1], POINTS[i+1])]              

game_data[-1].sort()
final_score = game_data[-1]
final_standings ={key:val for key,val in zip(NAMES,final_score)}

print(final_standings)
print()
print(game_data)
