# Texas is a Macro-Sized State Pt. 2
* **Event:** flagCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**


## Steps
#### Step 1
Again, we have a problem involving macros, but this one is a little more about reverse engineering. If we open the spreadsheet document, we'll notice there are 2 sheets: Texas Flag and Secret Flag. Opening up Secret Flag, you'll see a cell advising you not to run the macro. Additionally, you may notice a piece of the flag in cell A25 (but clearly not all of it). Where's the rest of the flag? You'll need to analyze the macro to find out.

#### Step 2
Open up the editor for macros and take a look at what the subroutine `disperse_secret` is doing. While you may not be familiar with BASIC, one thing that should jump out at you is the hardcoded cell positions: $A$25, $Z$500, and $M$200. You may already know A25 corresponds to one part of the flag, so it's a good guess to think these other cells are also related. 

#### Step 3
Go to each cell and piece together the dispersed components of the flag (the ordering should be pretty easy to figure out).


