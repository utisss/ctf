const flagSpan = document.getElementById('flag-span');

const okAction = (flag) => {
    flagSpan.innerText = flag;
};

get('get_flag', okAction);
