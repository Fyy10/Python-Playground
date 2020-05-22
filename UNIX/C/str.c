#include <stdio.h>

static char buff[256];
static char *string;

int main(int argc, char *argv[])
{
    printf("please input a string:\n");
    string = fgets(buff, 255, stdin);
    // gets(string);
    printf("your string is: %s\n", string);
    return 0;
}
