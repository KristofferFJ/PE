import unittest

# Lambda Count
"""
The lambda-calculus is a universal model of computation at the core of functional programming languages. It is based on lambda-terms, a minimal programming language featuring only function definitions, function calls and variables. Lambda-terms are built according to the following rules:
A lambda-term $T$ is said to be closed if for all variables $x$, all occurrences of $x$ within $T$ are contained within some abstraction $(\lambda x. M)$ in $T$. The smallest such abstraction is said to bind the occurrence of the variable $x$. In other words, a lambda-term is closed if all its variables are bound to parameters of enclosing functions definitions. For example, the term $(\lambda x. x)$ is closed, while the term $(\lambda x. (x y))$ is not because $y$ is not bound.
Also, we can rename variables as long as no binding abstraction changes. This means that $(\lambda x. x)$ and $(\lambda y. y)$ should be considered equivalent since we merely renamed a parameter. Two terms equivalent modulo such renaming are called $\alpha$-equivalent. Note that $(\lambda x. (\lambda y. (x y)))$ and $(\lambda x. (\lambda x. (x x)))$ are not $\alpha$-equivalent, since the abstraction binding the first variable was the outer one and becomes the inner one. However, $(\lambda x. (\lambda y. (x y)))$ and $(\lambda y. (\lambda x. (y x)))$ are $\alpha$-equivalent.
The following table regroups the lambda-terms that can be written with at most $15$ symbols, symbols being parenthesis, $\lambda$, dot and variables.
Let be $\Lambda(n)$ the number of distinct closed lambda-terms that can be written using at most $n$ symbols, where terms that are $\alpha$-equivalent to one another should be counted only once. You are given that $\Lambda(6) = 1$, $\Lambda(9) = 2$, $\Lambda(15) = 20$ and $\Lambda(35) = 3166438$.
Find $\Lambda(2000)$. Give the answer modulo $1\,000\,000\,007$.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
