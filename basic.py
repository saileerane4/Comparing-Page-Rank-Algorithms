import networkx as nx
import csv

G = nx.DiGraph()
# with open("edges1.csv", "rb") as f:
edgeList = list()
for line in open("edges1.csv"):
    csv_row = line.split(";")
    edgeList.append((csv_row[0].strip(), csv_row[1].strip()))
    # print(csv_row[0] + " : " + csv_row[1])
print("Done reading the csv file")
H = nx.DiGraph(edgeList)
print("Graph created")
print(H.number_of_nodes())

pr = nx.pagerank(H, alpha=0.85, max_iter=30, tol=1e-06, nstart=None, weight='weight', dangling=None, personalization=None)
print()
csv_file = open('external_pagerank.csv', 'w+')
for i in pr.keys():
    csv_file.write("/home/saileerane10/Desktop/solr-6.5.0/server/solr/myexample/CNNDownloadData/"+str(i) + "=" + str(pr[i]) + "\n")

print("Done writing page ranks")
