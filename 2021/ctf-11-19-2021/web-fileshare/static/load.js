ul = document.querySelector(".files");
id = new URLSearchParams(window.location.search).get("id")
fetch("/api/dir/" + id).then(response => response.json()).then(data => renderDir(data));

function renderDir(response) {
	for (let i of response["entries"]) {
		if (i["dir"]) {
			fetch("/api/dir/" + i["id"]).then(response => response.json()).then(data => appendDir(data));
		} else {
			fetch("/api/file/" + i["id"]).then(response => response.json()).then(data => appendFile(data));
		}
	}
}

function appendFile(response) {
	a = document.createElement("a");
	a.href = "/api/download/" + response["id"];
	a.innerText = response["filename"];
	li = document.createElement("li");
	li.appendChild(a);
	ul.appendChild(li);
}

function appendDir(response) {
	a = document.createElement("a");
	a.href = "/?id=" + response["id"];
	a.innerText = response["filename"] + "/";
	li = document.createElement("li");
	li.appendChild(a);
	ul.appendChild(li);
}
