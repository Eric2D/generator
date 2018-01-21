README

The Generator.

The idea behind the generator is to help keep the user from wasting time copying and pasting information from one place to another in great numbers or attempting to check large numbers of data with just a human eye. These programs are heavily pattern based. In order for the programs to work there must be a pattern for the system to work on.

So far there are working programs in this generator.

	1. The Replacer
	2. Search
	3. The Stripper


1. The Replacer




#########################################################################

2. Search

With Search you can find hundreds of items within a document in seconds and recieve clear results.

Place content to search in the please_find.txt file before running the program. When the program starts it will display the text in that file.

You will be asked "How many items would you like to search?" and this is where you input how many times you would like to search in that document.

The prompt will ask as many times as the number you entered, "What are you searching?". Depending on what kind of list you have the content can be copied and pasted all at once and the program will automatically enter accordingly. This method only works if the desired search phrases are in a list seperated by enter key spaces in a document or an excel list.

When the program is finished you can find your results in the Results.txt file. If you need to save the search results for any reason, be sure to take the content from the file and store it appropriately. The Search program will write over this file the next time it is run.





#########################################################################

3. The Stripper

The Stripper is a program that works in 3 parts. The Stripper searches through files, gathers the desired data, and pastes them in a new file.

First the files you would like data stripped from must be placed in the_data folder. Files that you are stripping data from should follow a pattern, otherwise the program will not be useful. For instance an html file has certain tags. If you would like the data between a couple of unique tags (unique on the file) that are on serveral other files as well then this program may be for you.

The program will ask you "Start search after?" and here is where you would input a specific phrase that is just before the content you want(this has to be true for every document). Then the program will ask "And the word just after the section?" and just like the before you want specific text just after the desired content.

After you enter in this information the program will run and print (in the terminal) a list of files in the order the program is working.

When the program finishes the results will be posted in the_results folder. If you run The Stripper again, the program will write over this file. Be sure to retreive the content before running The Stripper again.