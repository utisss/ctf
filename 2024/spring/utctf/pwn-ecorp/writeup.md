pnw-ecorp
@aadhi0319

There POC exploit is included in exploit.py. Essentially, this is a stack overflow with due to incorrect sanitization of web requests. You did not need to do any rop based cache flushing since qemu does not emulate cache coherency (I think).

My Talk on Exploiting this Router (which was up during the duration of the CTF):
https://www.youtube.com/watch?v=Ai5TlzaOFUE

CVE:
https://blog.viettelcybersecurity.com/tp-link-tl-wr940n-httpd-httprpmfs-stack-based-buffer-overflow-remote-code-execution-vulnerability/
