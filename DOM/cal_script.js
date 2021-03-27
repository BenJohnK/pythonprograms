var num1=""
var num2=""
var symbol=""
var activer=""
var current_text=""
// document.getElementById('computation').textContent='10.2'
// var computation=parseFloat(document.getElementById('computation').innerHTML)
// alert(computation)
// alert(typeof(computation))
var buttons_list=document.getElementsByClassName('digit')
for(let item of buttons_list){
    item.addEventListener('click',function(){
        if(current_text==""){
            document.getElementById('computation').innerHTML='&nbsp'
        }
        button_val=this.getAttribute('value')
        if(current_text.indexOf('x')>-1||current_text.indexOf('+')>-1||current_text.indexOf('-')>-1||current_text.indexOf('/')>-1){
            activer="num2"
        }
        else{
            activer="num1"
        }
        current_text+=button_val
        if(button_val=='x'||button_val=='+'||button_val=='-'||button_val=='/'){
            if(activer=='num1'&&num1!=""){
                symbol=button_val
                document.getElementById('computation').innerHTML=num1+symbol
                document.getElementById('entry-result').innerHTML=''
            }
        }
        else if(button_val=='='){
            // alert('clicked')
            var res=0;
            num1_cleaned=parseFloat(num1)
            num2_cleaned=parseFloat(num2)
            if(symbol=='x'){
                res=num1_cleaned*num2_cleaned
            }
            else if(symbol=='-'){
                res=num1_cleaned-num2_cleaned
            }
            else if(symbol=='+'){
                res=num1_cleaned+num2_cleaned
            }
            else if(symbol=='/'){
                if(num2_cleaned==0){
                    res='infinity'
                }
                else{
                    res=num1_cleaned/num2_cleaned
                }
            }
            document.getElementById('entry-result').innerHTML=res
            num1=""
            num2=""
            symbol=""
            activer=""
            current_text=""
        }
        else{
            if(activer=='num1'){
                num1+=button_val
                document.getElementById('entry-result').innerHTML=num1
            }
            if(activer=='num2'){
                num2+=button_val
                document.getElementById('entry-result').innerHTML=num2
                document.getElementById('computation').innerHTML=current_text
            }
        }
            
    })
}

