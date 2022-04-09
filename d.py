K = float(input())
N = int(input())
R = int(input())

P = pow(1-K, N)

geometric_pdfs = [P*(1-P)**(i-1) for i in range(1,R+1)]

print(sum(geometric_pdfs))