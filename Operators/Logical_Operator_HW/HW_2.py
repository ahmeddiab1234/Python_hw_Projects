# HW - 2 - Operator - Logical Operator - Simplify expressions

'''
1 - T and T and F and T
There is F and something then it will be False

2 - T and T and F and T or T and T
There is F and something then it will be False

3 - T and T and T and T or T and (T or F)
(T or F) = T
(T and T and T and T) = T
T or T and T = T or T = T

4 - T and T and T or T and (F or (T and (T and T)))
(T and T) = T 
    T and T and T or T and (F or (T and T))
(T and T) = T
    T and T and T or T and (F or T)
(F or T) = T
    T and T and T or T and T 
T or T = T

5 - T and T or T and F and T or T and T and F or (T and (T or F))
(T and (T or F)) = T and T = T
    T and T or T and F and T or T and T and F or T
(T and T) = T, (T and F) = F
    T or F and T or T and T and F or T
(F and T) = F, (T and T and F) = F
    T or F or F or T = T

6 - (T and T or T and F and T or T) and T and F or (T and (T or F))
(T and (T or F)) = T and T = T
    (T and T or T and F and T or T) and T and F or T
(T and T or T and F and T or T) = T or F or T = T
    T and T and F or T
F or T = T

7 - T and T or T and (F and T or T and T) and F or (T and (T or F))
(T and (T or F)) = T and T = T
    T and T or T and (F and T or T and T) and F or T
(F and T or T and T) = F or T = T
    T and T or T and T and F or T
T or F or T = T

'''

