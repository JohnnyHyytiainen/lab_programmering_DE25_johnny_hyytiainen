# kommentarer på svenska, koden på engelska.

# Vad: Läs FASTA-liknande DNA, räkna A/T/C/G per sekvens och plotta
# Varför: Uppfyller Lab 1 Task 1 (case-insensitiv, dict + graf). Fungerar även på "complicated"
# Hur: Läs -> split på '>' -> rensa -> id = första raden, sequence = join(rest).lower() -> Counter + plot


# Steg 1 - Importer
# Varför: Jag vill räkna bokstäver enkelt (Counter) och kunna plotta (matplotlib)
import matplotlib.pyplot as plt
from collections import Counter

# för robust path hantering (fil i \data mapp, inte i root mappen)
from pathlib import Path

# Steg 2 - Filväg
# Varför: Jag säger var filen finns då .txt filerna finns i annan mapp \data och ej i root
HERE = Path(__file__).resolve().parent
# av-kommentera/kommentera path = HERE / "data" / "dna_raw.txt" om du vill köra dna_raw.txt
path = HERE / "data" / "dna_raw.txt"
# av-kommentera/kommentera path = HERE / "data" / "dna_raw_complicated.txt" om du vill köra dna_raw_complicated.txt
# path = HERE / "data" / "dna_raw_complicated.txt"

# Steg 2.5 - Signatur färg
BAR_COLOR = "purple"


# Steg 3 - Läs rådata
# Varför: Jag läser in hela filen till EN sträng och städar bort extra whitespace i början/slutet
# with open(som vi fick lära oss i skolan) utf-8 för att hantera speciella tecken
with open(path, encoding="utf-8") as f:
    data = f.read().strip()

# Steg 4 - Dela i poster med >
# Varför: med FASTA parsing börjar varje post med >
# Split (">") delar på varje >. Första elementet är tomt, därför [1:]
for block in data.split(">")[1:]:

    # Steg 5 - Rensa rader i blocket
    # Varför: Jag vill ha en ren lista av rader utan tomma rader/extra whitespace
    lines = [line.strip() for line in block.splitlines() if line.strip()]
    # splitlines() delar på radbrytningar(\n) och strip() tar bort whitespace till höger och vänster
    # if line.strip slänger tomma rader (sant om inte tom rad efter strip)

    # VAKT - om lines är tom, får jag direkt ett error(IndexError) denna rad skyddar mot error
    if not lines:
        # se kommentar ovan. Detta är enbart för att skydda mot error
        continue

    # Steg 6 - Plocka ID och bygg sekvens
    # Varför: Första raden är mitt ID. Resten av raderna = sekvensen, ihopsatta och till gemener
    sequence_id = lines[0]
    # Join sätter/slår ihop rader utan \n. .lower() gör allt till små bokstäver
    sequence = "".join(lines[1:]).lower()
    # Tar bort ALLA whitespace(space, tab etc) immun mot "skräp" i filer och behöver ej oroa mig.
    sequence = "".join(sequence.split())

    # Steg 7 - Räkna med Counter
    # Varför: Snabbt sätt att få frekvens per bokstav (bättre än manuell loop för större data)
    count = Counter(character for character in sequence if character in "atcg")
    # Counter funktionen räknar ENDAST a,t,c,g. Ingenting annat (filtrerar bort others via if)

    # Steg 8 - Säkerställ nycklar + räkna övriga
    # Varför: Jag vill ALLTID ha fyra nycklar(keys) a,t,c,g även om någon är 0
    # Jag vill även veta hur många tecken som är others.
    counts = {b: count.get(b, 0) for b in "atcg"}
    # Snabbt sätt, total längd MINUS summan av counts(ingen extra loop)
    # Snabbare än sum(1 for....) då jag redan använder räknande med counts
    others = len(sequence) - sum(counts.values())

    # Steg 9 - Slutgiltig utskrift
    print(sequence_id, counts, f"(Others: {others})")

    # GLÖM EJ BORT INDENTERING FÖR PLOT! Glömmer du bort den så visas ENDAST seq 4 då den är utanför loopen!
    letters = ["a", "t", "c", "g"]
    values = [counts[b] for b in letters]
    plt.figure()
    plt.bar(range(len(letters)), values, color=BAR_COLOR)
    plt.xticks(range(len(letters)), letters)
    plt.xlabel("DNA letters")
    plt.ylabel("Frequency")
    # Titel på plott om vilken sekvens som visas + totala längden på sekvensen
    plt.title(f"{sequence_id} (n={len(sequence)})")
    plt.show()
