def validate(data, template, path=""):
    for key in template:
        current_path = f"{path}.{key}" if path else key

        if key not in data:
            return False, f"mismatched keys: {current_path}"

        if isinstance(template[key], dict):
            if not isinstance(data[key], dict):
                return False, f"bad type: {current_path}"
            
            state, error = validate(data[key], template[key], current_path)
            if not state:
                return state, error
        
        elif not isinstance(data[key], template[key]):
            return False, f"bad type: {current_path}"

    for key in data:
        current_path = f"{path}.{key}" if path else key
        if key not in template:
            return False, f"mismatched keys: {current_path}"

    return True, ""
