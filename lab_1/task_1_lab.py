# kommentarer på svenska, koden på engelska.
# importera matplotlib för plotting av frekvens graf som används som exempel i lab 1
from pathlib import Path

HERE = Path(__file__).resolve().parent
path = HERE / "data" / "dna_raw.txt"

# with open(som vi fick lära oss i skolan) utf-8 för att hantera speciella tecken
with open(path, encoding="utf-8") as f:
    # läs filen, strip() tar bort extra whitespace till höger och vänster
    data = f.read().strip()

# dela upp i block
# dela upp string vid varje > (resultatet, en list)
blocks = data.split(">")[1:]  # [1:] = skippa första elementet

for block in blocks:
    # rensa rader, dela till rader, trimma whitespace <---> och släng tomrader
    raw_lines = block.splitlines()  # delar upp block i rader, splitta på nya rader (\n)
    lines = []  # <--- tom lista

    for line in raw_lines:  # för line i raw_lines
        sq = (
            line.strip()
        )  # tar bort whitespace i början/slutet på just denna rad (line.strip())
        if sq:  # behåll bara rader som INTE är tomma
            lines.append(sq)  # append till lines
    # VAKT Om lines är tom, får jag DIREKT ett error i form av IndexError denna rad skyddar mot error
    if not lines:
        # se kommentar ovan. Detta är enbart för att skydda mot error
        continue
    # id och sekvens
    sequence_id = lines[0]  # första raden = header/ID (inte en tom lista)
    sequence = (
        ""  # starta tom sträng och bygger upp sekvensen genom att lägga till varje rad
    )
    # för line i lines, hoppa över första raden (headern), resten är sekvensrader
    for line in lines[1:]:
        sequence += line  # sequence + tom rad
    sequence = (
        sequence.lower()
    )  # variabeln = variabel.lower(gör allt till små bokstäver)
    sequence = sequence.replace(" ", "")  # tar bort mellanslag inne i sekvens

    # räkna
    # dict med varje key och value som 0
    counts = {"a": 0, "t": 0, "c": 0, "g": 0}
    # others = 0 (others är N i dna_raw.txt, alla characters som inte är a,t,c,g räknas som others)
    others = 0

    for characters in sequence:  # för characters i sequence under id och sekvens
        if characters in counts:  # om characters finns i count dict'en
            counts[characters] += 1  # öka value hos den key'n med 1 i dict'en
        else:  # annars
            others += 1  # +1 i others så som n i dna_raw.txt

    print(sequence_id, counts, f"(Other values: {others})")
