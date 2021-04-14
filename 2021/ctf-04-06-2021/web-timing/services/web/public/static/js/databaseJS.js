document.querySelectorAll('.databaseForm').forEach(item => {
    item.addEventListener("submit", function(e) {
        document.getElementById("databaseResult").innerHTML = "Logging in..."
        querydb(this.getAttribute("method"), this.getAttribute("action"), new FormData(this));
        e.preventDefault();
    });
});
function querydb(method, path, data) {

    const password = data.get('password');

    const retry = (tries) => tries == 0
        ? null
        : fetch(
            path + password,
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