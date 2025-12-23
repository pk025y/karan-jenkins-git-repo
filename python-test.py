from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones

def show_all_timezones():
    print(f"{'TIMEZONE':<35} CURRENT TIME")
    print("-" * 60)

    for tz in sorted(available_timezones()):
        try:
            current_time = datetime.now(ZoneInfo(tz))
            print(f"{tz:<35} {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception:
            pass

if __name__ == "__main__":
    show_all_timezones()
