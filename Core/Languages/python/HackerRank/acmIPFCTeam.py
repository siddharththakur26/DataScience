topic = ['10101', '11100', '11010', '00101']

team=[] 
for i in range(0,len(topic)):
    team1 = int(topic[i])
    for j in range(i+1,len(topic)):
        team2 = int(topic[j])
        addition = team1 + team2
        team.append(str(addition))
knowledge = []
for i in team:
    numberofZeros = i.count('0')
    length = len(i)
    knownKnowledge = length - numberofZeros
    knowledge.append(knownKnowledge)
maxKnowldge =  max(knowledge)
print maxKnowldge
print knowledge.count(maxKnowldge)
