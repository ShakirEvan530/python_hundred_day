a = float(input())
if a<=400.00:
    a1 =a+a*0.15
    b1=a1-a
    print(f"Novo salario: {a1:.2f}")
    print(f"Reajuste ganho: {b1:.2f}")
    print(f"Em percentual: {(b1/a)*100:.0f} %")
elif a>=400.01 and a<=800:
    a2=a+a*0.12
    b2=a2-a
    print(f"Novo salario: {a2:.2f}")
    print(f"Reajuste ganho: {b2:.2f}")
    print(f"Em percentual: {(b2/a)*100:.0f} %")
elif a>=800.01 and a<=1200:
    a3=a+a*0.10
    b3=a3-a
    print(f"Novo salario: {a3:.2f}")
    print(f"Reajuste ganho: {b3:.2f}")
    print(f"Em percentual: {(b3/a)*100:.0f} %")
elif a>=1200.01 and a<=2000:
    a4=a+a*0.07
    b4=a4-a
    print(f"Novo salario: {a4:.2f}")
    print(f"Reajuste ganho: {b4:.2f}")
    print(f"Em percentual: {(b4/a)*100:.0f} %")
else:
    a5=a+a*0.04
    b5=a5-a
    print(f"Novo salario: {a5:.2f}")
    print(f"Reajuste ganho: {b5:.2f}")
    print(f"Em percentual: {(b5/a)*100:.0f} %")
