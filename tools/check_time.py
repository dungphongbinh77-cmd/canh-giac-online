from datetime import datetime, timezone
from zoneinfo import ZoneInfo

VN = ZoneInfo("Asia/Ho_Chi_Minh")
print("UTC:      ", datetime.now(timezone.utc).isoformat(sep=" ", timespec="seconds"))
print("Viet Nam: ", datetime.now(VN).isoformat(sep=" ", timespec="seconds"))
print("Expected offset: +07:00")
