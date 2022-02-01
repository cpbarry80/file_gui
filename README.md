
generates a gui, where a listbox is populated with folders found C:\Models. user selects a folder and a compare between the two folders below is made. 
C:\Models\{folder_selected}\OLD MODEL\WORK'
C:\Models\{folder_selected}\CURRENT MODEL\WORK'

fuzzy_match library is used to produce the match_score. 
    Find the similarity between two strings using ngrams.
    Returns float score value, 0.0 being completely different strings and 1.0 being equal strings.


# setup 
pip install -r requirements.txt
run main.py to generate the gui

to create the 1 file .exe, from the folder main.py is in run 
    pyinstaller --onefile main.py
PyInstaller creates a distribution directory, DIST containing the main executable and the dynamic libraries bundled in an executable file