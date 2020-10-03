const authenticateBtn = document.getElementById('authenticate-btn');
const registerBtn = document.getElementById('register-btn');

const usernameInput = document.getElementById('username-input');
const passwordInput = document.getElementById('password-input');

function validate() {
    return !(usernameInput.value === "" || passwordInput.value === "");
}

authenticateBtn.addEventListener(
    'click',
    () => {
        if (!validate()) {
            return;
        }

        sendData( {username: `${usernameInput.value}`, password: `${passwordInput.value}`}, 'authenticate')
    }
)

registerBtn.addEventListener(
    'click',
    () => {
        if (!validate()) {
            return;
        }

        sendData( {username: `${usernameInput.value}`, password: `${passwordInput.value}`}, 'register')
    }
)
