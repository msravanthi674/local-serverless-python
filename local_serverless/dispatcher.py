import importlib.util

def dispatch_event(function_name, data):
    path = f"functions/{function_name}.py"
    spec = importlib.util.spec_from_file_location(function_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.run(data)
