# SpeechTechAssignment - The Problem
Git repo for the Speech Technology Windows fix. For this fix it was necessary to install two new modules Colorama and Windows Unicode Console. Since the November update, the stdout.write function in Python has not been working properly dues to not being able to handle the changes in the unicode length change in Windows.

[More information can be found in this link](https://github.com/Microsoft/vscode/issues/39149)

The error primarily occur when sequences of prints are being interrupted by the user (either highlighting text or scrolling up and down while the script is printing), which I believe is preventing cmd.exe to properly flush the text and accumulating thewrite bytes. Apparently, this problem will *probably* be fixed in the upcoming Windows updates.

# The Fix 

The way I fixed this error was to explicitly enable Unicode encoding-decoding in Windows (with the Windows Unicode library), and prevent multiple lines to be printed out in a fast manner by using carriage returns to update progres text etc. when possible. To run the code in this project simply install the following:

Using Pip:  
`pip install colorama`  
`pip intall win_unicode_console`

Using Conda:  
`conda install colorama`  
`conda install win_unicode_console`

Let me know if you guys have any problems with these scripts, I will be happy to help.
~Mat Gomes
