unshadow passwd shadow > unshadowed.txt
john unshadowed.txt
john --show unshadowed.txt
rm unshadowed.txt
