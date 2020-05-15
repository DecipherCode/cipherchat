document.addEventListener('DOMContentLoaded',function(){
    //request_usernames()
    if (screen.width<950){
        document.querySelector(".left").innerHTML+="<br style:'color:white'><p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;already a member? Scroll Down. </p>";}
})


function vanishL() {
    let element = document.getElementById("elementtofadeL")
    const template= Handlebars.compile(document.querySelector('#left').innerHTML);
    const content = template({});
    element.style.animationPlayState = 'running';
    setTimeout(() =>  {
      element.innerHTML = content;},350);
    }
function vanishR() {
    let element = document.getElementById("elementtofadeR")
    const template= Handlebars.compile(document.querySelector('#right').innerHTML);
    const content = template({});
    element.style.animationPlayState = 'running';
    setTimeout(() =>  {
        element.innerHTML = content;},350);
    }

function validate() {
    flag = false;
    var NAME =  document.getElementById('Name');
    var UNAME = document.getElementById('username');
    var PASS = document.getElementById('password');
    if(NAME.value.length>30){
        alert("Please provide a name shorter than 30 characters!");
        return flag;
        }
    if(UNAME.value.length<5) {
        alert("Please provide a username longer than 5 characters!");
        return flag;
        }
    if(UNAME.value.length>20) {
        alert("Please provide a username shorter than 20 characters!");
        return flag;
        }
    if(UNAME.value.length>20) {
        alert("Please provide a username shorter than 20 characters!");
        return flag;
        }
    if(PASS.value.length<8) {
        alert("Please ensure your password is longer than 8 characters!");
        return flag;
        }
   if(PASS.value.length>20) {
        alert("Please ensure your password is shorter than 20 characters!");
        return flag;
       }
    flag = true;
    alert("SUCCESS");    
    return(flag); 
  }
