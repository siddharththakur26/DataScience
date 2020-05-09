''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    testcases = int(input())
    
    result = []
    while testcases > 0:
        number_players = int(input())
        players_info=[]
        for i in range(number_players):
            players_info.append(input())    
        
        players_ratings=[]
        for i in players_info:
            players_ratings.append(i.split(' '))
        
        #print(players_ratings)
        player_ratings_dict={}
        for i in players_ratings:
            key = int(i[1])
            player_ratings_dict[key] = []
        
        for i in players_ratings:
            player_ratings_dict[int(i[1])].append(i[0])
        
        #print(player_ratings_dict)
        values = sorted(player_ratings_dict.keys(),reverse=True)
        #print(values)
        for i in values:
            result += player_ratings_dict.get(i)
        
        testcases -=1

    #print()
    for i in result:
        print(i)
    print(end='')
    


 # Write code here 

main()

