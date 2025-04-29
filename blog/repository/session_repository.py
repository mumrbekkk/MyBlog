

def get_session_value(request, key: str) -> str:
    return request.session.get(key)



