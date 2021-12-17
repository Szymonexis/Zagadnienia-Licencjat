# Zagadnienia na licencjat

## 1. Ciągi liczb rzeczywistych. Zbieżność ciągu, warunek Cauchy'ego.

<h3>Definicja</h3>

**Ciągiem** nazywamy funkcję, której dziedziną jest zbiór liczb naturalnych $\mathbb{N}$ lub jego skończony odcinek początkowy $\{ 1, 2, 3, ... , m \}$.
Ciągiem liczbowym nazywamy ciąg, którego wyrazy są liczbami.

Liczbę $g$ nazywamy **granicą ciągu nieskończonego** $(a_n)$ , jeśli dla każdej liczby dodatniej  istnieje taka liczba $k$, że dla $n>k$ zachodzi nierówność:
$|a_n-g|< \epsilon$

Ciągiem **zbieżnym (rozbieżnym)** nazywamy ciąg, który **posiada granicę (nie posiada granicy)**.

<h3> Własności: </h3>

> 1. Jeśli ciąg posiada granicę to tylko jedną.
>
> 2. Każdy ciąg zbieżny jest ograniczony.
>
> 3. Przy założeniu, że ciągi $(a_n)$ i $(b_n)$ są zbieżne, zachodzą następujące wzory:
>    - $\lim_{n \to \infty} (a_n \pm b_n) = \lim_{n \to \infty} a_n \pm \lim_{n \to \infty} b_n$ (dla iloczynu i ilorazu też zachodzi)
>    - $\lim_{n \to \infty} - (a_n) = - \lim_{n \to \infty} a_n$
> 4. Jeżeli ciąg $(b_n)$ jest zbieżny i $\lim_{n \to \infty} \neq 0$, to $\lim_{n \to \infty} {1 \over b_n} = {1 \over {\lim_{n \to \infty} b_n}}$.
>
> 5. Jeżeli ciąg $(a_n)$ jest zbieżny, to $\lim_{n \to \infty} |a_n| = | \lim_{n \to \infty} a_n|$.
>
> 6. **(Tw. o trzech ciągach)**: Jeśli $a_n \leq c_n \leq b_n \;\; i \;\; \lim_{n \to\infty} a_n = g = \lim_{n\to\infty} b_n$ , to ciąg $(c_n)$ jest zbieżny, przy czym $\lim_{n \to\infty} c_n = \lim_{n \to\infty} b_n  = \lim_{n\to\infty} a_n$.
>
> 7. Zmiana skończonej ilości wyrazów ciągu nie wpływa na jego zbieżność/granicę.
>
> 8. Podciąg ciągu zbieżnego jest zbieżny do tej samej granicy, co ciąg dany.

<p>
<h3>Warunek Cauchy’ego:</h3>

$\forall_{\epsilon > 0} \;\;\exists_{n_0 \in \mathbb{N}}\;\;\forall_{n, m > n_0}\;\;(|a_n - a_m|<\epsilon)$  

*Po ludzku:*
Ciągi Cauchy'ego to takie ciągi, dla których odległości między wyrazami zmierzają do zera.
Oznacza to, że wybierając dowolnie małą dodatnią liczbę rzeczywistą $\epsilon$ , można ustalić odpowiednio duży wskaźnik $\mathbb{N}$ taki, że dowolne dwa wyrazy o wyższych wskaźnikach są odległe od siebie o mniej niż $\epsilon$.

<h3> Własności ciągu Cauchy'ego: </h3>

> 1. Ciąg $(a_n)^{\infty}_{n=1}$ jest zbieżny $\Longleftrightarrow$ gdy jest ciągiem Cauchy’ego. **(ale niekoniecznie odwrotnie)**.
>
> 2. Każdy ciąg Cauchy’ego jest ograniczony.
</p>

## 2. Macierze. Podstawowe operacje na macierzach. Rząd i wyznacznik macierzy.

Macierzą (rzeczywistą) wymiaru <i>m$\times$n</i>, gdzie m, n $\isin$ $\natnums$, nazywamy prostokątną tablicę złożoną z <i>m$\times$n</i> liczb rzeczywistych ustawionych w <i>m</i> wierszach i <i>n</i> kolumnach

$$
\left[\begin{array}{cc} 
a_{11} & a_{12} & \ldots & a_{1n}\\
a_{21} & a_{22} & \ldots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{m1} & a_{m2} & \ldots & a_{mn}\\
\end{array}\right]
$$ 

### Dzialania na macierzach

__Suma/różnica__ <br>
Niech macierz $A=[a_{ij}]$, $B=[b_{ij}]$. Sumą/różnicą nazywamy macierz $C=[c_{ij}]_{m\times n}$, której elementy określone są wzorami 

$$
c_{ij}=a_{ij}\plusmn b_{ij} \ dla \ i \isin\{1, 2, \ldots, m\}, j \isin\{1, 2, \ldots, n\}.
$$  
<br>
Piszemy wtedy 

$$
C=A\plusmn B
$$

Zatem,

$$
\left[\begin{array}{cc} 
c_{11} & c_{12} & \ldots & c_{1n}\\
c_{21} & c_{22} & \ldots & c_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
c_{m1} & c_{m2} & \ldots & c_{mn}\\
\end{array}\right]
\left[\begin{array}{cc}
a_{11}\plusmn b_{11} & a_{12}\plusmn b_{12} & \ldots & a_{1n}\plusmn b_{1n}\\
a_{21}\plusmn b_{21} & a_{22}\plusmn b_{22} & \ldots & a_{2n}\plusmn b_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{m1}\plusmn b_{m1} & a_{m2}\plusmn b_{m1} & \ldots & a_{mn}\plusmn b_{mn}\\
\end{array}\right]
$$ 

__Iloczyn macierzy przez liczbę__<br>
Niech $A=[a_{ij}]_{m\times n}, \alpha$ niech będzie dowolną liczbą rzeczywistą. Iloczynem macierzy $A$ przez liczbę $\alpha$ nazywamy macierz $B=[b_{ij}]_{m\times n}$ której elementy określone są następująco: <p align="center"> $b_{ij}=\alpha \cdot a_{ij}$ </p> dla $i \isin${$1, 2, \ldots, m$}, $j \isin${$1, 2, \ldots, n$}. Piszemy wtedy <p align="center">$B=\alpha \cdot A$</p> Zatem

$$
\left[\begin{array}{cc} 
b_{11} & b_{12} & \ldots & b_{1n}\\
b_{21} & b_{22} & \ldots & b_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
b_{m1} & b_{m2} & \ldots & b_{mn}\\
\end{array}\right]
\left[\begin{array}{cc}
\alpha \cdot a_{11} & \alpha \cdot a_{12} & \ldots &\alpha \cdot  a_{1n}\\
\alpha \cdot a_{21} & \alpha \cdot a_{22} & \ldots & \alpha \cdot a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
\alpha \cdot a_{m1} & \alpha \cdot a_{m2} & \ldots & \alpha \cdot a_{mn}\\
\end{array}\right]
$$ 

__Iloczyn macierzy__

Iloczyn macierzy $AB$ jest możliwy jeśli macierz $A$ ma tyle samo kolumn co macierz $B$ ma wierszy. Iloczynem macierzy $A=[a_{ij}]_{n\times p}$ przez macierz $B=[b_{ij}]_{p\times m}$ nazywamy macierz $C=[c_{ij}]_{n\times m}$ taką, że: 
$$
c_{ij}=a_{i1}b_{1j}+a_{i2}b_{2j}+\ldots +a_{ip}b_{pj}=\sum_{k=1}^{p} a_{ik}b_{kj}
$$
Własności iloczynu macierzy:
- mnożenie macierzy jest łączne $A(BC)=(AB)C$ dlatego zapis $ABC$ jest jednoznaczny
- mnożenie macierzy jest rodzielne względem dodawania $A(B+C)=AB+BC$ i $(B+C)A=BA+CA$
- mnożenie macierzy nie jest przemienne $AB\not =BA$

__Macierz transponowana__

Niech

$$
A=\left[\begin{array}{cc} 
-5 & 2 & 1\\
-1 & 6 & 2\\
2 & 0 & 1\\
2 & 64 & 5\\
\end{array}\right]
$$

Wówczas

$$
A^T=\left[\begin{array}{cc} 
-5 & -1 & 2 & 2\\
2 & 6 & 0 & 64\\
1 & 2 & 1 & 5\\
\end{array}\right]
$$

__Rząd macierzy__

Chcąc obliczyć rząd macierzy musimy znależć największą macierz, której wyznacznik jest różny od zera, wielkość tej niezerowej macierzy będzie szukaną wartością, czyli jeśli największą macierzą, której wyznacznik jest różny od zera jest macierz $3\times 3$ to rząd macierzy jest równy $3$.

_Przyklad_

$$
A=\left[\begin{array}{cc} 
2 & 8 & 3 & -4\\
1 & 4 & 1 & -2\\
5 & 20 & 0 & -10\\
-3 & -12 & -2 & 6\\
\end{array}\right]
$$

Aby obliczyć rząd macierzy zaczynamy od obliczenia wyznacznika największej macierzy czyli w tym przypadku $4\times 4$

$$
det(A)=\left|\begin{array}{cc} 
2 & 8 & 3 & -4\\
1 & 4 & 1 & -2\\
5 & 20 & 0 & -10\\
-3 & -12 & -2 & 6\\
\end{array}\right| = 0
$$

Następnie obliczamy macierze $3\times 3$ do momentu aż wyjdzie nam liczba różna od zera. Z macierzy $4\times 4$ można utowrzyć 16 macierzy $3\times 3$ w następujący sposób:

1. $$det(A)=\left|\begin{array}{cc} - & - & - & -\\\mid & 4 & 1 & -2\\\mid & 20 & 0 & -10\\\mid & -12 & -2 & 6\\\end{array}\right|$$
2. $$det(A)=\left|\begin{array}{cc} - & - & - & -\\1 & \mid & 1 & -2\\5 & \mid & 0 & -10\\-3 & \mid & -2 & 6\\\end{array}\right|$$
3. $\ldots$
4. $\ldots$
5. $\ldots$
6. $\ldots$
7. $\ldots$
8. $\ldots$
9. $\ldots$
10. $\ldots$
11. $$det(A)=\left|\begin{array}{cc} 2 & 8 & \mid & -4\\1 & 4 & \mid & -2\\- & - & - & -\\-3 & -12 & \mid & 6\\\end{array}\right|$$
12. $\ldots$
13. $\ldots$
14. $\ldots$
15. $\ldots$
16. $$det(A)=\left|\begin{array}{cc} 2 & 8 & 3 & \mid\\1 & 4 & 1 & \mid\\5 & 20 & 0 & \mid\\- & - & - & -\\\end{array}\right|$$
    
Jeżeli któraś z nich wyjdzie różna od zera to koniec obliczeń. Wystarczy że obliczając wyznacznik macierzy pierwszej $3\times 3$ wyjdzie nam liczba różna od zera - wtedy z automatu możemy powiedzieć, że rząd macierzy wynosi $3$. Analogicznie jeżeli wszystkie wzory wyjdą na $0$, to wtedy szukamy macierzy $2\times 2$ poprzez wykreślenie wiersza i kolumny analogicznie jak do kroków powyżej tak aby otrzymać macierz $2\times 2$ (czyli wykreślając po dwa wiersze i dwie kolumny).<br>
Dla macierzy

$$
\left[\begin{array}{cc} 
2 & 8 & 3 & -4\\
1 & 4 & 1 & -2\\
5 & 20 & 0 & -10\\
-3 & -12 & -2 & 6\\
\end{array}\right]
$$

operacja ta wygalda nastepująco:

$$
\left[\begin{array}{cc} 
- & - & - & -\\
- & - & - & -\\
\mid & \mid & 0 & -10\\
\mid & \mid & -2 & 6\\
\end{array}\right]
\rArr
\left[\begin{array}{cc}
0 & -10\\
-2 & 6\\
\end{array}\right]
$$

__Wyznacznik macierzy__

$1\times 1:$ $det(A)=\left|\begin{array}{cc}5\\\end{array}\right|=5$<br>
$2\times 2:$ $det(A)=\left|\begin{array}{cc} a_{11} & a_{12}\\ a_{21} & a_{22}\\\end{array}\right|=a_{11}\cdot a_{22} - a_{21}\cdot a_{12}$<br>
$3\times 3:$ np. Metoda Sarrusa

1. Dopisujemy z prawej kolumny $1$ oraz $2$<br>$det(A)=\left|\begin{array}{cc} a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33}\end{array}\right|\begin{array}{cc} a_{11} & a_{12}\\ a_{21} & a_{22}\\ a_{31} & a_{32}\\\end{array}$
2. Następnie wymnażamy wyrazy zaznaczone kolorem<br>$det(A)=\left|\begin{array}{cc} \color{blue}a_{11} & \color{green}a_{12} & \color{red}a_{13}\\ a_{21} & \color{blue}a_{22} & \color{green}a_{23}\\ a_{31} & a_{32} & \color{blue}a_{33}\end{array}\right|\begin{array}{cc} a_{11} & a_{12}\\ \color{red}a_{21} & a_{22}\\ \color{green}a_{31} & \color{red}a_{32}\\\end{array}$<br>czyli<br>$a_{11}\cdot a_{22}\cdot a_{33} + a_{12}\cdot a_{23}\cdot a_{31} + a_{13}\cdot a_{21}\cdot a_{32}$
3. Analogicznie w drugą stronę<br>$det(A)=\left|\begin{array}{cc} a_{11} & a_{12} & \color{blue}a_{13}\\ a_{21} & \color{blue}a_{22} & \color{green}a_{23}\\ \color{blue}a_{31} & \color{green}a_{32} & \color{red}a_{33}\end{array}\right|\begin{array}{cc} \color{green}a_{11} & \color{red}a_{12}\\ \color{red}a_{21} & a_{22}\\ a_{31} & a_{32}\\\end{array}$<br>czyli<br>$a_{13}\cdot a_{22}\cdot a_{31} + a_{11}\cdot a_{23}\cdot a_{32} + a_{12}\cdot a_{21}\cdot a_{33}$
4. Następnie od wielomianu z kroku $2$ odejmujemy wielomian z kroku $3$:<br>$(a_{11}\cdot a_{22}\cdot a_{33} + a_{12}\cdot a_{23}\cdot a_{31} + a_{13}\cdot a_{21}\cdot a_{32}) - (a_{13}\cdot a_{22}\cdot a_{31} + a_{11}\cdot a_{23}\cdot a_{32} + a_{12}\cdot a_{21}\cdot a_{33})$
   
$4\times 4:$ np. Rozwinięcie Laplace'a

Szukamy w macierzy wiersza lub kolumny która ma najwięcej zer (dla łatwiejszego obliczania). Na przykład:

Dla macierzy

$$
\left[\begin{array}{cc} 
1 & -1 & 2 & 4\\
0 & 1 & 0 & 3\\
5 & 7 & -2 & 0\\
2 & 0 & -1 & 4\\
\end{array}\right]
$$

Sytuacja wyglada tak:

$$
\left|\begin{array}{cc} 
\color{red}1 & \color{green}-1 & \color{blue}2 & \color{magenta}4\\
0 & 1 & 0 & 3\\
\color{red}5 & \color{green}7 & \color{blue}-2 & \color{magenta}0\\
\color{red}2 & \color{green}0 & \color{blue}-1 & \color{magenta}4\\
\end{array}\right|=\color{red}0\color{default}\cdot (-1)^{2+1}\cdot \left|\begin{array}{cc}-1 & 2 & 4\\7 & -2 & 0\\0 & -1 & 4\\\end{array}\right| + \color{green}1\color{default}\cdot (-1)^{2+2}\cdot \left|\begin{array}{cc}1 & 2 & 4\\5 & -2 & 0\\2 & -1 & 4\\\end{array}\right| + \color{blue}0\color{default}\cdot (-1)^{2+3}\cdot \left|\begin{array}{cc}1 & -1 & 4\\5 & 7 & 0\\2 & 0 & 4\\\end{array}\right| + \color{magenta}3\color{default}\cdot (-1)^{2+4}\cdot \left|\begin{array}{cc}1 & -1 & 2\\5 & 7 & -2\\2 & 0 & -1\\\end{array}\right| =
$$
$$
\color{green}((1\cdot (-2)\cdot 4 + 2\cdot 0\cdot 2 + 4\cdot 5\cdot (-1)) - (2\cdot (-2)\cdot 4 + 1\cdot 0\cdot (-1) + 4\cdot 5\cdot 2)) \color{default}+ \color{magenta}3\cdot((1\cdot 7\cdot (-1) + (-1)\cdot (-2)\cdot 2 + 2\cdot 5\cdot 0)-(2\cdot 7\cdot 2 + 1\cdot (-2)\cdot 0 + (-1)\cdot (-1)\cdot 5))\color{default} =
$$
$$
\color{green}((-8 + 0 + (-20))-((-16) + 0 + 40))\color{default} + \color{magenta}3\cdot(((-7) + 4 + 0)-(28 + 0 + 5))\color{default} = 
$$
$$
\color{green}((-28)-(24))\color{default} + \color{magenta}3\cdot((-3)-(33))\color{default} = 
$$
$$
\color{green}(-52)\color{default} + \color{magenta}3\cdot(-36)\color{default} = 
$$
$$
\color{green}-52\color{default} + \color{magenta}-108\color{default} = -160
$$

Gdzie po równaniu pierwsza liczba to liczba $z$ wiersza $m$ i kolumny $n$ pomnożone przez $(-1)$ do potegi $(m+n)$ razy macierz po wykreśleniu wiersza $m$ i kolumny $n$. Następne dodajemy analogicznie.

__Maceirz odwrotna $(A^{-1})$__

Wzór:

$$
A^{-1}=(A^D)^T\cdot \frac{1}{det(A)}
$$

gdzie:

* $A^{-1}$ - macierz odwrotna
* $A^D$ - macierz dopełnień algebraicznych
* $(A^D)^T$ - macierz dołączona - czyli transponowana z macierzy dopełnień algebraicznych
* $det(A)$ - wyznacznik macierzy

Nie można obliczyć macierzy odwrotnej z macierzy osobliwej, czyli takiej której wyznacznik jest równy $0$. Więc jeśli liczymy macierz odwrotną zawsze zaczynamy od obliczania wyznacznika macierzy, jeśli wyjdzie on $0$ to znaczy, że z danej macierzy nie można obliczyć macierzy odwrotnej.

___Macierz odwrotna jest określona tylko dla macierzy kwadratowych, których wyznacznik $W$ jest $W\not ={0}$.___ <br>
Macierz odwrotna $A^{-1}$ do macierzy kwadratowej $A$ to macierz spełniająca równanie $A^{-1}\cdot A=A\cdot A^{-1}=I$, gdzie $I$ to macierz jednostkowa.<br>
Jeśli macierz $A^{-1}$ istnieje to macierz $A$ nazwyamy ___odwracalną___, a jeśli macierz $A^{-1}$ nie istnieje to macierz $A$ nazywamy ___nieodwracalną___.<br>
Jeśli macierz $A$ jest odwracalna to istnieje tylko jedna macierz odwrotna $A^{-1}$

__Własności macierzy odwrotnej__

* macierzą odwrotną od macierzy jednostkowej jest ta sama macierz tzn. $I^{-1}=I$
* $(diag(a_{11},a_{22},\ldots ,a_{nn}))^{-1}=diag((a_{11})^{-1},(a_{22})^{-1},\ldots, (a_{nn})^{-1})$
* $(A^{-1})^{-1}=A$
* $(A^{-1})^{T}=(A^{T})^{-1}$
* $(cA)^{-1}=c^{-1}A^{-1}$, gdzie $c$ to stała
* $(AB)^{-1}=B^{-1}A^{-1}$
* $det(A^{-1})=(det(A))^{-1}$
* macierz odwrotna do nieosobliwej macierzy symetrycznej jest symmetryczna
* macierz odwrotna do nieosobliwej macierzy trójkątej jest trójkątna
> ___Macierz nieosobliwa___ - macierz kwadratowa o wyznaczniku róznym od zera<br>
> ___Macierz symetryczna___ - macierz kwadratowa której wyrazy położone symetrycznie względem przekątnej głównej są równe, przykład:
> $$\left[\begin{array}{cc}a_{11} & a_{2} & \ldots & a_{n}\\a_{2} & a_{22} & \ldots & a_{n-1}\\\vdots & \vdots & \ddots & \vdots\\ a_{n}& a_{n-1} & \ldots & a_{nn}\\\end{array}\right]$$

___Proces obliczania macierzy odwrotnej dla macierzy $3\times 3$___
$$
B=
\left[\begin{array}{cc}
a_{11}& a_{12} &a_{13}\\
a_{21}& a_{22} &a_{23}\\
a_{31}& a_{32} &a_{33}\\
\end{array}\right]
=
\left[\begin{array}{cc}
2 & 5 & 7\\
6 & 3 & 4\\
5 & -2 & -3\\
\end{array}\right]
$$

Podobnie jak wcześniej najpierw obliczamy wyznacznik macierzy $3\times 3$:

$$
det(B)=
\left|\begin{array}{cc}
2 & 5 & 7\\
6 & 3 & 4\\
5 & -2 & -3\\
\end{array}\right|
= -1
$$

Następnie obliczamy macierz dopełnień algebraicznych:

$$
B^D=
\left[\begin{array}{cc}
+
\left|\begin{array}{cc}
a_{22} & a_{23}\\
a_{32} & a_{33}\\
\end{array}\right|& 
-
\left|\begin{array}{cc}
a_{21} & a_{23}\\
a_{31} & a_{33}\\
\end{array}\right| &
+
\left|\begin{array}{cc}
a_{21} & a_{22}\\
a_{31} & a_{32}\\
\end{array}\right|\\
-
\left|\begin{array}{cc}
a_{12} & a_{13}\\
a_{32} & a_{33}\\
\end{array}\right|& 
+
\left|\begin{array}{cc}
a_{11} & a_{13}\\
a_{31} & a_{33}\\
\end{array}\right| &
-
\left|\begin{array}{cc}
a_{11} & a_{12}\\
a_{31} & a_{33}\\
\end{array}\right|\\
+
\left|\begin{array}{cc}
a_{12} & a_{13}\\
a_{22} & a_{23}\\
\end{array}\right|& 
-
\left|\begin{array}{cc}
a_{11} & a_{13}\\
a_{21} & a_{23}\\
\end{array}\right| &
+
\left|\begin{array}{cc}
a_{11} & a_{12}\\
a_{21} & a_{22}\\
\end{array}\right|\\
\end{array}\right]
$$

czyli

$$
B^D=
\left[\begin{array}{cc}
+
\left|\begin{array}{cc}
3 & 4\\
-2 & -3\\
\end{array}\right|& 
-
\left|\begin{array}{cc}
6 & 4\\
5 & -3\\
\end{array}\right| &
+
\left|\begin{array}{cc}
6 & 3\\
5 & -2\\
\end{array}\right|\\
-
\left|\begin{array}{cc}
5 & 7\\
-2 & -3\\
\end{array}\right|& 
+
\left|\begin{array}{cc}
2 & 7\\
5 & -3\\
\end{array}\right| &
-
\left|\begin{array}{cc}
2 & 5\\
5 & -2\\
\end{array}\right|\\
+
\left|\begin{array}{cc}
5 & 7\\
3 & 4\\
\end{array}\right|& 
-
\left|\begin{array}{cc}
2 & 7\\
6 & 4\\
\end{array}\right| &
+
\left|\begin{array}{cc}
2 & 5\\
6 & 3\\
\end{array}\right|\\
\end{array}\right]
$$

Więc:

$$
B^D=
\left[\begin{array}{cc}
-1 & 38 & -27 \\
1 & -41 & 29 \\
-1 & 34 & -24 \\
\end{array}\right]
$$

Następnie obliczamy macierz transponowaną:

$$
(B^D)^T=
\left[\begin{array}{cc}
-1 & 1 & -1 \\
38 & -41 & 34 \\
-27 & 29 & -24 \\
\end{array}\right]
$$

więc macierz odwrotna będzie miała postać:

$$
\frac{(B^D)^T}{det(B)}=
\left[\begin{array}{cc}
1 & -1 & 1 \\
-38 & 41 & -34 \\
27 & -29 & 24 \\
\end{array}\right]
$$

__Ślad macierzy__

Ślad macierzy jest to suma elementów leżących na przekątnej danej macierzy. Ślad macierzy definujemy tylko dla macierzy kwadratowej. Ślad macierzy kwadratowej $A=[a_{ij}]$ stopnia $n$ jest sumą elementów leżących na głównej przekątnej (diagonali). Ślad macierzy oznaczamy $Tr(A), TrA$ lub $trace(A)$.

$$
Tr(A) = \sum_{i=1}^{n}{a_{ii}} = a_{11} + a_{22} + \ldots + a_{nn}
$$

Mając macierz

$$
A=
\left[\begin{array}{cc}
1 & 2 & 4 & -4\\
-3 & 4 & -6 & 12\\
-9 & 2 & -1 & 3\\
5 & 0 & 2 & 1\\
\end{array}\right]
$$

obliczamy ślad macierzy w następujący sposób:

$$
tr(A)=tr
\left[\begin{array}{cc}
\color{red}1 & 2 & 4 & -4\\
-3 & \color{red}4 & -6 & 12\\
-9 & 2 & \color{red}-1 & 3\\
5 & 0 & 2 & \color{red}1\\
\end{array}\right] = 1 + 4 + (-1) + 1 = 5
$$

__Własności śladu macierzy__

* jeśli macierze $A=a_{ij}$ i $B=b_{ij}$ są macierzami kwadratowymi tego samego stopnia to: $Tr(A+B)=Tr(A)+Tr(B)$
* jeśli macierz $A=a_{ij}$ jest macierzą kwadratową, a $\alpha$ jest liczbą rzeczywistą to: $Tr(\alpha A)=\alpha Tr(A)$
* jeśli $A\isin M_n$ a $B\isin M_n$ to: $Tr(AB)=Tr(BA)$
* jeśli $A\isin M_n$, $B\isin M_n$ i $C\isin M_n$ (cykliczna przemieenność śladu) to: $Tr(ABC)=Tr(CAB)=Tr(BCA)$
* przekątna główna mecierzy nie ulegnie zmianie przy transpozycji: $Tr(A)=Tr(A^T)$

## 3. Rozwiązywanie układów równań liniowych.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 4. Rachunek zdań. Tautologie.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 5. Indukcja matematyczna.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 6. Permutacje, wariacje i kombinacje.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 7. Klasyczna definicja prawdopodobieństwa. Prawdopodobieństwo geometryczne.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 8. Struktura logiczna i funkcjonalna klasycznego komputera.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 9. Reprezentacja liczb w pozycyjnym systemie liczbowym. Systemy dwójkowy i szesnastkowy oraz ich zastosowania.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 10. Arytmetyka stałopozycyjna i zmiennopozycyjna. Reprezentacja liczb w komputerze.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 11. System operacyjny. Postrzeganie systemu operacyjnego przez warstwę oprogramowania użytkowego.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 12. Cechy tradycyjnego systemu unixowego.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 13. Iteracja, rekurencja i ich realizacja.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 14. Mechanizmy strukturalizacji programów - instrukcje warunkowe i pętle.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 15. Podprogramy. Przekazywanie parametrów podprogramu.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 16. Porównanie programowania obiektowego i strukturalnego.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 17. Hermetyzacja danych - cechy klas obiektowych (pola, metody, poziomy prywatności danych).

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 18. Typy metod: konstruktory, destruktory, selektory, zapytania, iteratory.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 19. Dziedziczenie i dynamiczny polimorfizm.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 20. Polimorfizm statyczny – szablony.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 21. Listy i drzewa oraz ich zastosowania. Stosy i kolejki.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 22. Grafy i metody ich przeszukiwania. Zastosowania.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 23. Metody projektowania algorytmów (dziel i rządź, programowanie dynamiczne i algorytmy zachłanne).

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 24. Elementarne i nieelementarne metody sortowania.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 25. Elementarne metody wyszukiwania. Haszowanie.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 26. Złożoność obliczeniowa algorytmu. Przykłady.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 27. Pojęcie bazy danych - funkcje i możliwości.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 28. Relacja i jej atrybuty w bazach danych.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 29. Spójność referencyjna baz danych.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 30. Normalizacja relacji - postaci normalne.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 31. Modelowanie bazy danych - rodzaje połączeń relacyjnych, pojęcie klucza głównego i obcego.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 32. Pojęcie indeksu - rodzaje i zastosowanie.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 33. Podstawowe konstrukcje języka SQL.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 34. Warstwy i funkcje modelu ISO OSI.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 35. Adresowanie logiczne w sieciach komputerowych.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 36. Najważniejsze protokoły rodziny TCP/IP.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 37. Cykle życia oprogramowania.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 38. Proces testowania i jego rola w tworzeniu oprogramowania.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 39. UML, jego struktura i przeznaczenie.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 40. Podstawowe funkcje w zespole projektowym i ich role.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 41. Pojęcie Maszyny Turinga - idea pracy automatu, hipoteza Churcha-Turinga

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 42. Usługa translacji adresów w sieci TCP/IP.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 43. Mechanizm trasowania (ang. routing) pakietów w Internecie.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 44. Usługi nazewnicze sieci TCP/IP.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 45. Zarządzanie konfiguracją urządzenia w sieci TCP/IP.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 46. Wirtualne sieci lokalne.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 47. Technologie redundantne w sieciach komputerowych.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 48. Metody optymalizacji zapytań SQL.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 49. Modele uwierzytelniania, autoryzacji i kontroli dostępu do systemów komputerowych.

<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>

## 50. Teoretyczne modele komputerów: automaty skończone, automaty ze stosem, maszyny Turinga i odpowiadające im klasy języków formalnych.
<a href="<link_to_resource_local_or_online_here>"></a><b></b>
<table align="center">
    <thead>
        <tr>
            <th>Ex. 1</th>
            <th>Ex. 2</th>
            <th>Ex. 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ts</td>
            <td>Ts</td>
            <td>Ts</td>
        </tr>
    </tbody>
</table>
