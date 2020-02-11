1. Upon examining the device, you realize that it is a TM4C Cortex-M4 microcontroller w/
    3 input buttons
2. You’re given a copy of the firmware with the flag redacted.
3. Using this copy of the firmware, you figure out that you need to get past various
    conditionals (that are dependent on the buttons (MMIO)) to have the device print the flag
4. From here, you create a list of the buttons that you need to press in the proper order.
5. If you get the sequence right, the flag prints
**Correct sequence SW2 -> PE0 (aux button) -> SW2 ->SW1 -> SW
utflag{push_mY_butt0ns}**
