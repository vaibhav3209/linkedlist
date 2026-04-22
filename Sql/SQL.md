## 📋 ***List of Topics***:
[Topic A](#topic-a) |
[question practice](#question-practice--topic-a)


[Topic B](#topic-b) |
[question practice](#notes-from-question-practice-topic-b)


## ***Interview Questions*** 
> Note:
> 1. While practicing explain your answers 
> like voice typing on keyboard , SEND ans. to AI .....
> 2. Always ask question "Is this Optimized?" , "How many 
> rows it's fetching?"  **"How will this query handle NULL ?"**



### Topic A
- Theory
##### question practice - Topic A




### Topic B
- Theory 
- ##### question practice - Topic B


## Notes from Question Practice

--------------------------------------------------------------------
--------------------------------------------------------------------

Problem set 1  Hackerrank:(First 6 questions)
https://www.hackerrank.com/challenges/revising-the-select-query/problem

Solution: 

``` sql

SELECT *
FROM CITY
WHERE POPULATION > 100000
  AND COUNTRYCODE = 'USA';

``` 

1.     How would the Order of Conditions optimise the query?

Ans.  For the output the order doesn't matters (AS sql is NOT 
EXECUTED top to down).

but the thinking of filtering country first is better optimised.


2.     What would change if the population column has NULL?

MY ans. (Wrong)==>> ZERO rows returned. 

Correct ans. ==>> The situation which become NULL > 100000 will
get skipped rest will be fetched.

3.     How would you apply indexing for query optimisations?

Ans.   Composite indexes of (Country code, population).
Country code will check equality and then population Will 
be a ***Range checker***

4.     which is better ''SELECT *''  or ''SELECT col1,col2'' ?

Ans.  When we write SELECT * ==>> Database reads all columns 
from the disk.

But when we write ***SELECT name,population***:
    
- less data is read from disk
- less data is sent over network
- less memory usage



```
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'USA'
  AND POPULATION > 120000;
```

1.      Will the same index work now when the population has changed?

Ans.  Yes, the same composite index on (countrycode, population) 
can be used for filtering. 

Additionally, if we extend the index 
to include NAME, the query can become index-covered and avoid table lookups.


2.      Follow up:: Will you add a new index everytime you write a new
        query then? Like you are doing above case.

When to add indexes : 
- if query runs frequently
- performance matters
- read >> write workload

Trade offs:
- More storage
- Slower writes (INSERT/UPDATE)


3.      What if this query runs many times per day?

Ans. 
- indexing(It's just the start.)(Don't say it abruptly)
- Cache (Redis, Memcached) to reduce Db hits
- create VIEW / CTEs precomputed tables 
- If USA is mostly searched then we create partitions. So
only that part is scanned. 
- ***Read REPLICAS***: One db to handle writes , multiple read 
replicas(Horizontal scaling).


--------------------------------------------------------------------
--------------------------------------------------------------------