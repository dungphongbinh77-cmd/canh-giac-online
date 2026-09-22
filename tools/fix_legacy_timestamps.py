from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path

import gspread
from google.oauth2.service_account import Credentials

SHEETS = ["quiz_attempts", "message_checks"]
TIME_COL = "created_at"


def parse_old(value: str):
    value = (value or "").strip()
    if not value:
        return None
    # New rows already carry +07:00; never shift them again.
    if value.endswith("+07:00") or value.endswith("+0700"):
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            pass
    return None


def main():
    ap = argparse.ArgumentParser(description="Shift legacy UTC-like timestamps by +7 hours. Dry-run by default.")
    ap.add_argument("--json", required=True, help="Path to Google service-account JSON")
    ap.add_argument("--spreadsheet-id", required=True)
    ap.add_argument("--apply", action="store_true", help="Actually update Google Sheets")
    args = ap.parse_args()

    info = json.loads(Path(args.json).read_text(encoding="utf-8"))
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = Credentials.from_service_account_info(info, scopes=scopes)
    book = gspread.authorize(creds).open_by_key(args.spreadsheet_id)

    total = 0
    for title in SHEETS:
        try:
            ws = book.worksheet(title)
        except Exception:
            print(f"SKIP {title}: worksheet not found")
            continue
        values = ws.get_all_values()
        if not values:
            continue
        headers = values[0]
        if TIME_COL not in headers:
            print(f"SKIP {title}: missing {TIME_COL}")
            continue
        c = headers.index(TIME_COL) + 1
        updates = []
        for row_idx, row in enumerate(values[1:], start=2):
            raw = row[c-1] if len(row) >= c else ""
            dt = parse_old(raw)
            if dt is None:
                continue
            fixed = (dt + timedelta(hours=7)).strftime("%Y-%m-%d %H:%M:%S+07:00")
            updates.append({"range": gspread.utils.rowcol_to_a1(row_idx, c), "values": [[fixed]]})
            if len(updates) <= 5:
                print(f"{title} {row_idx}: {raw} -> {fixed}")
        total += len(updates)
        print(f"{title}: {len(updates)} legacy timestamps detected")
        if args.apply and updates:
            ws.batch_update(updates, value_input_option="RAW")
    print(f"Total legacy timestamps: {total}")
    if not args.apply:
        print("DRY RUN ONLY. Re-run with --apply after checking the preview.")

if __name__ == "__main__":
    main()
