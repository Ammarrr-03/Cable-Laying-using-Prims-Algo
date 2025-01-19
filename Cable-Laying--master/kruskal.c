#include<stdio.h>
#include<time.h>
#define MAX 20

int i,j,a,b,u,v,n,ne=1; // "n=no_of_company
int min,mincost=0,cost[MAX][MAX],parent[MAX]={-1};// parent array is for mark the visited nodes
int find(int);
int uni(int,int);

void main()
{
	printf("\nEnter the number of companies:");
	scanf("%d",&n);

	printf("\nEnter the distance between them:\n");
	for(i=1;i<=n;i++) // this loop is for taking input 
	{
		for(j=1;j<=n;j++)
		{
			scanf("%d",&cost[i][j]);
			if(cost[i][j]==0)
				cost[i][j]=999;
		}
	}
      
    clock_t begin = clock(); // this function is use to measure the execution time 
    printf("\n");

	while(ne<n) // ne is less n because no of edges is one less than no of vertices
	{
	min=999;
		for(i=1;i<=n;i++) //this loop is for finding the minimum edge from the matrix 
		{
			for(j=1;j <=n;j++)
			{
				if(cost[i][j] < min)
				{
					min=cost[i][j];
					a=u=i;
					b=v=j;
				}
			}
		}
		u=find(u);  
		v=find(v);
		if(uni(u,v))
		{
			printf("\n%d Connection (%d,%d) distance =%d\n",ne++,a,b,min);
			mincost +=min;
		}
		cost[a][b]=cost[b][a]=999;
	}
	printf("\nMinimum cost for laying a cable = %d\n",mincost);

	clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("\ntime taken=%f\n", time_spent);
}
int find(int i) // find() function is used to find the parent u , v
{
	while(parent[i])
	i=parent[i];
	return i;
}
int uni(int i,int j) // union() fuction is used for checking both the u and v have same
{                     //parent to avoid loop.
	if(i!=j)
	{
		parent[j]=i;
		return 1;
	}
	return 0;
    
}