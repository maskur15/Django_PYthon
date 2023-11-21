var updateBtns = document.getElementsByClassName('update-cart')
for(i=0;i<updateBtns.length;i++)
{
    updateBtns[i].addEventListener('click',function()
    {
        
        var prodcutId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',prodcutId,' Action: ',action)
        console.log('USER',user)
        if(user=='AnonymousUser'){
            console.log('User is not authenticated')
        }
        else{
            updateUserOrder(prodcutId,action)
        }
    })
}
function updateUserOrder(productId,action){

    console.log('user is authenticated . sending data')
    var url = '/updateitem/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken, // Include the CSRF token in the headers

        },
        body:JSON.stringify({'productId':productId,'action':action})
    }).then((response)=>{
        return response.json();
    })
    .then((data)=>{
        console.log('Data',data)
        location.reload()
    });


}
