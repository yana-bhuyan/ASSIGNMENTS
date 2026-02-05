#include <stdio.h>

int main() {
int n;
printf("Enter number of elements: ");
scanf("%d", &n);

int arr[100];
printf("Enter elements:\n");
for (int i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}

int key;
printf("Enter number to search: ");
scanf("%d", &key);

int found = 0;
for (int i = 0; i < n; i++) {
if (arr[i] == key) {
found = 1;
printf("Number found at position %d", i + 1);
break;
}
}

if (found == 0) {
printf("Number not found in the array");
}

return 0;
}