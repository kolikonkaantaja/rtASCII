rtASCII(random terminal ASCII)
Written in python and shell
			       \ ----o-o-o-o \		Useless
o----			        \ ----o	    o \		Useless
o----			         \ ----o     o \	Useless		      |\
o-o-o-o-o-o-o-o-o-o-o-o-o----\	  \ ----o     o \	Useless		      | \
o----  			 o----\	   \ ----o     o \	Useless	\== == == =====  \ SOFTW
\ o----		   o-o-o-o-o----\   \ ----o     o \	Useless  \== == == ====  / SOFTW
 \ o---           o----	             \ ----o     o \	Useless		      | /
  \ o----	 o----	----o-o-o-o-o-o-o-o-      o \	Useless		      |/
   \ o----	o----	----o                      o \	Useless
AK  \ o-o-o-o-o-o----	----o-o-o-o-o-o-o-o-o-o-o-o-o \	Useless

To start it up after opening terminal:
	1. Copy "rtasciis.sh" to ~/
	2. Change directory to the location where you clone it.
	   Example:
	   	rtasciis.sh
	##Change this directory to where is your rtASCII directory
	cd "your directory goes here"/rtASCII
	python rtascii.py
	3. In your .bashrc(any other shell should work) write this line "sh rtasciis.sh" to the bottom of your .bashrc
	4. If it doesnt work, troubleshoot it;)
Adding own ASCII art:
	Template is "1template.sh"
	1. Write your ASCII art between "cat << "EOS"" and "EOS" in copy of 1template.sh
	2. Colors. Colors are in ANSI format so you need to check refrence for them.
