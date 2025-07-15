/*
    A A A A
    A A A
    A A
    A
*/
#include<stdio.h>
void main()
{
    int n,i,j;
    char x='A';
    printf("Enter the range : ");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(j=i;j<=n;j++)
        {
            printf("%c ",x);
        }
        printf("\n");
    }
}