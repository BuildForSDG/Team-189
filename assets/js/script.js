let password = document.getElementById('password');
let confirmPassword = document.getElementById('confirm_password');

const checkPassword = (password, confirmPassword) => {
    if(password.value === confirmPassword.value) {
        alert("Passwords match. :)");
        confirmPassword.style.backgroundColor = "#66cc66";
    } else if (password.value != confirmPassword.value) {
        alert("Passwords don't match.");
        confirmPassword.style.backgroundColor = "#ff6666";
    }

}