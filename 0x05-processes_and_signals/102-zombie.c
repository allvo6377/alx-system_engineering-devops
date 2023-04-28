#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * main - creates 5 zombie processes
 *
 * Return: always 0
 */
int main(void)
{
    pid_t pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        pid = fork();
        if (pid > 0)
        {
            printf("Zombie process created, PID: %d\n", pid);
            sleep(1);
        }
        else
            exit(0);
    }

    /* Keep the parent process running */
    while (1)
        sleep(1);

    return (0);
}

