# HW Assignment #15
##### By: Jacob Ridlinghafer
###### 12/07/2020

#### Grade
3/3 - Nice work, glad you got it working.  These are great questions, hopefully we have time we can discuss them tomorrow. The short answer is that running a single for loop wont go much faster on these machines if you are just running on one core. It will just be the speed difference between that processor and whatever you have on your laptop. To get big speedups you need to divide your code up so it can run in parallel -- i.e. dividing the work up among multiple cores.  Also the exception to this is that running on one GPU can be much faster than running on one CPU if you have something that is optimized to take advantage of it. 

#Questions



1. What resources did you request on Ocelote? How long did you wait in the queue for your job to run and how long did it take to run?

I requested 1 node, 1 core, and 6gb of memory total. The queue was almost instant maybe like 2-3 seconds. It only took 5 seconds to run my entire script.

2. What was the most confusing part to you about setting up and running your job on Ocelote?

I had trouble with the windows not uploading the file properly so converting it to unix format was the only issue that I had.

3. Where else did you run your job? How did the setup compare to your run on Ocelote?

I ran my script on Google Collab the setup was almost exactly how you would run a jupyter notebook on your own computer. Although, it seemed a bit faster than my pc when running cells. This was much less complicated and was easy to set-up and use I had no issues with this setup.

4. What questions do you still have after doing this?

I am curious how fast this could run massive for loops, or our final project in modflow last semester cause that took like 5-10 minutes for one cell I remember. I am also curious to how changing to multicore usage would increase speeds.
