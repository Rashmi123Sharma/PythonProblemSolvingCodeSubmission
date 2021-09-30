#Problem Set 2
#Name: Rashmi Sharma
#Time Spent : 1 day

#Problem#1

def evaluate_poly(poly,x):
    result=0
    for i in range(0,len(poly)):
        result+=poly[i]*x**i
    return result
poly=(0.0,0.0,5.0,9.3,7.0)
x= -13
print(evaluate_poly(poly,x))


#Problem#2

def compute_deriv(poly):
    result=()
    for i in range(1,len(poly)):
        result += (poly[i]*(i),)
    return result
poly =(-13.39,0.0,17.5,3.0,1.0)
print(compute_deriv(poly))



#Problem#3

def compute_root(poly, x_0, epsilon):
    iteration_counter = 1
    while (abs(evaluate_poly(poly,x_0)) > epsilon):
        iteration_counter += 1
        x_0 = x_0 - (evaluate_poly(poly,x_0)/ (evaluate_poly(compute_deriv(poly),x_0)))
    return (x_0,iteration_counter)
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = 0.0001
print(compute_root(poly , x_0 , epsilon))

