var login_details=JSON.parse(window.localStorage.getItem('user'))
if(login_details==null){
    window.location.href="login.html"
}
var accountnumber=login_details['accountnumber']
document.getElementById('hello').innerHTML='hello '+user_details[accountnumber]['name']