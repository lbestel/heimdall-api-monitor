from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass
class CheckResult:
    monitor_id: int
    health_status: str
    expected_status: int
    http_status: int | None
    latency_ms: float | None
    reason: str
    checked_at: datetime

    def to_dict(self):
        return asdict(self)
