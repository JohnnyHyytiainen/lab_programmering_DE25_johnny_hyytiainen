# Labbar – Programmering (DE25)

Struktur för **lab_1** och **lab_2** i kursen Programmering (Data Engineer 2025).  
Kod körs som `.py` (ingen Jupyter). Virtuell miljö `.venv` används för renare paketversioner.

## Innehåll
- [Syfte](#syfte)
- [Miljö & versioner](#miljö--versioner)
- [Snabbstart](#snabbstart)
- [Struktur](#struktur)

## Syfte
- En mapp per lab, kod i `.py`.
- Tydlig data-/plots-struktur.
- Enkelt att klona och köra.
- Källor/anteckningar i `lab_X/notes.md`.

## Miljö & versioner
- **Python:** 3.12.x (ange exakt om du vill)  
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
## Struktur
- `lab_1/` och `lab_2/` ligger i separata mappar i repot.
- Varje labb-mapp innehåller:
  - `data/` med relevanta filer (t.ex. `dna_raw.txt`, PDF med uppgiftstext).
  - Python-skript (`.py`) som löser uppgifterna.
  - `notes.md` med källor och vad jag fått hjälp med (radintervall + länk).
- Kod körs som `.py` (ingen Jupyter).
