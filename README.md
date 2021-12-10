### Applicant Info -- Requested Information from Recruiter Email 
Please include a current resume in .doc or .docx format in the zip file with your response.
•	Attached. 
Let us know your current work authorization status in the USA.
•	USA citizen 
And let us know your potential start date (we are prioritizing candidates that can start immediately.)
•	May 16, 2022

### Overall Approach 
My overall approach to use a dictionary to 
map a given locus with its corresponding coverage. 

From the read.csv file I take the starting position
and length and use it to iterate through all the loci
in the snippet. These are inserted into the dictionary
as keys. Its corresponding value is the number of times
I've seen the key.
This would have a runtime of 
O(m * n) where m is the number of reads and n 
is the length of each read.

Dictionary = key : locus | value : coverage 

Then in loci.csv I take the given position, access 
the dictionary, and output the corresponding 
coverage. Accessing the dictionary would be O(1) 
for each given position. So the runtime would be 
O(l), where l is the number of positions 
in the loci.csv file.

So the overall runtime of the program would be 
O(m*n) + O(l).

### Optimizations
Another approach I considered was to use an 
array instead of a dictionary. The performance would 
be better, but it would be more difficult to implement. 
Dictionaries have more overhead in terms of requiring 
more space and time. A dictionary would need more space 
because it has 3 pointers (key, value, and hash). It 
would also take more time because you have to create a
hash for each entry. So comparatively the dictionary 
is easier to implement but would not perform as well 
as an array. 

Doing the static array approach you'd create an int array such 
that each index represents a locus. Each index starts 
with a value of 0, then while processing through the length of the read
we increment the value of the corresponding index every time we see it. 
At the end, each index in the array would contain the 
coverage of its respectively locus.
The difficulty of implementing with this approach is you'd 
already need to know range of loci to create the static 
array. 

Another optimization that should be considered but is out 
of the scope of this problem is using Pandas, the python 
data analysis tool. This problem assumes the data given has 
already been cleaned and there are no invalid or missing values. 
Using Panadas would make it easier to address these concerns 
and make it simpler to work with large datasets by manipulating 
them as dataframes rather than reading and processing individual 
rows. However, because Panadas is a heavy framework it would not 
be sensible to use for this exercise. 
