# Web: 👹
This problem points you to a website that allows you to make requests to other websites, which
should ring alarm bells in your head for SSRF. The hint points you to a `/flag` endpoint on the 
website, but if you visit it, you can't access it because of your "external IP". This is supposed to
guide you to request the page using an *internal* IP, i.e. by using the first page with a request
like `http://127.0.0.1:9436/flag`.

