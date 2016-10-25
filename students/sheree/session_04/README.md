http://uwpce-pythoncert.github.io/IntroToPython/session04.html#homework

### Recommended Reading:

- Dive Into Python: Chapt. 13,14

### Assignments:

- Finish the dict/sets lab
- Finish the Exceptions lab
- Coding kata: trigrams
- Paths and files
- Update mailroom with dicts and exceptions


### Text and files and dicts, and...
Coding Kata 14 - Dave Thomas

	http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/

	and in this doc:

	Kata Fourteen: Tom Swift Under Milk Wood

	and on github here

	http://uwpce-pythoncert.github.io/IntroToPython/exercises/kata_fourteen.html

Use The Adventures of Sherlock Holmes as input:

	./exercises/sherlock.txt

	and on github here:

	http://uwpce-pythoncert.github.io/IntroToPython/_downloads/sherlock.txt

This is intentionally open-ended and underspecified. There are many interesting decisions to make.
Experiment with different lengths for the lookup key. (3 words, 4 words, 3 letters, etc)

### Paths and File Processing

write a program which prints the full path to all files in the current directory, one per line
write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)

	advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
	Note that if you want it to do any kind of file, you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing.)

update mailroom from last week to:

	Use dicts where appropriate
	Write a full set of letters to everyone to individual files on disk
	See if you can use a dict to switch between the users selections
	Try to use a dict and the .format() method to do the letter as one big template – rather than building up a big string in parts.