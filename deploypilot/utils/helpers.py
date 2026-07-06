def env_to_bool(key: str) -> bool:
    return key.lower() in ["1", "true", "yes", "on"]