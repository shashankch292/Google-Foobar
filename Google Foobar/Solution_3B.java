package com.google.challenges; 

public class Answer {   
    public static int answer(int[] l) 
	{ 
		int i,j,res=0,len=l.length;
		int[] d=new int[len];

		for(i=1;i<len;i++)
		{
			for(j=0;j<i;j++)
			{
				if(l[i]%l[j]==0)
					d[i]++;
			}
		}

		for(i=2;i<len;i++)
		{
			for(j=1;j<i;j++)
			{
				if(l[i]%l[j]==0)
					res+=d[j];
			}
		}

		return res;
		
        // Your code goes here.

    } 
}
