# office_365_renaming_utility
A tool to rename files in a directory to fit the office 365 character limitations

This program will walk through all files underneath a given directory and rename them in order to fit the character limitations for OneDrive for Business.
Those requirements can be found at:
	https://support.microsoft.com/en-us/kb/2933738?wa=wsignin1.0
	
The program will replace characters based off the following dictionary:
	{"\\":"_","/":"_",":":";","*":"^","?":"_","\"":"_","<":"_",">":"_","|":"_","#":"_","%":"_","{":"(","}":")","~":"-","&":"_and_"}

Usage:

renaming_utility.exe "path you want to run on"


