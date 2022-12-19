from random import randint
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Sum, Avg, RandomIntSum, RandomIntMed, Ans')
pyDatalog.create_terms('Summary, Range, Length, ListSummary, List, Median')

(Summary[Range] == sum_(X, for_each = X)) <= X.in_(range_(Range + 1))
(Length[Range] == len_(X, for_each = X)) <= X.in_(range_(Range + 1))
RandomList = [randint(0, 99) for _ in range(0, 100)]
RandomList.sort()
(ListSummary[List] == sum_(X, for_each = X)) <= X.in_(List)
(Ans == Median[List]) <= (Ans == (List[49] + List[50]) / 2)

print(Sum == Summary[8])
print()
print(Avg == (Summary[8] / Length[8]))
print()
print(RandomIntSum == ListSummary[RandomList])
print()
print(RandomIntMed == Median[RandomList])
