function sendData(data, endpoint) {
    const XHR = new XMLHttpRequest();

    // Define what happens on successful data submission
    XHR.addEventListener('load', function (event) {
        if (event.target.status === 200) {
            window.location.href = 'flag.html';
        } else {
            alert('Oops! The server has rejected you.');
        }
    });

    // Define what happens in case of error
    XHR.addEventListener('error', function (event) {
        alert('Oops! Something went wrong.');
    });

    XHR.open('POST', `/api/v1/${endpoint}`);
    XHR.setRequestHeader('Content-Type', 'application/json');
    XHR.send(JSON.stringify(data));
}

function get(endpoint, okAction) {
    const XHR = new XMLHttpRequest();

    // Define what happens on successful data submission
    XHR.addEventListener('load', function (event) {
        if (event.target.status === 200) {
            okAction(event.target.response);
        } else {
            alert('Oops! The server has rejected you.');
        }
    });

    // Define what happens in case of error
    XHR.addEventListener('error', function (event) {
        alert('Oops! Something went wrong.');
    });

    XHR.open('GET', `/api/v1/${endpoint}`);
    XHR.send();
}
