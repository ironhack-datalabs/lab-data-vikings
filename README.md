# Lab | Vikings (lab-data-vikings)

## Introduction
The Vikings and the Saxons are at War. Both are Soldiers but they have their own methods to fight. Vikings are ported to Python. YAY!!

In this laboratory you will work with the concept of inheritance in Python. 

### Getting Started
Modify the file ```vikingsClases.py``` so that all the tests are correct.
### Challenge Question

### Bonus Question


## Tests
To run the battery of tests you must enter the following command line through the terminal. 
```
% > python3 tests.py -v
```

### Correct Test
When the tests are all correct you will receive the following message in the terminal. 
```
% > python3 tests.py -v

testSaxon (__main__.MyTest) ... ok
testSoldier (__main__.MyTest) ... ok
testViking (__main__.MyTest) ... ok
testWar (__main__.MyTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
### Failed Test
When some test is incorrect you will receive the following message in the terminal. It means that you must keep making changes in the ```vikingsClases.py``` file.
```
$ > python3 tests.py -v

testSaxon (__main__.MyTest) ... FAIL
testSoldier (__main__.MyTest) ... ok
testViking (__main__.MyTest) ... ok
testWar (__main__.MyTest) ... ok

======================================================================
FAIL: testSaxon (__main__.MyTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests.py", line 53, in testSaxon
    self.assertEqual(len(signature(Saxon).parameters), 2)
AssertionError: 3 != 2

----------------------------------------------------------------------
Ran 4 tests in 0.002s

FAILED (failures=1)
```

## Deliverables

* REQUIRED: vikingsClases.py modified with your solution to the challenge question.
* OPTIONAL: tests2.py with your solution to the bonus question.


## Submission


## Resources

* https://docs.python.org/3/library/unittest.html

## Additional Challenge for the Nerds
You can try to make your own tests for your code. 
