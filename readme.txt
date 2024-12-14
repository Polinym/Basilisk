Hi! This is Basilisk, an editor/compiler for Fire Emblem 1.
It does not work with Fire Emblem 2, or any other game.
There's simply too many things for FE1-hacking to cover in a
single readme file, so I'll just explain what this editor is
capable of and give you the basics.

Before you can begin hacking, you need to define a base ROM
to use for all your projects (the only compatible ROM is the
one created from the patch included with this editor, which should
be applied to an unedited Japanese ROM ). Once you have created
the modded ROM, you do have the option of using any derivatives of
that modded ROM as your base ROM, though I wouldn't reccomend it.

Press the "Load Base ROM" button to select the modded FE1 ROM.

Press "Set Project Directory" to define the computer directory
you'd like to use for all projects. Individual Project folders
will be created within this directory.

The "Project Name" box on the right side can be used to
set or change the project you are currently working with.
The project named here will be the one used for the rest
of the options.

With a project name set, click "Generate Project from Template"
to create a subfolder in your Project Directory that will
contain all the files for your Project You only have to generate
a project from a template once for every new Project.

* * * IMPORTANT * * * 

Press "Save Config" once you have changed all the previous settings
to save them. This way, when you close and re-open Basilisk later,
it will remember where your Base ROM, Project Directory, and
current Project are.

* * * * * * * * * * *

Once you have a Project created, you can click "Open Project"
to begin working on it. The directory will contain folders and
text files for all the data that Basilisk is capable of editing.
Simply change the text files using the editor of your choice,
and when you're all done making changes, you can come back to
Basilisk.

The "Backup ROM" button can be pressed to quickly create a
numbered backup of the ROM currently in your Project folder.

Be sure to do this BEFORE you click "Compile", as that button
overwrites the ROM in your Project folder every time.

- - - - - - - - UNIT MAKER - - - - - - - -

The "Open Unit Maker" is a GUI that I included to make the
task of creating/changing player units easier. You must set your
current Project before using this, as it loads the names of
chars/classes/items from your Project folder. 

In Basilisk, Fire Emblem units are treated as Bytestrings, which
is all the hexadecimal values that make up a unit's data written
in a single line.
Prince Mars, the first playable unit, is stored as:

011501121200300503050707070705000619000500000000000000

You can paste this Bytestring, or any valid unit Bytestring,
into the Unit Maker to load its settings into the GUI. 

The "Generate" button takes all of the settings of the GUI
and creates a Bytestring in the bar at the top. You can then
paste this Bytestring anywhere a unit Bytestring is used

- - - - - - - - - - - - - - - - - - - - -

When you're done making changes, you can press the
"Compile Project" button to compile the data in your Project.
Your Project folder contains its own ROM, which is the one
Basilisk will write the data to. 

When editing the text files, you must try to preseve as much of
the original formatting as possible. If some text is in the
wrong place, Basilisk may throw an error. All errors will pop
up in the output box of the GUI, in the top right corner.

Errors in text files will likely show you in which file the issue
occured, so there you go.

If all of your data has been loaded correctly, then issues may
occur in the process of writing the data to ROM. 



* * * IMPORTANT * * * 

   The Eternal Struggle of Free Space

As a NES ROM, FE1 has very limited space. Admittedly, it has
considerably more free space than other NES ROMs, but it is
still quite small. 

I've done the best I can with adding three sets of dictionary
compression into the game (hence, the modded ROM), plus compression
for chapter maps, but you're still inevitably going to face the
issue of limited space at some point.

When Basilisk runs out of room for a given chunk of data, it will stop
inserting the rest of that chunk, but try and continue to insert other
chunks. The output box will tell you the number of freespace issues that
occur, if any, at the end of the compile messsage.

After every part of the game that Basilisk compiles, it will print the amount of
bytes of freespace that remain for that chunk of data. 

If two strings in the same ROM bank (section of the game) are the same, Basilisk
will only compile one instance of the string and have all references point to
that ones string. This greatly helps cut down on the amount of space that your
data takes up, and the displayed freespace amount accounts for this.

   How to Manage Your Space Issues

The biggest place where space issues will occur is with names and text.

The default project configuration has very little wiggle-room
 (like, a dozen or so bytes) in regards to space (which I hope to fix someday), 
so I'd not advise you mess with the dictionary stuff much unless you're 
planning to change a whole bunch of text.

Regardless, you have three dictionaries that you can use to compress your text.

Dictionary compression is where when you have multiple instances of a word
in a game, you store that word once in a "dictionary" and store that word's
index number in every place where that word would appear.

For example, the default first dictionary's word is "Archbishop", which takes
up 10 bytes by itself. Anytime I want to use the word "Archbishop" in my modded
FE1 ROM, I store the word as 2 bytes (8F, 00) instead. When the game finds
8F, it goes "Hey, that's a dictionary entry!" and reads the word it finds at
the 00th position in the dictionary, "Archbishop".

The dictionaries are located in <Project>/text/dictionary

"dictionary.txt" and "dictionary2.txt" are used for all of the game's
cutscene text, not menus. If you're planning on having a huge new script for
the game or doing major edits, these are the two you'll use to set up a new
dictionary for your edited script.

"dictionary_names" is a relatively new dictionary I added to work with all
of the game's menus. This includes basically everything in the text/names
folder, as well as the item_names. As this one is very new, it's entirely
possible that there's some edge case out there in the game that doesn't
work with my dictionary, so let me know if you see an error.

I won't get deep into optimizing your dictionaries here, but in a sentence,

Your longest / most common character sequences should be the entries
in your dictionary.

* * * * * * * * * * *

DON'T FORGET!

Even if the compiler throws a freespace error, it WILL continue
to write the OTHER data outside the bank where the error occured,
so your ROM will still be modified!



When you run into errors, you can always reach out to me, Polinym,
on FEUniverse ( https://feuniverse.us/ )
or ROMHacking.net ( https://www.romhacking.net/forum/ )


Oh, and before you go...

///////////////////////////////////////////////////////////////////////////

If you like Basilisk and want to support its development, you can
check out my very own indie game on Steam, Octo Vinctum!

https://store.steampowered.com/app/1899110/Octo_Vinctum_Revenge_of_the_Czar/

Octo Vinctum: Revenge of the Czar is an epic JRPG where you battle enemies
with the power of kind words and amazing Talents! This role-playing
adventure is filled with humorous references to games both famous and obscure,
especially Fire Emblem! You play as a young girl named Sabrina and her friends
as they take down an evil entertainment empire named Czar Entertainment, attempt
to recover lost magical relics, and face cosmic horrors you have to see to believe!


You can also check out my other FREE games on Itch.io! 

https://polinym.itch.io/

///////////////////////////////////////////////////////////////////////////










///////////////////////////////////////////////////////////////////////////





