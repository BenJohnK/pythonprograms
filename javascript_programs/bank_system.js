class Bank{
    constructor(accno,p_name,bal){
        this.accno=accno;
        this.p_name=p_name;
        this.bal=bal;
    }

    deposit(amount){
        this.bal=this.bal+amount;
        console.log("amount inserted!")
        console.log("Remaining Balance:"+this.bal)
    }
    withdraw(amount){
        if(this.bal<amount){
            console.log("Insufficient Funds")
        }
        else{
            this.bal=this.bal-amount;
            console.log("Remaining balance:"+this.bal)
        }
    }
}
var p1=new Bank(100,"ben",3000);
p1.withdraw(3000)
