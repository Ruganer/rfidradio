## rfidradio

Ein Musik-Player der gesteuert wird über eine WebUI oder RFID-Tags.
Das System basiert bisher auf Volumio und ein paar Python-Skripten, die ich gefunden und minimal angepasst habe um die externen Schalter (ON/OFF, Volume/Toggle) abzufragen und zu bedienen.

### ToDo Software:
EinScript, dass:
- auf eine Eingabe des RFID-Readers wartet (10 stellige Nummer + ENTER)
- die Nummer in einer Datenbank (evtl. txt-Datei) abgleicht und einer MP3 zuordnet
- die MP3 im Player abspielt

### Probleme
- RFID-Reader wird als HID erkannt

### Beispiele
- https://github.com/mwiedemeyer/RaspiMusicBox
- https://github.com/Terminal-Geek/Audioplayer
- https://www.musicpd.org

### Hardware
![img_5210](https://user-images.githubusercontent.com/25091747/33244486-447f4a74-d2f8-11e7-8385-c3340e1acabd.jpg)
