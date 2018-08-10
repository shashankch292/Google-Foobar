package com.google.challenges; 
import java.util.ArrayDeque;
import java.util.Queue;

public class Answer {
    
    static int[] rown={-1,0,0,1};
    static int[] coln={0,-1,1,0};
    
    static class point
    {
        public point(int r,int c)
        {
            this.x=r;
            this.y=c;
        }
        int x,y;
    }
    
    static class Qnode
    {
        public Qnode(point s,int d)
        {
            this.pt=s;
            this.dist=d;
        }
        point pt;
        int dist;
    }
    
    static int Shortest_path(int[][] maze,int row,int col)
    {
        point src=new point(0,0);
        point dest=new point(row-1,col-1);
        
        boolean[][] vst=new boolean[row][col];
        vst[src.x][src.y]=true;
        
        Queue<Qnode> q=new ArrayDeque<Qnode>();
        
        Qnode s=new Qnode(src,0);
        q.add(s);
        
        while(!q.isEmpty())
        {
            Qnode cr=q.peek();
            point pt=cr.pt;
            
            if(pt.x==dest.x&&pt.y==dest.y)
                return cr.dist;
                
            q.poll();
            
            for(int i=0;i<4;i++)
            {
                int r=pt.x+rown[i];
                int c=pt.y+coln[i];
                
                if(((r>=0)&&(r<row)&&(c>=0)&&(c<col))&&maze[r][c]==0&&!vst[r][c])
                {
                    vst[r][c]=true;
                    Qnode ad=new Qnode(new point(r,c),cr.dist+1);
                    q.add(ad);
                }
            }
        }
        return -1;
    }
    
    public static int answer(int[][] maze) 
    {
        int row=maze.length;
        int col=maze[0].length;
        int min=10000;
        int k=Shortest_path(maze,row,col);
        if(k>0)
            min=k;
        int i,j;
        for(i=0;i<row;i++)
        {
            for(j=0;j<col;j++)
            {
                if(maze[i][j]==1)
                {
                    maze[i][j]=0;
                    k=Shortest_path(maze,row,col);
                    maze[i][j]=1;
                    if(k<min&&k>0)
                        min=k;
                }
            }
        }
        
        return min+1;

        // Your code goes here.

    } 
}
