# Evidence pojištěnců - Django

Tento projekt je full stack webová aplikace určená pro správu pojištěnců pomocí frameworku Django. Umožňuje snadno a efektivně přidávat, upravovat, vyhledávat a zobrazovat informace o pojištěncích.

## Funkce
- Přidání nového pojištěnce
- Zobrazení seznamu všech pojištěnců
- Vyhledávání pojištěnce podle jména a příjmení
- Editace a aktualizace informací o pojištěnci

## Technologie
Projekt je postaven na následujících technologiích:
- **Django** (Python webový framework)
- **SQL** (databáze)
- **HTML**, **CSS**, **JavaScript**

## Nasazení projektu
Projekt je nasazen online, můžete jej vyzkoušet na adrese: [https://liboroliva.pythonanywhere.com/](https://liboroliva.pythonanywhere.com/)

## Instalace

1. Klonujte tento repozitář:
   ```bash
   git clone https://github.com/liborgit/evidence-pojistencu-django.git
   ```


2. Přesuňte se do adresáře projektu:
    ```bash
    cd evidence-pojistencu-django/src
    ```

3. Nainstalujte závislosti pomocí souboru `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4. Vytvořte soubor .env a přidej následující proměnné prostředí:
    ```makefile
    DJANGO_SECRET_KEY=...
    DJANGO_DEBUG=False
    DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost,...
    ```

5. Proveďte migrace databáze:
    ```bash
    python manage.py migrate
    ```
    
6. Spusťte vývojový server:
    ```bash
    python manage.py runserver
    ```
