def prefill(n,v=None):
    try:
        return [v for i in range(int(n))] 
    except (TypeError, ValueError):
        return f"{v} is invalid"
