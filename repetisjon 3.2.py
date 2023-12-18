import statistics
def gjennomsnitt():
    liste = float(input("skriv inn tall"))
    result = statistics.mean(liste)
    print(result)
gjennomsnitt()