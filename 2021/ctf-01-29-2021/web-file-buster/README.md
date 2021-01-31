# File-Buster
* **Event:** robopocalypseCTF
* **Problem Type:** Web
* **Point Value / Difficulty:** Easy (200)

## Walkthrough
A tool used to brute-force: URIs (directories and files) in web sites is good for this one. Dirbuster and Gobuster are both popular, but i prefer the former. for dirbuster you type in the target url, select a wordlist to use for brute force directories and files, directory-list-lowercase-2.3-small.txt is good to start with, you can also specify file types to search for. Here we'd be looking for .txt. Dirbuster searches directories recursively so you can just wait till it finds the file you are looking for. Once it does find it you can click the result and go straight to the location.

## Flag
'utflag{Bust3d_b33p_b00p}'
