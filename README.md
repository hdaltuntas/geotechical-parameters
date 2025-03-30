# geotechical-parameters

This python code determines geotechnical parameters with the help of empirical formulas

30.03.2025

1. Added `sptn60` parameter to `undrained_shear_strength()` function
2. Fixed the return value in `cv()` function to return `cv` instead of `cs`
3. Fixed the typo in `liguid_limit` to `liquid_limit`
4. Added `cu` and `cpt` inputs for the deformation modulus calculation
5. Changed all `if` statements to `elif` for better flow control
6. Fixed some parentheses issues in the mathematical expressions
7. A `GeotechnicalParameters` class that organizes all calculation methods as static methods
8. Proper docstrings for each method explaining what it calculates
9. A main() function that handles user input and displays results
10. Better organized output formatting
11. Consistent naming conventions
12. Proper error handling for invalid inputs