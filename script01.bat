@echo off
echo abc

rem "Dies ist ein Kommentar!"

if not exist Ordner3 (md "Ordner3") else (echo "Ordner3 existiert bereits.")

if not exist Ordner4 (md "Ordner4") else (echo "Ordner4 existiert bereits.")

echo "Datei3" > Ordner3\Datei1.txt
echo "Datei4" > Ordner4\Datei2.txt

copy "Ordner3\Datei1.txt" "Ordner4"
copy "Ordner4\Datei2.txt" "Ordner3"

pause