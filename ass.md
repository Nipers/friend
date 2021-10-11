### Problem 1

#### A

For Approach 1, because of the function, there is no difference between critical and uncritical requests, so in the worst case, the number of comparisons that have to be performed is O(log(m0 + m1)). 

For Approach 2, to insert a request, we need to know which type it is, if critical, we need to compare at most log(m0) times, else log(m1). To eject the next request, we can get the top of two heaps can compare two request, then pop the more urgent one. So in the worst case we need 1 + log(max(m0, m1)) comparisons. So the complexity is O(log(m)), m is the bigger one between m0 and m1.

So they are the same complex asymptotically, but I think in the worst case Approach 2 may cost more comparisons, because 2 * max(m0, m1) > m0 + m1.

#### B

```
function HeapUpdate(H, rold, rnew)
	begin <- 1
	end <- H.size()
```

