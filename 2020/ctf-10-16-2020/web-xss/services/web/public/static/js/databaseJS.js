document.querySelectorAll('.databaseForm').forEach(item => {
    item.addEventListener("submit", function(e) {
        document.getElementById("databaseResult").innerHTML = "Please wait for an admin to review your feedback..."
        querydb(this.getAttribute("method"), this.getAttribute("action"), new FormData(this));
        e.preventDefault();
    });
});
function querydb(method, path, data) {

    const retry = (tries) => tries == 0
        ? null
        : fetch(
            path + btoa(data.get('feedback')),
            {
                method,
                headers: { 'Content-Type': 'application/x-www-form-urlencoded'},
            }
          )
            .then(res => res.status == 200
                ? res.text().then(t => t)
                : "Some error occured"
            )
            .then(res => document.getElementById("databaseResult").innerHTML = res)
            .catch(e => retry(tries - 1));

    retry(1);
}

function payload(data) {
    var formdata = ""; 
    for(var pair of data.entries()) {
        formdata += pair[0] + "=" + pair[1] + "&";
    }
    return formdata;
}
