#include "stdio.h"

int main()
{
    int n, i, ans = 1;
    printf("Please input a numebr: ");
    scanf("%d", &n);
    if (n < 0) printf("Wrong number!\n");
    else
    {
        for (i = 1; i <= n; i++) ans *= i;
        printf("n!=%d\n", ans);
    }
    return 0;
}
