var updatebtn = document.getElementsByClassName('option1')
console.log(updatebtn.value)
console.log('hello')


for (var i = 0; i <updatebtn.length; i++){  
    updatebtn[i].addEventlistener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('i.Id:',productId,'action:',action)
    })
}   