def centralDifferenceFirst(f : callable, x : float, h : float = 10e-5 ):
    """
    Calculates the first derivative of a function using the central difference method.

    Parameters:
    - f (callable): The function to differentiate.
    - x (float): The point at which to evaluate the derivative.
    - h (float, optional): The step size. Default is 10e-5.

    Returns:
    - float: The approximate value of the first derivative at the given point.
    """
    return (f(x+h) - f(x-h))/(2*h)

def centralDifferenceSecond(f : callable, x : float, h : float = 10e-5):
    """
    Calculates the second derivative of a function using the central difference method.

    Parameters:
    - f (callable): The function to differentiate.
    - x (float): The point at which to evaluate the derivative.
    - h (float, optional): The step size. Default is 10e-5.

    Returns:
    - float: The approximate value of the second derivative at the given point.
    """
    return (f(x+2*h) - 2*f(x+h) + 2*f(x-h) - f(x-2*h))/(2 * h**3)

def forwardDifferenceFirst(f : callable, x : float, h : float = 10e-5):
    """
    Calculates the first derivative of a function using the forward difference method.

    Parameters:
    - f (callable): The function to differentiate.
    - x (float): The point at which to evaluate the derivative.
    - h (float, optional): The step size. Default is 10e-5.

    Returns:
    - float: The approximate value of the first derivative at the given point.
    """
    return (f(x+h) - f(x))/h

def backwardDifferenceFirst(f : callable, x : float, h : float = 10e-5):
    """
    Calculates the first derivative of a function using the backward difference method.

    Parameters:
    - f (callable): The function to differentiate.
    - x (float): The point at which to evaluate the derivative.
    - h (float, optional): The step size. Default is 10e-5.

    Returns:
    - float: The approximate value of the first derivative at the given point.
    """
    return (f(x) - f(x-h))/h

def nonCentranDifferenceSecond1(f : callable, x : float, h : float = 10e-5):
    """
    Calculates the second derivative of a function using a non-central difference method.

    Parameters:
    - f (callable): The function to differentiate.
    - x (float): The point at which to evaluate the derivative.
    - h (float, optional): The step size. Default is 10e-5.

    Returns:
    - float: The approximate value of the second derivative at the given point.
    """
    return (-3*f(x) + 4*f(x+h) - f(x+2*h))/(2*h)

def nonCentranDifferenceSecond2(f : callable, x : float, h : float = 10e-5):
    """
    Calculates the second derivative of a function using a non-central difference method.

    Parameters:
    - f (callable): The function to differentiate.
    - x (float): The point at which to evaluate the derivative.
    - h (float, optional): The step size. Default is 10e-5.

    Returns:
    - float: The approximate value of the second derivative at the given point.
    """
    return (2*f(x) - 5*f(x+h) + 4*f(x+2*h) - 1*f(x+3*h))/(h**2)

def nonCentranDifferenceSecond3(f : callable, x : float, h : float = 10e-5):
    """
    Calculates the second derivative of a function using a non-central difference method.

    Parameters:
    - f (callable): The function to differentiate.
    - x (float): The point at which to evaluate the derivative.
    - h (float, optional): The step size. Default is 10e-5.

    Returns:
    - float: The approximate value of the second derivative at the given point.
    """
    return (-5*f(x) + 18*f(x+h) - 24*f(x+2*h) + 14*f(x+3*h) - 3*f(x+4*h))/(2*h**3)

def nonCentranDifferenceSecond4(f : callable, x : float, h : float = 10e-5):
    """
    Calculates the second derivative of a function using a non-central difference method.

    Parameters:
    - f (callable): The function to differentiate.
    - x (float): The point at which to evaluate the derivative.
    - h (float, optional): The step size. Default is 10e-5.

    Returns:
    - float: The approximate value of the second derivative at the given point.
    """
    return (3*f(x) - 14*f(x+h) + 26*f(x+2*h) - 24*f(x+3*h) + 11*f(x+4*h) - 2*f(x+5*h))/(h**4)

def getNthDiff(baseFunc : callable, x : float, n : int = 1, h : float = 10e-5):
    """
    Calculates the nth derivative of a function using recursion.

    Parameters:
    - baseFunc (callable): The base function to differentiate.
    - x (float): The point at which to evaluate the derivative.
    - n (int, optional): The order of the derivative. Default is 1.
    - h (float, optional): The step size. Default is 10e-5.

    Returns:
    - float: The approximate value of the nth derivative at the given point.
    """
    if(n == 1):
        return forwardDifferenceFirst(baseFunc, x, h)
    elif(n == 0):
        return baseFunc(x)
    
    a = getNthDiff(baseFunc, x, n-1, h)
    b = getNthDiff(baseFunc, x+h, n-1, h)
    return (b - a)/h
