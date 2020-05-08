from datetime import datetime


print_history = {}

def sprint(message: str) -> None:
    print_history.update({
        "last_print": message,
        "history": print_history.get("history", []) + [{
            "message": message,
            "at": datetime.utcnow()
        }]
    })

def get_last_sprint() -> str:
    return print_history.get("last_print")
