import subprocess

while True:                                             # schleife
 rfid = raw_input("input: ")                            # user eingabe
 text = '/home/volumio/rfid//test.txt'                  # pfad zur datenbak

 with open(text) as text:                               # text als text oeffnen
  found = False                                         # var
  for line in text:
      if rfid in line:                                    
          found = True
          member = line.split('|')                      # auseinandernehmen der Zeile
          id = member[0]
          playlist = member[1].strip()
          print "key: %s" % id
          print "playlist: %s" % playlist
          if rfid == id:                                # wenn rfid in datenbank
            subprocess.call(['volumio', 'toggle'])
            print
            print
  else: 
      if rfid != id:
       print("key not found in database")
  text.close  
