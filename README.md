Following Makers' workshop on Algorithmic Complexity
https://github.com/makersacademy/course/blob/master/algorithmic_complexity/README.md

Using matplotlib python library to display data.

Testing with unittest:
```
python tests.py
```

A module called 'timer' is included for timing functions. Usage:

```
from timer import timer
stopwatch = timer.Stopwatch()
stopwatch.measure(lambda: your_function(arguments))
```

E.g.:

```
>>> from random import shuffle
>>> from timer import timer
>>> list = []
>>> for i in range(1000):
...     list.append(i)
>>> stopwatch = timer.Stopwatch()
>>> stopwatch.measure(lambda: shuffle(list))
1.1905910469067749e-05
```

Also try:

list.sort()
list[-1]
list.reverse()

Using matplotlib:
https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/