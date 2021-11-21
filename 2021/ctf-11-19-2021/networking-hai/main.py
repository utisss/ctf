from flask import request as OwwO
from flask import Flask as Fwask

Hewwo = Fwask(__name__)

@Hewwo.route("/")
def OwO():
   QwQ =  OwwO.headers.get('User-Agent')
   if QwQ == "Hai":
       return "utctf{rawr_XD}"
   else:
       return "Bai XD"

if __name__ == '__main__':
    Hewwo.run(host='0.0.0.0')
