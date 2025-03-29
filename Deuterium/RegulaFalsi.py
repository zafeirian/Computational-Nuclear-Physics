def FalsePosition(f,xl,xu,n, imax=200):
    # Setting the first value of xr_old in order to
    # calculate the first approximate error.
    xr_old = xl

    # Setting an iteration counter.
    iterations_fp = 0

    # Creating a list for storing all the xr values
    # and a list for storing all the approximate errors
    # in order to present the convergence of the method.
    xr_list = []
    err_a_list = []
    err_a = 100
    #Scarborough
    err_s = (0.5*10**(2-n))/100 #Calculating the Scarborough Error

    fl = f(xl)
    fu = f(xu)
    
#    lower_counter = 0  # MV: Counter for checking how many times did the lower boundary stayed the same.
#    upper_counter = 0  # MV: Counter for checking how many times did the upper boundary stayed the same.

    # Creating the loop of False Position Method.

    for i in range(imax):  #Maximum Iterations are set to 200.
        xr = xu - fu*(xl-xu)/(fl-fu)  # Calculating the xr.


        # Calculating the approximate error.
        if xr!=0 and iterations_fp>0:
            err_a = abs((xr - xr_old)/xr)    
            
        iterations_fp += 1   # Iteration counter. 
        # Storing xr and the approximate error on their corresponding lists.
        xr_list.append(xr) 
        err_a_list.append(err_a)

        # Checking if the approximate error is less than the Scarborough Error
        # in order to stop the iterations.
        if (err_a <= err_s):
            break

        fr=f(xr)
        if fl*fr<0: # Checking if the root is on the interval [xl,xr].
            xu = xr # Setting the upper boundary equal to xr for the next iteration.
            fu=f(xu)
#            lower_counter += 1  # MV: Lower boundary stayed the same one more time.
#            upper_counter = 0   # MV: Counter reset since the upper boundary changed.
#            if lower_counter>2: # MV: Checking if the lower boundary stayed the same for 3 iterations.
#                fl=fl/2       # MV: Halving the lower boundary.
        elif fl*fr>0:  # Checking if the root is on the interval [xr,xu].
            xl = xr # Setting the lower boundary equal to xr for the next iteration.
            fl=f(xl)
#           lower_counter = 0   # MV: Counter reset since the lower boundary changed.
#            upper_counter += 1  # MV: Upper boundary stayed the same one more time.
#            if upper_counter>2: # MV: Checking if the upper boundary stayed the same for 3 iterations.
#                fu=fu/2         # MV: Halving the upper boundary.
        else: # The scenario where xr is the root of the function.
            break # Stopping the iterations, since the root is found.

        # Storing the last value of xr to calculate the approximate error
        # in the next iteration. The algorithm works even if we don't use
        # the storing lists xr_list and err_a_list.
        xr_old = xr 

#    print(f'With a certainty of {n} significant figures, the root is found to be x = {xr}, after {iterations_fp} iterations.')
    return xr, iterations_fp
