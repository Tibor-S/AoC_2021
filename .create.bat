@echo off 
set day=%1
set inpath=C:\Users\Sebastian\Documents\Programming\AoC_2021\i%day%.in
set py1path=C:\Users\Sebastian\Documents\Programming\AoC_2021\p%day%_p1.py
set py2path=C:\Users\Sebastian\Documents\Programming\AoC_2021\p%day%_p2.py
set n=^&echo.

copy /y nul %inpath% > nul
echo. >%py1path%
echo. >>%py1path%
echo path = __file__ + "/../i%day%.in">>%py1path%
echo data = open(path).read()>>%py1path%
echo. >%py2path%
echo. >>%py2path%
echo path = __file__ + "/../i%day%.in">>%py2path%
echo data = open(path).read()>>%py2path%