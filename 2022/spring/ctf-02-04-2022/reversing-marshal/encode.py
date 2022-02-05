import marshal
import zlib
import base64

actual_flag = list(b"utflag{this_problem_would_have_been_easier_to_write_if_coffee_beans_were_actual_beans}")
def encode():
    global actual_flag
    for i in range(1, len(actual_flag)):
        actual_flag[i] = actual_flag[i] ^ actual_flag[i-1]
    actual_flag = base64.b64encode(bytes(actual_flag)[::-1])
    return actual_flag

def check_flag(flag):
    import base64
    encoded_flag = b'LVAjTSxJK3QYeQx4G3olQDJXIH8MYgNmBFs+Wz1bNFcIbgdYPUkgUiV6FWE+TClAM1I3aAZjBmQ7XihJIX4adgNsG0QpTCBCLV8vcANqAnYNagtnAXU='
    working_flag = list(flag)
    for i in range(1, len(working_flag)):
        working_flag[i] = working_flag[i] ^ working_flag[i-1]
    working_flag = base64.b64encode(bytes(working_flag)[::-1])
    return working_flag == encoded_flag

print(encode())
print(base64.b64encode(zlib.compress(marshal.dumps(check_flag.__code__))))
