syms x y z l1 l2a l2b l3a l3b eq1 eq2 eq3
A = [(l1 + l2a), -l2b, -l1, -eq1; l2a, -(l1 +l2b), -l1, - eq2; l2a, -l2b, -(l3a + l3b), -eq3];
rref(A)