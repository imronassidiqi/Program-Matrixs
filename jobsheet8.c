#include <stdio.h>
#include <stdlib.h>

int A[4][4],i,j;

int main(int argc, char *argv[])
{
 for(i=0;j=i<2;i++)
 {
  for(j=0;j<2;j++)
  {
     printf("Input Matriks A[%d][%d]: ",i+1,j+1);
     scanf("%d",&A[i][j]);
  }
 }

 for(i=0;i<2;i++)

 {
  for(j=0;j<2;j++)
  {
     printf("%4d",A[i][j]);
  }
  printf("\n");
 }
 return 0;
}
