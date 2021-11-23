def zero(operator: callable = int) -> int: return operator(0)
def one(operator: callable = int) -> int: return operator(1)
def two(operator: callable = int) -> int: return operator(2)
def three(operator: callable = int) -> int: return operator(3) 
def four(operator: callable = int) -> int: return operator(4)
def five(operator: callable = int) -> int: return operator(5)
def six(operator: callable = int) -> int: return operator(6)
def seven(operator: callable = int) -> int: return operator(7) 
def eight(operator: callable = int) -> int: return operator(8)
def nine(operator: callable = int) -> int: return operator(9)


def plus(operand: int) -> callable: return int(operand).__add__
def minus(operand: int) -> callable: return int(operand).__rsub__
def times(operand: int) -> callable: return int(operand).__mul__
def divided_by(operand: int) -> callable: return int(operand).__rfloordiv__
