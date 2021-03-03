#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>


int main(int argc, char **argv)
{
  int pipe1[2], pipe2[2];
  int process_id;

  char *wc_args[] = {"wc", NULL};
  char *grep_args[] = {"grep", "--binary-files=text", "-i", "hai",  NULL};

  pipe(pipe1);
  pipe(pipe2);

  process_id = fork();

  if (process_id < 0)
    perror("Fork failed!");
  else if (process_id > 0)
  {
    char m;
    close(pipe1[0]);
    close(pipe2[1]);

    dup2(pipe2[0], 0);
    close(pipe2[0]);

    FILE *f1 = fopen("files.txt", "r");
    while ((m = fgetc(f1)) != EOF)
      write(pipe1[1], &m, 1);
    close(pipe1[1]);

    wait(NULL);

    execvp(*wc_args, wc_args);
  }
  else
  {
    close(pipe1[1]);
    close(pipe2[0]);

    dup2(pipe1[0], 0);
    dup2(pipe2[1], 1);

    close(pipe1[0]);
    close(pipe2[1]);

    execvp(*grep_args, grep_args);
  }
}


