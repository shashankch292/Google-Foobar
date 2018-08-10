'''
**************************************
Python Solution
**************************************
'''

from itertools import product
from fractions import Fraction
from functools import reduce
#this is for matrix inversion
def invert(matrix):
    n = len(matrix)
    inverse = [[Fraction(0) for col in range(n)] for row in range(n)]
    for i in range(n):
        inverse[i][i] = Fraction(1)
    for i in range(n):
        for j in range(n):
            if i != j:
                if matrix[i][i] == 0:
                    return False
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(n):
                    inverse[j][k] = inverse[j][k] - ratio * inverse[i][k]
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
    for i in range(n):
        a = matrix[i][i]
        if a == 0:
            return False
        for j in range(n):
            inverse[i][j] = inverse[i][j] / a
    return inverse
#finding sum of a row in matrix
def sumRow(m, r):
    return sum(m[r])
#subtracting two matrices
def substract(matr_a, matr_b):
    output = []
    for i in range(len(matr_a)):
        tmp = []
        for valA, valB in zip(matr_a[i], matr_b[i]):
            tmp.append(valA - valB)
        output.append(tmp[:])
    return output[:]
#matrix multiplication
def matrixmult(matr_a, matr_b):
    #cols = len(matr_b[0])
    rows = len(matr_b)
    if rows is not 0:
        cols = len(matr_b[0])
    else:
        cols = 0
    resRows = range(len(matr_a))
    rMatrix = [[0] * cols for _ in resRows]
    for idx in resRows:
        for j, k in product(range(cols), range(rows)):
            rMatrix[idx][j] += matr_a[idx][k] * matr_b[k][j]
    if cols is not 0:
        return rMatrix
    else:
        return 0
    # return rMatrix
#gcd to find lcm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
#lcm to find last value of the output
def lcm(a,n):
    ans = a[0]
    for i in range(1,n):
        ans = (a[i]*ans)//gcd(a[i],ans)
    return ans
#main function
def answer(m):
    num = len(m)
    if(num==1):
	return [1,1]
    f=[]
    store=list(m)
    #finding zero rows
    for i in range(0,num):
        j=[]
        j.append(sumRow(m,i))
        j.append(i)
        f.append(j)
    k=0;
    #Fraction Conversion
    for i in range(0,num):
        for j in range(0,num):
            if f[i][0]!=0:
                m[i][j]=Fraction(m[i][j],f[i][0])
    j=[]
    for i in range(0,len(f)):
        if f[i][0].numerator==0:
            j.append(i)
            del m[f[i][1]-k]
            k=k+1
    q=m
    k=[]
    t=0
    e=m
   # print(m)
    q=[]
    for i in range(0,len(m)):
        row=[]
        for r in range(0,len(m[0])):
            for t in range(0,len(j)):
                if j[t] is r:
                    row.append(m[i][r])
        q.append(row)
   # print(q)
    t=0;
    w=0;
    e=[]
    #hello-----------------
    for i in range(len(f)):
        if f[i][0]!=0:
            row=[]
            for j in range(len(f)):
                if f[j][0]!=0:
                    row.append(store[i][j])
            e.append(row)
    '''for i in range(0,len(m)):
        row=[]
        flag=1
        for r in range(0,len(m[0])):
            for t in range(0,len(j)):
                if j[t] is r:
                    flag=0
                    break
            if flag is 1:
                row.append(m[i][r])
        e.append(row)'''
    #print(e)
    l=[]
    for i in range(0,len(e)):
        k=[]
        for b in range(0,len(e)):
            if i==b:
                k.append(1)
            else:
                k.append(0)
        l.append(k)
    #print(l)
    #print(e)
    l=substract(l,e)
    #print(l)
    l=invert(l)
    r = matrixmult(l,q)
    #print(r)
    if r == 0:
        return 0
    else:
        m =r[0]
    e=[]
    for i in range(0,len(m)):
        e.append(m[i].denominator)
    k=lcm(e,len(e))
    e=[]
    for i in range(0,len(m)):
        e.append((m[i].numerator*k)//m[i].denominator)
    e.append(k)
    #print(e)
    return e


'''
**************************************
Java Solution (Some error)
**************************************

package com.google.challenges; 
import java.math.*;

public class Answer {  
    public static void getCofactor(BigInteger[][] a,BigInteger[][] temp,int p,int q,int n,int nn)
    {
        int i=0,j=0;
        
        for(int row=0;row<nn;row++)
        {
            for(int col=0;col<nn;col++)
            {
                if(row!=p&&col!=q)
                {
                    temp[i][j++]=a[row][col];
                    
                    if(j==nn-1)
                    {
                        j=0;
                        i++;
                    }
                }
            }
        }
    }
    
    public static BigInteger determinant(BigInteger[][] a,int n,int nn)
    {
        BigInteger d=BigInteger.ZERO;
        if(nn==1)
            return a[0][0];
        
        BigInteger[][] temp=new BigInteger[n][n];
        int sign=1;
        
        for(int f=0;f<nn;f++)
        {
            getCofactor(a,temp,0,f,n,nn);
            d=d.add((BigInteger.valueOf(sign)).multiply(a[0][f]).multiply(determinant(temp,n,nn-1)));
            sign=-sign;
        }
        return d;
    }
    
    public static void adjoint(BigInteger[][] a,BigInteger[][] fi,int n)
    {
        if(n==1)
        {
            fi[0][0]=BigInteger.ONE;
            return;
        }
        
        int i,j,sign=1;
        BigInteger[][] temp=new BigInteger[n][n];
        
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                getCofactor(a,temp,i,j,n,n);
                sign=((i+j)%2==0)?1:-1;
                fi[j][i]=(BigInteger.valueOf(sign)).multiply(determinant(temp,n,n-1));
            }
        }
    }
    
    public static int[] answer(int[][] m) 
    {
        int rl=m.length,cl=m[0].length;
        if(rl==1)
        {
            int[] res={1,1};
            return res;
        }
        long[][] mn=new long[rl][cl];
        int i,j,k=0,cnt=0,flag;
        int[] ord=new int[rl];
        
        for(i=0;i<rl;i++)
        {
            flag=0;
            for(j=0;j<cl;j++)
            {
                if(m[i][j]>0)
                    flag=1;
            }
            if(flag==0)
            {
                ord[k++]=i;
                cnt++;
            }
        }
        
        for(i=0;i<rl;i++)
        {
            for(j=0;j<k;j++)
            {
                if(ord[j]==i)
                    break;
            }
            if(j==k)
                ord[k++]=i;
        }
        
        BigInteger[] sum=new BigInteger[rl-cnt];
        BigInteger[][] r=new BigInteger[rl-cnt][cnt];
        BigInteger[][] rd=new BigInteger[rl-cnt][cnt];
        BigInteger[][] c=new BigInteger[rl-cnt][cl-cnt];
        BigInteger[][] f=new BigInteger[rl-cnt][cl-cnt];
        BigInteger[][] fi=new BigInteger[rl-cnt][cl-cnt];
        BigInteger[][] fid=new BigInteger[rl-cnt][cl-cnt];
        
        for(i=0;i<(rl-cnt);i++)
            sum[i]=BigInteger.ZERO;
        
        for(i=0;i<rl;i++)
        {
            for(j=0;j<cl;j++)
            {
                mn[i][j]=m[ord[i]][ord[j]];
                if(i>=cnt)
                    sum[i-cnt]=sum[i-cnt].add(BigInteger.valueOf(mn[i][j]));
                if(i>=cnt&&j<cnt)
                {
                    r[i-cnt][j]=BigInteger.valueOf(mn[i][j]);
                }
            }
        }
        
        BigInteger deno=sum[0];
        
        for(i=0;i<(rl-cnt);i++)
        {
            //System.out.print(sum[i]+" ");
            for(j=0;j<cnt;j++)
                rd[i][j]=sum[i];
            
            deno=(deno.multiply(sum[i])).divide(deno.gcd(sum[i]));
            //deno=(deno*sum[i])/gcd(deno,sum[i]);
        }
        
        for(i=cnt;i<rl;i++)
        {
            for(j=cnt;j<cl;j++)
            {
                c[i-cnt][j-cnt]=(BigInteger.valueOf(mn[i][j])).multiply(deno.divide(sum[i-cnt]));
                //c[i-cnt][j-cnt]=mn[i][j]*(deno/sum[i-cnt]);
                BigInteger value=BigInteger.ZERO;
                if(i==j)
                    value=BigInteger.ONE;
                f[i-cnt][j-cnt]=(value.multiply(deno)).subtract(c[i-cnt][j-cnt]);
                //System.out.print(f[i-cnt][j-cnt]+" ");
            }
        }
        //System.out.println(deno+" ");
        
        int slen=rl-cnt;
        
        adjoint(f,fi,slen);
        
        /*for(i=0;i<slen;i++)
            for(j=0;j<slen;j++)
                System.out.print(fi[i][j]+" ");*/
        
        BigInteger det=(determinant(f,slen,slen)).abs();
        //System.out.println(det+" ");
        
        BigInteger denopow=deno;
        /*for(i=1;i<slen;i++)
        {
            denopow=denopow.multiply(deno);
        }*/
        //System.out.println(denopow+" ");
        
        for(i=0;i<slen;i++)
        {
            for(j=0;j<slen;j++)
            {
                BigInteger g=det.gcd((fi[i][j].multiply(denopow)).abs());
                //System.out.print(denopow+" "+fi[i][j]+" ");
                fi[i][j]=(fi[i][j].multiply(denopow)).divide(g);
                fid[i][j]=det.divide(g);
                //System.out.println(det+"/"+g+"="+fid[i][j]+" ");
                //System.out.print(fi[i][j]+"/"+fid[i][j]+" ");
            }
        }
        
        BigInteger[][] mul=new BigInteger[slen][cnt];
        BigInteger[][] muld=new BigInteger[slen][cnt];
        
        for(i=0;i<slen;i++)
        {
            for(j=0;j<cnt;j++)
            {
                mul[i][j]=BigInteger.ZERO;
                BigInteger hcf=BigInteger.ONE;
                for(k=0;k<slen;k++)
                {
                    if(((fi[i][k].multiply(r[k][j])).compareTo(BigInteger.ZERO))!=0)
                        hcf=hcf.multiply((fid[i][k].multiply(rd[k][j])).divide(hcf.gcd(fid[i][k].multiply(rd[k][j]))));
                    mul[i][j]=mul[i][j].add((fi[i][k].multiply(r[k][j])).multiply(hcf.divide(fid[i][k].multiply(rd[k][j]))));
                }
                muld[i][j]=hcf;
            }
        }
        
        for(i=0;i<slen;i++)
        {
            for(j=0;j<cnt;j++)
            {
                BigInteger g=mul[i][j].gcd(muld[i][j]);
                mul[i][j]=mul[i][j].divide(g);
                muld[i][j]=muld[i][j].divide(g);
                //System.out.print(mul[i][j]+"/"+muld[i][j]+" ");
            }
        }
        
        int[] res=new int[cnt+1];
        
        BigInteger hcf=BigInteger.ONE;
        for(i=0;i<cnt;i++)
        {
            hcf=(hcf.multiply(muld[0][i])).divide(hcf.gcd(muld[0][i]));
        }
        for(i=0;i<cnt;i++)
        {
            mul[0][i]=mul[0][i].multiply(hcf.divide(muld[0][i]));
            res[i]=mul[0][i].intValue();
        }
        res[i]=hcf.intValue();
        
        return res;

        // Your code goes here.

    }
}
'''