# Comparing-Page-Rank-Algorithms
Comparing Apache Solr's default search algorithm and page rank algorithm


Description:
-Created a user interface to accept the user query input and display the results similar to Googles search engine
-After the query is entered by the user, top 10 results along with a small snippet containing the query words.
-The user will have two options of using either a default Solr indexing or Page rank algorithm.

Steps followed-

Step 1: Installed Ubuntu on VMware ( Virtual Box lagged on my host machine)

Step 2: Installed the latest version of JAVA (jdk 1.8) and Solr (Solr 6.5.0). Started solr in standalone mode using the command bin/solr start 

Step 3: Created the core myexample using the command bin/solr create -c myexample. 

Step 4: Uncompressed the CNN data folder containing CNNDownloadData html file and stored it in the myexample folder. Indexed these documents using solr.

Step 5: Downloaded the latest version of PHP to create a user interface.

Step 6: Developed a solr.php front end interface with a search box where queries can
be entered. It has a checkbox if a user wants to search a query with PageRank Algorithm[descending order]. This is done by using the solr-php-client. The checkbox was added after the pagerank file was reloaded in the myexample folder.

Step 7: Developed a program in java (ExtractLinks.java) to extract the outgoing edges present in the html file and saving it in the CSV file called edges.csv   

Step 8: Created an external file[external_pagerank.csv] which contains the page rank
scores of the web pages, extracted from the zip provided to us.
a)	Installed NetworkX library in ubuntu using command “sudo apt-get install python-networkx”
b)	Created NetworkX graph(DiGraph) using the edges.csv file.
c)	Pass this NetworkX graph to the PageRank function. The parameters used for the PageRank function are as follows:
alpha=0.85,personalization=None,max_iter=30,tol=1e-06,nstart=None,weight='weight',dangling=None
d)  The pagerank function returns a dictionary of the form <id>=<pagerank score> and is written into external_pagerank.csv
e) This external_pagerank.csv is copied into the data folder of the myexample core(/server/solr/myexample/data/)
f) Made the necessary modifications to the managed_schema and solr_config.xml
g) The index is reloaded. Solr Dashboard> Core Admin> Reload

Step 8: Executed the given set of queries for both Solr Default and pagerank algorithms and generated the top ten results for each query. 

