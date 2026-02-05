#include <stdio.h>
#include <string.h>

int main() {
char s[100];

printf("Enter uppercase string :\n");
scanf("%s", s);

for (int i = 0; i < strlen(s); i++) {
if (s[i] >= 'A' && s[i] <= 'Z') {
s[i] = s[i] + 32;
}
}

printf("Lowercase string : %s", s);

return 0;
}