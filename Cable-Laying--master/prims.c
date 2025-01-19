#include<stdio.h>
#include<time.h>
#define MAX 20

int a,b,u,v,n,i,j,ne=1; // n: no. of nodes // ne: for iteration in while
int visited[MAX]={0},min,mincost=0,cost[MAX][MAX]; //visited array is for marking the visited node 

void main()
{	
    printf("\nEnter the number of companies:");	
    scanf("%d",&n);	

    printf("\nEnter the distance between them:\n");	
        for (i=1;i<=n;i++)	  
            for (j=1;j<=n;j++) 
            {		
                scanf("%d",&cost[i][j]);		
                if(cost[i][j]==0)		    
                cost[i][j]=999;	
            }	

    visited[1]=1;	
    clock_t begin = clock();
    printf("\n");

    while(ne<n)
    {	
      min=999;	
      for (i=1;i<=n;i++) // this loop is checking the minimum value of the adjacent 
      { 
        for (j=1;j<=n;j++) // edge from selected node
        {		    
          if(cost[i][j]<min)		     
            if(visited[i]!=0)
                {			
                    min=cost[i][j];			
                    a=u=i;			
                    b=v=j;		
                }
        }
      }   		
        if(visited[u]==0 || visited[v]==0) // this is used for checking the cycle in graph
            {			
                printf("\nConnection %d-%d distance:%d\n",a,b,min);
                ne++;
                mincost+=min;			
                visited[b]=1; 		
            }		
        cost[a][b]=cost[b][a]=999;	
    }	

    printf("\nMinimun cost for laying a cable=%d\n",mincost);

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("\ntime taken=%f\n", time_spent);
}