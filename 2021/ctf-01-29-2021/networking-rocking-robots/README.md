# Rocking Robots
* **Event:** robopocalypseCTF
* **Problem Type:** Networking
* **Point Value / Difficulty:** Hard
* **(Optional) Tools Required / Used:** Wireshark, John the Ripper

## How To Solve
#### Step 1
Notice the capture file contains a WPA2 handshake (filter by `eapol` ub Wireshark).

Unzip the capture file and use John the Ripper to crack the password. Extract the necessary information for John to do its work and output it to the `crackme` file. Hashcat is a good alternative to John. There are other utilities for working with Hashcat.
```shell
gzip -kd capture.pcap.gz
wpapcap2john capture.pcap > crackme
```

The title is a hint to use the rockyou password list.

Normally, you can run (assuming the dictionary file is at `rockyou.txt`:
```shell
john -w=rockyou.txt -form=wpapsk crackme
```

If you want to use OpenCL, use the following:
```shell
john -w=rockyou.txt -form=wpapsk-opencl crackme
```

```shell
john --show crackme
```
The password is `janeimeelyzza`.


#### Step 2
Open the capture file in Wireshark. From the `wireless toolbar` (might have to be enabled in the `view` menu tab) select `802.11 Preferences`. In the settings for `IEEE 802.11 wireless LAN`, enable decryption and edit the decryption keys. Add a new key of the type `wpa-pwd` and use `janeimeelyzza` as the password. The capture should now be decrypted.


#### Step 3
Observe that there is a broadcasted UDP packet that contains the flag as a string in the data.
