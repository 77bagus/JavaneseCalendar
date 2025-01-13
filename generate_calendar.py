import json
from datetime import datetime, timedelta

# Data Pasaran dan Wuku dalam kalender Jawa
PASARAN = ["Legi", "Pahing", "Pon", "Wage", "Kliwon"]
JAWA_MONTHS = ["Sura", "Sapar", "Mulud", "Bakda Mulud", "Jumadil Awal", "Jumadil Akhir",
               "Rejeb", "Ruwah", "Pasa", "Sawal", "Dulkaidah", "Besar"]

def generate_javanese_calendar(year_start, year_end):
    start_date = datetime(year_start, 1, 1)
    end_date = datetime(year_end, 12, 31)
    jawa_calendar = []
    jawa_day = 0  # Counter for determining pasaran

    # Iterate through the dates
    current_date = start_date
    while current_date <= end_date:
        # Determine Javanese month and pasaran
        month_index = (current_date.month - 1) % 12
        pasaran_index = jawa_day % 5
        jawa_calendar.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "pasaran": PASARAN[pasaran_index],
            "bulan_jawa": JAWA_MONTHS[month_index]
        })
        jawa_day += 1
        current_date += timedelta(days=1)
    
    return jawa_calendar

if __name__ == "__main__":
    # Generate data for a specific range
    year_start = 2025
    year_end = 2025
    calendar_data = generate_javanese_calendar(year_start, year_end)
    
    # Save to a JSON file
    with open("javanese_calendar.json", "w", encoding="utf-8") as file:
        json.dump(calendar_data, file, ensure_ascii=False, indent=4)
    print("Javanese calendar generated successfully.")
