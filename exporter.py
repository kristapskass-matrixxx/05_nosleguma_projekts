# exporter.py
import json
import os

def export_data(data, filename="exported_data.json"):
    """
    Saglabā datus JSON failā pašreizējā direktorijā.
    """
    filepath = os.path.join(os.getcwd(), filename)
    
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Dati saglabāti failā: {filepath}")
    except Exception as e:
        print(f"Kļūda datu saglabāšanā: {e}")