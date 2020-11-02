#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <seccomp.h> /* libseccomp */

static int install_syscall_filter(void)
{
    // Init the filter
    scmp_filter_ctx ctx;
    ctx = seccomp_init(SCMP_ACT_KILL); // default action: kill

    // setup basic whitelist
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(rt_sigreturn), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit_group), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(openat), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(fstat), 0);

    seccomp_load(ctx);
}


int main() {
  printf("Things are about to get spooky!\n");
  install_syscall_filter();
  printf("I've disabled all syscalls except file operations and exit!\n");
  printf("I'll let your overflow a buffer. You can't call exec anyway lol\n");
  printf("I've hidden the flag at /home/seccomp/flag.txt\n");
  char buffer[100];
  gets(buffer);
  return 1;
}

// Add some useful gadgets and force functions into PLT
void func() {
    // This will crash
    asm("pop %rdx; ret");
    open(0,0);
    read(0,0,0);
    write(0,0,0);
}
