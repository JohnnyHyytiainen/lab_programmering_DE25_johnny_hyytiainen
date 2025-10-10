# Kommentarer på svenska, koden på engelska.
# Vad: Läsa FASTA-liknande DNA, räkna a/t/c/g per post och plotta frekvenser.
# Varför: Samma struktur och semantik som task_1_lab(Långform -> kortform) men som en funktion som klarar av fler rader/sekvenser
# Hur: Läs -> split på ">" -> rensa rader -> sequence_id=lines[0], sequence="".join(lines[1:]).lower()
# Tar bort all whitespace i sekvensen, räknar atcg manuellt, allt annat = others


# Steg 1 - Importer
# för robust path hantering (fil i \data mapp, inte i root mappen)
from pathlib import Path
import matplotlib.pyplot as plt

# Steg 2 - Filväg
# Varför: Jag säger var filen finns då .txt filerna finns i annan mapp \data och ej i root
HERE = Path(__file__).resolve().parent
# av-kommentera/kommentera path = HERE / "data" / "dna_raw.txt" om du vill köra dna_raw.txt
# path = HERE / "data" / "dna_raw.txt"
# av-kommentera/kommentera path = HERE / "data" / "dna_raw_complicated.txt" om du vill köra dna_raw_complicated.txt
path = HERE / "data" / "dna_raw_complicated.txt"

# Steg 2.5 - Signaturfärg + bokstavsordning för plott
BAR_COLOR = "purple"
LETTERS = ["a", "t", "c", "g"]


# Steg 3 - Skapa funktionen med beskrivande docstrings
def parse_and_count(path):
    """
    Baserad på FASTA-format för DNA-data.
    Läser en FASTA-lik fil och returnerar en lista av tuples:
    [(sequence_id, {'a': int, 't': int, 'c': int, 'g': int}, others_int), ...]
    Keys är alltid 'a','t','c','g'.
    """
    # Steg 4 - Läs in filen. Jag får en enda str med allt innehåll, utan extra blankrader i kanterna
    with open(path, encoding="utf-8") as f:
        data = f.read().strip()

    # FASTA-poster börjar med >. Första elementet före första > är tomt, därför -> [1:]
    parts = data.split(">")[1:]
    # Samla resultat här, så som sequence_id, counts_dict, others
    results = []

    # Steg 5 - Loopa över varje post
    for block in parts:
        # dela i rader med splitlines()
        raw_lines = block.splitlines()
        # trimma och släng tomma rader
        lines = [line.strip() for line in raw_lines if line.strip()]

        # VAKT - om inga rader kvar -> hoppa över blocket
        if not lines:
            continue

        # Steg 6 - ID/header. Bygga sekvens (join flera rader till en string)
        sequence_id = lines[0]  # header/ID
        # normalisera till gemener(små bokstäver)
        sequence = "".join(lines[1:]).lower()
        # rensa ALLA whitespace, .split() tar bort whitespace mellan tecken
        sequence = "".join(sequence.split())

        # Steg 7 - räkna baser och others.
        # dict för a,t,c,g med value 0 för alla
        counts = {"a": 0, "t": 0, "c": 0, "g": 0}
        others = 0  # allt som ej är a,t,c,g räknas som others
        for character in sequence:
            if character in counts:
                counts[character] += 1
            else:
                others += 1

        # Steg 8. Lägg till(append) results
        results.append((sequence_id, counts, others))
    # Steg 9. Returnera results, se steg 3-8
    return results


# Steg 10 - Körning + plott
if __name__ == "__main__":
    results = parse_and_count(path)

    for sequence_id, counts, others in results:
        total = sum(counts.values()) + others
        print(sequence_id, counts, f"(Others: {others})")

        # GLÖM EJ BORT, ha plott UTANFÖR funktionen!
        values = [counts[b] for b in LETTERS]
        plt.figure()
        plt.bar(range(len(LETTERS)), values, color=BAR_COLOR)
        plt.xticks(range(len(LETTERS)), LETTERS)
        plt.xlabel("DNA letters")
        plt.ylabel("Frequency")
        # Titel på plott om vilken sekvens som visas + totala längden på sekvensen
        plt.title(f"{sequence_id} (n={total})")
        plt.show()
