The python book is pretty straight forward just make sure to read comments as you go if you have trouble understanding how things were done.
Note: make sure that
filename = 'streamflow_week6.txt'
filepath = os.path.join('../../data', filename)
is changed to where you keep it and to 'streamflow_week7.txt' so you get this assignments predictions not lastweeks.

- Week 1 forecast submission values: 74.019 cfs

- Week 2 forecast submission values: 82.82 cfs


### Reviewer: Lourdes Fierro

## Forecast values
- Week 1 forecast regression based: 74.019 cfs

- Week 2 forecast regression based: 82.82 cfs

- Week 1 forecast submission values: 74.019 cfs

- Week 2 forecast submission values: 82.82 cfs

Since instructions are not provided, I assumed that the submission values for this week are the same as the regression based values.

## Questions to consider
### 1. Is the script easy to read and understand?
- Are variables and functions named descriptively when useful? Most of them were easy to understand, but very few could have had a more descriptive (intuitive) name, but they do followed the lower case naming convention. I think the variable data_to_plot name is a little ambiguous, it could have a name related to its function such as outlier_grtr_aug or something like that :D.
- Are the comments helpful? Most of the comments helps to understand the code structure, but there are a few sections where a little more description could have been helpful to get the purpose of the cell code in a more instinctive and faster way. For example, I was not sure why   *lastweek.append(prediction)* variable is used. I would add something that gives a little more of detail on how the values are being added.   
- Can you run the script on your own easily?: It was not complicated to run it, but the path to the data file needed to be changed. I included a note at the bottom of the file about this point. besides that, the code ran smoothly :). I liked the plots.
- Are the doc-strings useful? Doc-strings are not presented inside the *lo_hi* function :( .
### 2. Does the code follow PEP8 style consistently?
 - If not are there specific instances where the script diverges from this style? Overall, you did a great job in this section :)
### 3. Is the code written succinctly and efficiently?
- Are there superfluous code sections?: Overall, the code is straight forward and it uses all variables that are created :D. Once I understood the append section, I really liked what it does.
- Is the use of functions appropriate? I'm not sure if the function is useful for the code purpose. I think it describes if your prediction values are lower or higher than 75, but it's not clear where does this value come from, and how this information affects the forecast. I would add some comments about how you set the threshold. Another option could be to use the function to set a condition where it is decided if the forecast obtained is good to go or not, and maybe submit other value instead of the "bad one".
- Is the code written elegantly without decreasing readability? The code is overall clear, and I liked its simplicity. I would just like to mention that there are some sections that are a little more difficult to spot since the spacing between sections is slightly inconsistent ( sometimes lines are used to separate the sections, but sometimes there aren't any).  I'm not sure how elegant it is since I'm not an expert coder, but I think it looks good :D.

* A few points from the assignment's instruction were not completely followed, such as:
- *Double check before you submit that the script can run directly from this folder and that you have the path to your data and functions setup correctly so that your peer review partner can run it without making any adjustments*
- *The space to provide comments and scores in the ReadMe.md file*

* Readability: 2/3 (No doc-strings are included)
* Style: 3/3
* Code Efficiency: 3/3
