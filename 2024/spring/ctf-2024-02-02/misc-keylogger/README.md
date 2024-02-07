# Miscellaneous - Keylogger
### @aadhi0319

You notice that you have a pcap file, so you should first open it in Wireshark to get more information. It immediately becomes clear that this is not a normal pcap file as there is no internet traffic. Instead, you see many USB interrupts. This hints that this is a USB device capture. The USB interrupts in particular suggest that a USB keyboard is attached. We can then attempt to decode these events to determine what was typed.

A quick google search should reveal that the filter `(usb.transfer_type == 0x01 && usb.data_len == 8) && !(usbhid.data == 00:00:00:00:00:00:00:00)` extracts all the keypress events. We select all these packets and click `File -> Export specified packets` to export these packets to another pcap file called `keypress.pcapng`.

`tshark -r ./keypress.pcapng -Y 'usb.capdata' -T fields -e usb.capdata | awk '{print substr($1,3,18)}' | sed 's/../:&/g2' > usbPcapData`

You should now get a usbPcapData file that looks like this:
```
00:18:00:00:00:00:00
00:17:00:00:00:00:00
00:09:00:00:00:00:00
00:0f:00:00:00:00:00
00:04:00:00:00:00:00
00:0a:00:00:00:00:00
00:00:00:00:00:00:00
00:2f:00:00:00:00:00
00:00:00:00:00:00:00
00:0c:00:00:00:00:00
00:00:00:00:00:00:00
00:2d:00:00:00:00:00
00:00:00:00:00:00:00
00:0e:00:00:00:00:00
00:11:00:00:00:00:00
00:12:00:00:00:00:00
00:1a:00:00:00:00:00
00:00:00:00:00:00:00
00:2d:00:00:00:00:00
00:00:00:00:00:00:00
00:04:00:00:00:00:00
00:0f:00:00:00:00:00
00:0f:00:00:00:00:00
00:00:00:00:00:00:00
00:2d:00:00:00:00:00
00:00:00:00:00:00:00
00:17:00:00:00:00:00
00:0b:00:00:00:00:00
00:08:00:00:00:00:00
00:00:00:00:00:00:00
00:2d:00:00:00:00:00
00:00:00:00:00:00:00
00:16:00:00:00:00:00
00:08:00:00:00:00:00
00:06:00:00:00:00:00
00:15:00:00:00:00:00
00:08:00:00:00:00:00
00:17:00:00:00:00:00
00:17:16:00:00:00:00
00:16:00:00:00:00:00
00:00:00:00:00:00:00
00:30:00:00:00:00:00
00:00:00:00:00:00:00
```

Pair the second byte in this list with the table on page 53 of the [USB HID documentation](https://usb.org/sites/default/files/documents/hut1_12v2.pdf). Note that the second byte represents the code. Also, by knowing the utflag flag format and looking at the capture, you can discern that `00:00:00:00:00:00:00:00` toggles shift. Pairing all this information together, you can discern the flag as being `utflag{i_know_all_the_secretts}`. If you're wondering, yes I did mispell secrets when capturing the pcap file.
