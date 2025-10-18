# Labbar – Programmering (DE25)

Struktur för **lab_1** och **lab_2** i kursen Programmering (Data Engineer 2025).  
Kod körs som `.py` (ingen Jupyter). Virtuell miljö `.venv` används för renare paketversioner.

## Innehåll
- [Syfte](#syfte)
- [Miljö & versioner](#miljö--versioner)
- [Snabbstart](#snabbstart)
- [Struktur](#struktur)
- [Körning](#körning)
- [Exempeloutput](#exempeloutput)

## Syfte
- En mapp per lab, kod i `.py`.
- Tydlig data-/plots-struktur.
- Enkelt att klona och köra.
- Källor/anteckningar i `lab_X/notes.md`.

## Miljö & versioner
- **Python:** 3.12.x  
- **Paket:** se `requirements.txt` (genereras med `pip freeze`).  
- VS Code pekar på `.venv` via `.vscode/settings.json`.

## Snabbstart
**Windows (PowerShell):**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Struktur
- `lab_1/` och `lab_2/` ligger i separata mappar i repot.
- Varje labb-mapp innehåller:
  - `data/` med relevanta filer (t.ex. `dna_raw.txt`, PDF med uppgiftstext).
  - Python-skript (`.py`) som löser uppgifterna.
  - `notes.md` med källor och vad jag fått hjälp med (radintervall + länk).
- Kod körs som `.py` (ingen Jupyter).

## Körning
# Task 1 (script + plottar)
python lab_1/task_1_lab.py

# Task 2 (funktion + plottar)
python lab_1/task_2_lab.py

## Exempeloutput (task_2, dna_raw_complicated.txt)
seq1 {'a': 17, 't': 7, 'c': 8, 'g': 2} (Others: 0)
seq2 {'a': 3,  't': 7, 'c': 4, 'g':10} (Others: 0)
seq3 {'a':36, 't':19, 'c':34, 'g':21} (Others: 2)
seq4 {'a':17, 't':12, 'c':15, 'g':20} (Others: 0)

