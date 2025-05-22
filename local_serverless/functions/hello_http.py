def run(request):
    name = request.get("name", "world")
    return {"message": f"Hello, {name}!"}
