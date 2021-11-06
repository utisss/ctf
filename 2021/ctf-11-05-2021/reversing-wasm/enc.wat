(module
    (func $encrypt
        (param $a i32)
        (param $b i32)
        (result i32)

        (get_local $a)
        (get_local $b)
        (i32.mul)
        (i32.const 3389592)
        (i32.add)
    )

    (export "encrypt" (func $encrypt))
)