from fastapi import FastAPI, Query
from app.model import multiply_matrices
from app.metrics import record_request

app = FastAPI(title="Matrix Multiplication API")

@app.get("/multiply")
def multiply(a11: int, a12: int, a21: int, a22: int,
             b11: int, b12: int, b21: int, b22: int):
    """
    Multiply two 2x2 matrices.
    Example:
    /multiply?a11=1&a12=2&a21=3&a22=4&b11=5&b12=6&b21=7&b22=8
    """
    A = [[a11, a12], [a21, a22]]
    B = [[b11, b12], [b21, b22]]
    record_request()
    result = multiply_matrices(A, B)
    return {"matrix_A": A, "matrix_B": B, "result": result}
