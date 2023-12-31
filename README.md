# Installation
Instruktioner varierar beroende på om måldatorn har python.

**OBS!** Om eran admin inte tillåter er köra `.bat` filer eller `.exe` från nätet, se rubriken [Om IT-Människan är jobbig](#om-it-människan-är-jobbig).
## Med Python
1. Om du har python kan du ladda ner [darias_boxplots-2.1-py3-none-any.whl](https://github.com/marcell-ziegler/darias_boxplots/releases/download/v2.2/darias_boxplots-2.2-py3-none-any.whl), [python_run.bat](https://github.com/marcell-ziegler/darias_boxplots/releases/download/v2.2/python_run.bat) och frivilligt [python_uninstall.bat](https://github.com/marcell-ziegler/darias_boxplots/releases/download/v2.2/python_uninstall.bat) från den [senaste releasen](https://github.com/marcell-ziegler/darias_boxplots/releases/tag/v2.2) här i GitHub.
2. Gå till dina nedladdningar (finns som `%UserProfile%/Downloads` i windows) och dubbeklicka (kör) `python_run.bat`
    - Om du blir ombedd att godkänna paketinstallation, gör det.
3. Använd appen. Vid varje start kan du köra `python_run.bat` eller köra `python -m darias_boxplots` från terminalen. **OBS!** du måste köra `python_install.bat` minst en gång innan andra metoden funkar.
4. För att avinstallera kör `python_uninstall.bat` från godtycklig plats.

## Utan Python
1. Har måldatorn inte python kan du ladda ned [darias_boxplots.exe](https://github.com/marcell-ziegler/darias_boxplots/releases/download/v2.2/darias_boxplots.exe) från den [senaste releasen](https://github.com/marcell-ziegler/darias_boxplots/releases/tag/v2.2) här i GitHub.
2. Kör filen `darias_boxplots.exe`
3. Använd appen
4. Ingen avinstallation krävs, radera endast filen när du är klar.

# Om IT-Människan är jobbig
Om du inte kan köra mina förskrivna skript, genomför följande metod (desvärre krävs python för detta):
1. Ladda ner [darias_boxplots-2.1-py3-none-any.whl](https://github.com/marcell-ziegler/darias_boxplots/releases/download/v2.2/darias_boxplots-2.2-py3-none-any.whl) från den [senaste releasen](https://github.com/marcell-ziegler/darias_boxplots/releases/tag/v2.2) här i GitHub.
2. I terminalen kör följande från samma mapp som `.whl` filen ligger i:
```shell
pip install darias_boxplots-1.0-py3-none-any.whl
```
3. Därefter är följande kommando sättet att starta appen från varsomhelst i terminalen:
```shell
python -m darias_boxplots
```
4. För att avinstallera kör:
```shell
pip uninstall darias_boxplots
```

# Användning av appen
1. Starta appen
2. Tryck på `Get Plot Data`. I dialogen välj en fil som är antingen `.csv` eller `.txt`.
  - Filen måste vara delimiterad med `;`, `,` eller en newline-karaktär (`"\n"` i python). Exporter från Google Sheets är newline-delimiterade om tabellvärdena är vertikala och semikolon om de är horisontella.
3. Betrakta plotten. Om du inte vill ha linjer, klicka ur knappen `Grid`.
4. Om du är nöjd kan du trycka på `Save Plot` och sedan välja en plats och namnge den `.png` som kommer genereras.

## Format av excelark
Måste se ut **exakt** såhär. Siffror **måste** använda punkter (`.`) som decimatecken. Basically måste de vara läsliga python floats. Endast siffrorna (datan) får ändras. Annars kommer pandas att dö och jag har inte implementerat någon error handling.
![image](https://github.com/marcell-ziegler/darias_boxplots/assets/82723301/cbea055a-5e43-4f72-8d38-ca78f3058528)


# Exempel
## Exempel på appfönster
![image](https://github.com/marcell-ziegler/darias_boxplots/assets/82723301/4e6c15dc-54d4-4ff9-b86e-fc34cbf91ff5)
## Exemepel med video
**OBS! Dessa är nu gamla!**
### Pythonmetoden
[Vi#deo](https://1drv.ms/v/s!Ahf4h_NoO2C-h_wvu_qVneF_USwIKQ?e=w2xC9a)

### No-Pythonmetoden
[Video](https://1drv.ms/v/s!Ahf4h_NoO2C-h_wuM-IiM4yVMuFamQ?e=RczGsE)

### Jobbig IT-metoden
[Video](https://1drv.ms/v/s!Ahf4h_NoO2C-h_wtxgccl6VaiYa1dQ?e=I1Nst4)



