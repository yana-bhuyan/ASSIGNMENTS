#include <stdio.h>

int main() {
    int arr[20];
    int n, i, j, value;
    int k;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter array elements:\n");
    for (k = 0; k < n; k++) {
        scanf("%d", &arr[k]);
    }

    
    printf("Enter position to insert (i): ");
    scanf("%d", &i);

    printf("Enter element to insert: ");
    scanf("%d", &value);

    for (k = n; k >= i; k--) {
        arr[k] = arr[k - 1];
    }
    arr[i - 1] = value;
    n++;

    
    printf("Enter position to delete (j): ");
    scanf("%d", &j);

    for (k = j - 1; k < n - 1; k++) {
        arr[k] = arr[k + 1];
    }
    n--;

    printf("Final array:\n");
    for (k = 0; k < n; k++) {
        printf("%d ", arr[k]);
    }

    return 0;
}
