import logging
from typing import Any, Dict, Optional

def validate_payload(data: Any) -> Optional[Dict[str, Any]]:
    if not isinstance(data, dict):
        logging.error("invalid payload format: expected dict")
        return None
    if "id" not in data or "payload" not in data:
        logging.error("missing required fields in payload")
        return None
    return data

def process_stream(data_stream: Any) -> None:
    for item in data_stream:
        validated = validate_payload(item)
        if validated is None:
            continue
        try:
            execute_task(validated)
        except Exception as e:
            logging.exception(f"task execution failure: {e}")

def execute_task(data: Dict[str, Any]) -> None:
    logging.info(f"processing task {data.get('id')}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sample_stream = [{"id": 1, "payload": "data1"}, "invalid", {"id": 2}]
    process_stream(sample_stream)