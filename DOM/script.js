var htwo_elements=document.getElementsByTagName('h2')
for(let item of htwo_elements){
    item.style.color="red"
}
var list_elements=document.getElementsByClassName('com')
for(let item of list_elements){
    item.style.color='blue'
    // item.innerHTML='text changed'
}
var single_list_element=document.getElementById('ids');
single_list_element.style.color="cyan"
console.log(typeof(single_list_element))
var head=document.head
console.log(typeof(head))
function res(){
    alert('hi')
    var r=document.getElementById('input-field').value
    result=eval(r)
    alert(result)
}
