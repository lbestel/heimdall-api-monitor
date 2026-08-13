class Monitor:
    def __init__(  # noqa: PLR0913, PLR0917
        self,
        monitor_id: int,
        name: str,
        url: str,
        method: str,
        expected_status: int,
        timeout: int,
    ):
        self._monitor_id = monitor_id
        self._name = name
        self._url = url
        self._method = method
        self._expected_status = expected_status
        self._timeout = timeout

    @property
    def monitor_id(self):
        return self._monitor_id

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    @property
    def method(self):
        return self._method

    @property
    def expected_status(self):
        return self._expected_status

    @property
    def timeout(self):
        return self._timeout
