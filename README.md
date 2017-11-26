## rfidradio :notes:

Ein Musik-Player der gesteuert wird über eine WebUI und RFID-Tags.
Das System basiert bisher auf [Volumio](https://volumio.org) und ein paar Python-Skripten, die ich gefunden und minimal angepasst habe um die externen Schalter (ON/OFF, Volume/Toggle) abzufragen und zu bedienen.

### ToDo Software:

Ein Script, dass:
- auf eine Eingabe des RFID-Readers wartet (10 stellige Nummer + ENTER)
- die Nummer in einer Datenbank (evtl. txt-Datei) abgleicht und einer MP3 zuordnet
- die MP3 im Player abspielt
- Feedback über LED am ON/OFF-Taster

Es sollte möglichst einfach sein, neue Inhalte hinzuzufügen. Auf Volumio kann man per smb zugreifen. Dann kann man einfach neue Titel hinzufügen und einen Eintrag in der txt-Datei machen.

### Probleme
- RFID-Reader wird als HID erkannt

### Beispiele
- https://github.com/mwiedemeyer/RaspiMusicBox
- https://github.com/Terminal-Geek/Audioplayer
- https://www.musicpd.org

### Hardware
![img_5210](https://user-images.githubusercontent.com/25091747/33244486-447f4a74-d2f8-11e7-8385-c3340e1acabd.jpg)

- https://www.amazon.de/gp/product/B00HSDOTTU/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1 -> RFID
- https://www.amazon.de/gp/product/B00HSWXR9Y/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1 -> Rotary Encoder
- https://www.amazon.de/gp/product/B01FM6TOH6/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1 -> Power Bank
- https://cdn-learn.adafruit.com/downloads/pdf/adafruit-speaker-bonnet-for-raspberry-pi.pdf -> DAC und Boxen
- https://www.ebay.de/itm/232503354835 -> Taster
