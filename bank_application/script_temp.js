// var user_details={
//     1000:{"name":"arjun","password":"testone"},
//     1001:{"name":"ajay","password":"testtwo"},
//     1002:{"name":"arjun","password":"testthree"},
//     1003:{"name":"ajay","password":"testfour"},
// }
// function authenticate(accn,pwd){
//     if(accno in user_details){
//         if(pwd==user_details[accno]["password"]){
//             return 1
//         }
//         else{
//             return -1
//         }
//     }
//     else{
//         return 0
//     }
// }
// var form=document.getElementById('login-form')
// form.addEventListener('submit',function(e){
//     e.preventDefault()
//     accno=document.getElementById('acco').value
//     pwd=document.getElementById('pass').value
//     user=authenticate(accno,pwd)
//     if(user==1){
//         alert("login success")
//         window.location.href='home.html'
//     }
//     else if(user==-1){
//         console.log("incorrect password")
//         alert("incorrect password")
//     }
//     else{
//         console.log("invalid account number")
//         alert("invalid account number")
//     }

// })

var user_details=JSON.parse(window.localStorage.getItem('user_details'))

class Bank{
    static authenticate(accno,pwd){
        
        if(accno in user_details){
            if(pwd==user_details[accno]["password"]){
                return 1
            }
            else{
                return -1
            }
        }
        else{
            return 0
        }
    }
    static login(){
        var accno=document.querySelector('#acco').value
        var pwd=document.querySelector('#pass').value
        var user=Bank.authenticate(accno,pwd)
        if(user==1){
            alert("login success")
            var user_login={
                accountnumber:accno,
                password:pwd
            }
            window.localStorage.setItem('user',JSON.stringify(user_login))
            window.location.href="home.html"
        }
        else if(user==-1){
            console.log("incorrect password")
            alert("incorrect password")
        }
        else{
            console.log("invalid account number")
            alert("invalid account number")
        }
    }
    static transaction(clicked_object){
        var login_details=JSON.parse(window.localStorage.getItem('user'))
        var accno=login_details['accountnumber']
        var pwd=login_details['password']
        var user = Bank.authenticate(accno,pwd)
        if(user==1){
            var amount=document.getElementById('amount').value
            if(amount!=''){
                if(clicked_object.getAttribute('action')=='deposit'){
                    user_details[accno]['balance']+=parseInt(amount)
                    alert("Deposited! Your balance is"+user_details[accno]['balance'])
                    window.localStorage.setItem('user_details',JSON.stringify(user_details))
                }
                else{
                    if(user_details[accno]['balance']>=amount){
                        user_details[accno]['balance']-=amount
                        alert("Withdrawn! Your balance is"+user_details[accno]['balance'])
                        window.localStorage.setItem('user_details',JSON.stringify(user_details))
                    }
                    else{
                        alert("Transaction Failed, Insufficient balance")
                    }
                }
            }
        }
        else if(user==-1){
            alert('incorrect password.')
        }
        else{
            alert('invalid account number')
        }
    }
    static logout(){
        window.localStorage.removeItem('user')
        window.location.href="login.html"
    }
}

