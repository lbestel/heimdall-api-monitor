from src.application.services.monitor_service import MonitorService
from src.domain.entities.monitor import Monitor
from src.infrastructure.http.httpclient import HttpClient

google = Monitor(1, 'Google', 'https://www.google.com', 'GET', 200, 5)
http_google = HttpClient(google)
test_google = MonitorService(google, http_google)
print(test_google.check())

http404 = Monitor(
    2, 'http404', 'https://postman-echo.com/status/404', 'GET', 404, 5
)
http_http404 = HttpClient(http404)
test_http404 = MonitorService(http404, http_http404)
print(test_http404.check())

http500 = Monitor(
    3, 'http500', 'https://postman-echo.com/status/500', 'GET', 500, 5
)
http_http500 = HttpClient(http500)
test_http500 = MonitorService(http500, http_http500)
print(test_http500.check())

delay = Monitor(4, 'delay', 'https://postman-echo.com/delay/10', 'GET', 200, 5)
http_delay = HttpClient(delay)
test_delay = MonitorService(delay, http_delay)
print(test_delay.check())

unexpected_status_201 = Monitor(
    5,
    'unexpected-201',
    'https://postman-echo.com/status/201',
    'GET',
    200,
    5,
)
http_unexpected_status_201 = HttpClient(unexpected_status_201)
test_unexpected_status_201 = MonitorService(
    unexpected_status_201, http_unexpected_status_201
)
print(test_unexpected_status_201.check())

unexpected_status_204 = Monitor(
    6,
    'unexpected-204',
    'https://postman-echo.com/status/204',
    'GET',
    200,
    5,
)
http_unexpected_status_204 = HttpClient(unexpected_status_204)
test_unexpected_status_204 = MonitorService(
    unexpected_status_204, http_unexpected_status_204
)
print(test_unexpected_status_204.check())

unexpected_status_404 = Monitor(
    7,
    'unexpected-404',
    'https://postman-echo.com/status/404',
    'GET',
    200,
    5,
)
http_unexpected_status_404 = HttpClient(unexpected_status_404)
test_unexpected_status_404 = MonitorService(
    unexpected_status_404, http_unexpected_status_404
)
print(test_unexpected_status_404.check())

unexpected_status_500 = Monitor(
    8,
    'unexpected-500',
    'https://postman-echo.com/status/500',
    'GET',
    200,
    5,
)
http_unexpected_status_500 = HttpClient(unexpected_status_500)
test_unexpected_status_500 = MonitorService(
    unexpected_status_500, http_unexpected_status_500
)
print(test_unexpected_status_500.check())
