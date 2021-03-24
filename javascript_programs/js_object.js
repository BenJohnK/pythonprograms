var text="bababac"
var obj={}
letters=text.split("")
for(let letter of letters){
    if(letter in obj){
        obj[letter]+=1
        console.log("first recursive character is "+letter)
        break
    }
    else{
        obj[letter]=1
    }
}