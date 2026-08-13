from datetime import datetime

import httpx

from src.domain.entities.checkresult import CheckResult
from src.domain.entities.monitor import Monitor
from src.domain.value_objects.http_status import HttpStatus
from src.infrastructure.http.httpclient import HttpClient


class MonitorService:
    def __init__(self, monitor: Monitor, http: HttpClient):
        self._http = http
        self._monitor = monitor

    def _build_result(self, response: httpx.Response) -> CheckResult:
        status = HttpStatus(response.status_code)

        if status.value == self._monitor.expected_status:
            check_status = 'UP'
            reason = '-'
        elif status.is_success() or status.is_redirection():
            check_status = 'DEGRADED'
            reason = status.name
        else:
            check_status = 'DOWN'
            reason = status.name

        return CheckResult(
            monitor_id=self._monitor.monitor_id,
            health_status=check_status,
            expected_status=self._monitor.expected_status,
            http_status=status.value,
            latency_ms=round(response.elapsed.total_seconds() * 1000, 2),
            reason=reason,
            checked_at=datetime.now(),
        )

    def _build_timeout_result(self) -> CheckResult:
        return CheckResult(
            monitor_id=self._monitor.monitor_id,
            health_status='DOWN',
            expected_status=self._monitor.expected_status,
            http_status=None,
            latency_ms=None,
            reason='READ_TIMEOUT',
            checked_at=datetime.now(),
        )

    def check(self):
        try:
            response = self._http.request()
            result = self._build_result(response)

            return result.to_dict()

        except httpx.ReadTimeout:
            return self._build_timeout_result().to_dict()
