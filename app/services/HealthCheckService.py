class HealthCheckService:
    def __init__(self):
        pass

    def health_check(self):
        return {"message": "health check"}

health_service = HealthCheckService()