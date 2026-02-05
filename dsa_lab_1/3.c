#include <stdio.h>

int main() {
    int a[10][10];
    int r, c;
    int i, j;
    int rowSum, colSum;

    printf("Enter number of rows: ");
    scanf("%d", &r);

    printf("Enter number of columns: ");
    scanf("%d", &c);

    printf("Enter matrix elements: ");
    for (i = 0; i < r; i++) {
        for (j = 0; j < c; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    
    for (i = 0; i < r; i++) {
        rowSum = 0;
        for (j = 0; j < c; j++) {
            rowSum = rowSum + a[i][j];
        }
        printf("Sum of row %d = %d\n", i + 1, rowSum);
    }

    
    for (j = 0; j < c; j++) {
        colSum = 0;
        for (i = 0; i < r; i++) {
            colSum = colSum + a[i][j];
        }
        printf("Sum of column %d = %d\n", j + 1, colSum);
    }

    return 0;
}
