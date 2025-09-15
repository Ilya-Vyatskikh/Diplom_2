class IngredientData:
    """Набор ингридиентов с существующим хэщем"""
    valid_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}

    """Набор без ингридиентов"""
    empty_data = {"ingredients": []}

    """Набор ингридиентов с несуществующим хэщем"""
    invalid_data = {"ingredients": ["invalid-hash-123"]}