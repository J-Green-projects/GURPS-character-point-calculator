# GURPS-character-point-calculator
A character point calculator for .rtf, .txt, and .docx "free form" character sheets that is run in the command line.

To use: simply run the script, enter the filepath, and then the character that comes before the point value of a given trait. I have tried to keep this flexible, but a consistent and special formatting is necessary. The character must be consistent, and it cannot be used for other things with numeric values.<br><br>
It will work with formatting like:<br>
360 deg. Vision [easy to hit -20%] (25 pts)<br>
Absent-Mindedness (-15 pts)<br>
Accounting - IQ/Hard, IQ+0 (4 pts) [skill level 10]<br>
Backpack, Frame [$100, 10 lbs]<br><br>
The point delimiter is "(", and the script will only take into account 4 characters after that, disregarding all non-numeric characters. You can use any delimiter you like, but point costs must have a unique delimiter.
