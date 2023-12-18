import subprocess
valg = int(input("tast for hva du vill gjøre med bildet ditt: 1 filter, 2 svart hvitt filter, 3 bilderotasjon, 4 endre størrelse, 5 skriv tekst på bilde, 6 ramme inn bildet, 7 for å avslutte"))
if valg == 1:
    
 subprocess.run(["python", "oppgaveA.py"])
elif valg == 2:
 subprocess.run(["python", "oppgaveB.py"])
elif valg == 3:
 subprocess.run(["python", "oppgaveC.py"])
elif valg == 4:
 subprocess.run(["python", "oppgaveD.py"])
elif valg == 5:
 subprocess.run(["python", "oppgaveF.py"])
elif valg == 6:
 subprocess.run(["python", "oppgaveG.py"])
elif valg == 7: 
 SystemExit
    