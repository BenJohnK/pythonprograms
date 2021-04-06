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
class Bank{
    static getUserDetails(accno=0,balance=0){
        var user_details={
            1000:{"name":"arjun","password":"testone","balance":3000},
            1001:{"name":"ajay","password":"testtwo","balance":3000},
            1002:{"name":"arjun","password":"testthree","balance":3000},
            1003:{"name":"ajay","password":"testfour","balance":3000},
        }
        if(accno==0&&balance==0){
            return user_details
        }
        alert('hey')
        user_details[accno]['balance']=balance 
        alert(user_details[accno]['balance'])       
    }
    static authenticate(accno,pwd){
        var user_details=Bank.getUserDetails()
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
        var accno=document.querySelector('#acco').value
        var pwd=document.querySelector('#pass').value
        var user = Bank.authenticate(accno,pwd)
        if(user==1){
            var amount=document.getElementById('amount').value
            var user_details=Bank.user_details
            if(clicked_object.getAttribute('action')=='deposit'){
                user_details[accno]['balance']+=parseInt(amount)
                alert("Deposited! Your balance is"+user_details[accno]['balance'])
                Bank.getUserDetails(accno,user_details[accno]['balance'])
            }
            else{
                if(user_details[accno]['balance']>=amount){
                    user_details[accno]['balance']-=amount
                    alert("Withdrawn! Your balance is"+user_details[accno]['balance'])
                    Bank.getUserDetails(accno,user_details[accno]['balance'])
                }
                else{
                    alert("Transaction Failed, Insufficient balance")
                }
            }
        }
    }
}

