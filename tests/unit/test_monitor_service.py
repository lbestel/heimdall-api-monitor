from http import HTTPStatus
from unittest.mock import Mock

from src.application.services.monitor_service import MonitorService
from src.domain.entities.monitor import Monitor


def test_monitor_is_up():
    monitor = Monitor(
        monitor_id=1,
        name='Google',
        url='https://google.com',
        method='GET',
        expected_status=200,
        timeout=5,
    )

    http = Mock()

    response = Mock()
    response.status_code = HTTPStatus.OK
    response.elapsed.total_seconds.return_value = 0.1

    http.request.return_value = response

    service = MonitorService(monitor, http)

    result = service.check()

    assert result['health_status'] == 'UP'
    assert result['http_status'] == HTTPStatus.OK
