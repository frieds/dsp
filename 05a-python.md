# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples both can store a sequence of values. In both lists and tuples, you can index the values by
integers and you can use the slice operator to get a range of elements. In both, the values can be of any type. In both,
 you can nest additional sequences inside. However, lists are mutable - so the values can be changed after the list is 
 declared. However, tuples are immutable - so the values inside cannot be modified.  Lists cannot be used as keys in a 
 dictionary because lists are mutable. So the issue would arise if you had a list as a key in a dictionary, and since 
 that list is mutable, you'd try to change it. However, when you change the key, that key is now in the wrong bucket 
 as originally intended and a KeyError would occur.  When Python tries to implement a hash table for your dictionary 
 with a list as a key, you'll immediately get a TypeError that the type *list*, as the key, is unhashable. However, 
 tuples can be used as keys in a dictionary because they are immutable.  

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists are different than sets in that lists are ordered collections and can contain duplicate elements. Lists support
indexing and slicing. Lists can contain any date type while sets cannot contain mutable objects such as lists and 
dictionaries. Unlike lists, set objects support many mathematical operations such as union, intersection,
 difference and symmetric difference.
 An example of a list: 
```
[1, 2, 2, 4, [1, 2], {1: 1}]
```
>>An example of a set:
```
{1, 2, 4}
```
>> Generally you'll get better performance for finding an element in a set versus a list if you're just searching for
 membership. The reason for this is sets are implemented using hash tables; so in the background there'd be a search for 
 the object determined by its hash, and this operation's performance does not depend on size of the set. To search for 
 membership in a list, up to the whole list may need to be search, which will take an awful lot of time as the list 
 grows.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's *lambda* is a tool for building functions. *Lambda* also allows you to pass the body of functions to other
 functions without using the *def* keyword. Using *lambda* can be a more concise way of implementing a function rather 
 than writing two distinct functions using the *def* keyword. However, *lambda* should only be used for complex one-time 
 anonymous functions in your scripts. Below is an example of a miniaturized phone book that 
 records people's names (first and last) along with their phone number. We can sort the phone book by people's first names.
```
>>> phone_book = {('Friedman', 'Daniel'): 5551234567, ('Cohen', 'Jake'): 5551245363, ('Strauss', 'Amanda'): 5533233235}
>>> sorted(phone_book.items(), key=lambda x: x[0][1])
[(('Strauss', 'Amanda'), 5533233235), (('Friedman', 'Daniel'), 5551234567), (('Cohen', 'Jake'), 5551245363)]
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension provide a concise way to create lists. You can create a list comprehension statement in one line,
while the alternative may be to create a multi-line function with the def keyword. However, list comprehension are 
more difficult to debug because you can't add a print statement inside the body. Let's say we want to create a list
of all the numbers evenly divisible by 3 from 0 to 20. We can use list comprehensions:
```
>>> [x for x in range(0, 20) if x%3==0]
[0, 3, 6, 9, 12, 15, 18]
```
>> We can also use the filter function. This built-in Python function constructs an iterator from those elements of the
iterable for which our function would return true. So in our example, we'll only return elements whose remainder is 0
when divided by 3.
```
>>> list(filter(lambda x: x%3==0, range(0,20)))
[0, 3, 6, 9, 12, 15, 18]
```
>>> Here's another example of a list comprehension in which we create a list of tuples with a pair of #, square
```
>>> [(x, x**2) for x in range(0,6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```
>>> We can do the same thing with lambda and the map function. The map function is a built in Python function that
applies a specified function to each element in our iterable, in our case the range of 0 to 6. The lambda function
 creates an inline function in a single expression. The value of this expression, in our case a tuple of (x, x**2) 
 is what the function returns when invoked.
```
>>> list(map(lambda x: (x, x**2), range(0,6)))
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```
>>>In the instances above that we use lambda, we do a function call in order to calculate each list item. This would cause
our statement to run rather slow. By comparison, the first list comprehension example is much faster.
 [Guido recommends](https://www.python.org/doc/essays/list2str/) to avoid calling lambda inside loops so our last
  example with map and lambda is likely to have a slower runtime than the corresponding list comprehension. Generally 
  using map(), filter() or reduce() with a built-in function is faster than a for loop with in-line code though. The map 
  function is a built in Python function that applies a specified function to each element in an iterable. 
>>> Sets are an unordered collection with no duplicate elements. Set comprehensions are constructed using the same 
principles as list comprehensions; however, the resulting sequence is a set. Here's an example:
```
>>> b = {x for x in 'comprehensions' if x not in 'oei'}
>>> b
{'p', 'r', 'n', 's', 'c', 'h', 'm'}
>>> type(b)
<class 'set'>
```
>>> Dictionary comprehensions evaluate to a dictionary. Remember the example from above that created a list of tuples, 
inside each tuple a (number, number&ast;number). We can create something similar using a dictionary comprehension. Note 
below how x: x&ast;&ast;2 is in the format of a key:value pair while using the list comprehension expression above, we used
(x, x**2) to generate tuples instead.
```
>>> c = x: x**2 for x in range(0,6)}
>>> c
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> type(c)
<class 'dict'>
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





