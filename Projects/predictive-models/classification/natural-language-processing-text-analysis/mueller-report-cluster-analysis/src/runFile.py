import csv
import re
from gensim.models import Word2Vec
import numpy as np 
import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

'''
TASK:
Have to cluster sentences from the Mueller report to get optimal number of clusters.
'''

lines = list()

##### Data Pre Procesing #####
'''
Opening the csv file in  and reading each row and storing only text values in a list.
'''
with open('muller_report.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    count =0
    for row in reader:
        if count > 207:
            lines.append(row[2])
        count +=1
#print (len(lines))
'''
Form sentences from text value stored in the list
'''
sentences = list()
for i in lines:
    sentences.append(i)
    
sentence_formation =  (' '.join(sentences))

#print(sentences)
#print(''.join(sentences))
'''
Create list of sentences i.e every element of list is one whole sentence
'''
sentence_segment= sentence_formation.split('.')
sentence_segement_final=[]
for segment in sentence_segment:
    if len(segment)>3:
        sentence_segement_final.append(segment)
#print(sentence_segement_final)

sentences_processed =[]
'''
1. Remove special characters
2. Remove Extra Spaces
3. Lower case all the sentences
4. Remove strings less then equal to 3 characters phrases
'''
for i in sentence_segement_final:
    temp_alphanum_only =re.sub('[^a-zA-Z0-9.]', ' ', i)
    temp_alphanum_singleSpaces_only = re.sub(' +', ' ',temp_alphanum_only)
    temp_final = temp_alphanum_singleSpaces_only.lower()
    sentences_processed.append(temp_final)
    
#print (sentences_processed)


##### Sentence Embedding #####
'''
Word2Vec model is used. It is true that this model. Each sentences is tokenized, after that 
each word is summed based on number of occuracnces in a sentence. Finally, the sum is divided
by total number of words in the sentences. This allows to do sentence embedding
'''
sentences_tokens =[]
for segment in sentences_processed:
    temp_segment = segment.split(' ')
    sentences_tokens.append(temp_segment)
#print(sentences_tokens)

model = Word2Vec(sentences_tokens,min_count=1)
'''
returns array value of each sentences
'''
def sentence_vectorization(sentences_segment,model):
    sentence_vector=[]
    word_count=0
    for word in sentences_segment:
        try:
            if word_count==0:
                sentence_vector = model[word]
            else:
                sentence_vector = np.add(sentence_vector,model[word])
            word_count +=1
        except:
            pass
    return np.asarray(sentence_vector)/word_count
sentence_value=[]
for segment in sentences_tokens:
    sentence_value.append(sentence_vectorization(segment,model))

#print(sentence_value)

##### Clustering Analysis #####
'''
Analysing optimal number of clusters. Use of dendogram to visualize a graph between 
dissmiliar  vs distance value. Hence, reduce the dissimilarity to form the cluster. 
Priority is to reduce dissimilar value to the least and able to form cluster
'''

Z = shc.linkage(sentence_value,'ward')
dendogram = shc.dendrogram(Z)
plt.title("dendograms")
plt.ylabel('Dissimilarity Value')
plt.xlabel('Euclidean Distance')
plt.show()

# No of Optimal CLusters would be 4 or 5. I have choosen 5.

'''
Hierarchial clustering

Each object in a separate cluster. At each step, the two clusters that are most similar are joined 
into a single new cluster.Once fused, objects are never separated.
'''

clusters = AgglomerativeClustering(n_clusters=5,affinity='euclidean',linkage='ward')
predict = clusters.fit_predict(sentence_value)
cluster_dictionary={}

for index,sentence in enumerate(sentences_tokens):
    key = predict[index]
    cluster_dictionary.setdefault(key,[])
    cluster_dictionary[key].append(sentence)

print(cluster_dictionary)   


with open('cluster.txt', 'w') as f:
    print(cluster_dictionary, file=f)
