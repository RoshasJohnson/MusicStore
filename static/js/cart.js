// var updatebtn = document.getElementsByClassName('update-cart')
// console.log(updatebtn)
// for (var i = 0; i <updatebtn.length; i++){  
//     updatebtn[i].addEventListener("click",function(){
//         var productId = this.dataset.product
//         var action = this.dataset.action
//         console.log('i.Id:',productId,'action:',action)
//         // console.log('user:',user)
//         updateuserOrder(productId,action)   
//     })
// }

// function updateuserOrder(productId,action){
//     console.log('user in logged in ,sending data....')
//     var url = '/update_item/'
//     fetch(url,{
//       method:'POST',
//       headers:{'content-Type':'application/json',
//       'X-CSRFToken':csrftoken,
//     },
//     body:JSON.stringify({'productId':productId,'action':action})

//     })
//     .then((response)=>{
//       return response.json()
//     })
//     .then((data)=>{
//       console.log('data',data)
//     })
    

// }
