class LogRecord:
    def __init__(self, time, service, actor, country, ip_source, ip, device, type, action, crud, targets, tags, grouped_events, hit_count, classification):
        self.time = time
        self.service = service
        self.actor = actor
        self.country = country
        self.ip_source = ip_source
        self.ip = ip
        self.device = device
        self.type = type
        self.action = action
        self.crud = crud
        self.targets = targets
        self.tags = tags
        self.grouped_events = grouped_events
        self.hit_count = hit_count
        self.classification = classification

    def update(self, **kwargs):
        new_data = {**vars(self), **kwargs}
        return LogRecord(**new_data)

    def __str__(self):
        return ', '.join([f"{key}: {value}" for key, value in vars(self).items()])


# Example usage
record1 = LogRecord(
    time="2023-08-09 10:15:00",
    service="Login",
    actor="User123",
    country="USA",
    ip_source="192.168.1.10",
    ip="203.0.113.50",
    device="Laptop",
    type="Authentication",
    action="Login",
    crud="R",
    targets="user123@example.com",
    tags="security, login",
    grouped_events="Login Attempts",
    hit_count=1,
    classification="Success"
)

print(record1)

record2 = record1.update(action="Logout", hit_count=2)
print(record2)
