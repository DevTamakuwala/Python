import re

def is_rgm_identifier(identifier):
    pattern = r'^[a-k][0369][a-zA-Z0-9#]*$'
    if re.fullmatch(pattern, identifier):
        return "Valid RGM Identifier"
    else:
        return "Invalid RGM Identifier"

# Example usage:
print(is_rgm_identifier("a3hello"))
print(is_rgm_identifier("k0world#"))
print(is_rgm_identifier("z3notvalid"))
print(is_rgm_identifier("b5"))
