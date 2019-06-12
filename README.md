
For Makers' workshop on Algorithmic Complexity
https://github.com/makersacademy/course/blob/master/algorithmic_complexity/README.md

Using matplotlib python library to display how algorithms perform with different N (so that you can see what kind of Big-O notation might be at play).

## Before running

Make sure you have installed requirements in e.g. a virtual environment and activated it.

Testing with unittest:
```
python -m unittest discover -s <directory>
```

Using matplotlib:
https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/

## Using

>>> from algorithms import generate_data, plot
>>> dg = generate_data.DataGenerator()
>>> x_data, y_data = dg.time_with_various_n(
...     function=lambda list: list.sort()
... )
>>> pl = plot.Plotter()
>>> pl.plot(x_data, y_data)
'C:\\Users\\David\\Desktop\\projects\\algorithms\\plots\\1560338967.574717.png'

# Goals for project

Become conversant in algorithmic complexity; be able to use this knowledge to write efficient code.

Host the algorithmic timer and graph-plotter on a website (possibly just for local hosting due to security issues with running strangers' code)

Stretch goal: apply supervised machine learning of to the timing output so that the app can suggest the likely curve of the graph (with % confidence)