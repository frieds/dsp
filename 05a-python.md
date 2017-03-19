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
 `[1, 2, 2, 4, [1, 2], {1: 1}]`
 An example of a set:
  `{1, 2, 4}`
 Generally you'll get better performance for finding an element in a set versus a list if you're just searching for
 membership. The reason for this is sets are implemented using hash tables; so in the background there'd be a search for 
 the object determined by its hash, and this operation's performance does not depend on size of the set. To search for 
 membership in a list, up to the whole list may need to be search, which will take an awful lot of time as the list 
 grows.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

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





