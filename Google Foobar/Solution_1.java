package com.google.challenges; 

public class Answer {   
    public static int answer(int total_lambs) 
	{ 
		int i,c=0,l=s.length();
        for(i=1;i<=l;i++)
        {
            if(l%i!=0)
                continue;
            String sb=s.substring(0,i);
            int index=s.indexOf(sb);
            c=0;
            while(index>=0)
            {
                index=s.indexOf(sb,index+1);
                c++;
            }
            if(l/i==c)
                break;
        }
        return c;
		
        // Your code goes here.

    } 
}
