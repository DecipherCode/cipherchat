document.addEventListener('DOMContentLoaded',function(){
    if (screen.width<950)
        document.querySelector(".left").innerHTML+="<br style:'color:white'><p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;already a member? Scroll Down. </p>";
})


function vanishL() {
    let element = document.getElementById("elementtofadeL")
    const template= Handlebars.compile(document.querySelector('#left').innerHTML);
    const content = template({});
    element.style.animationPlayState = 'running';
    setTimeout(() =>  {
      element.innerHTML = content;},350);
    document.getElementById("agree").disabled = true;
    element.addEventListener('animationend', enable())
    }
function enable() {
    if (data_received){
        document.getElementById("agree").disabled = false;
    }
    else{
        setTimeout(enable(),300)
    }
}
function vanishR() {
    let element = document.getElementById("elementtofadeR")
    const template= Handlebars.compile(document.querySelector('#right').innerHTML);
    const content = template({});
    element.style.animationPlayState = 'running';
    setTimeout(() =>  {
        element.innerHTML = content;},350);
    }

function check() {
    var length = document.getElementById('username').value.length;
    var value =  document.getElementById('username').value;
    var lengthPass = document.getElementById('password').value.length;
    console.log(data.users.includes(value))
    if (data.users.includes(value)){
        alert("Username exists");
        return false
    }
    if (length<5) {
        alert("Sorry username too short! Must be 5 characters atleast");
        return false }
    if (lengthPass<8) {
        alert("Password must be atleast 8 characters long!");
        return false }
    return true
    }
function AgreeCheck() {
        var verify = check();
        document.getElementById("agree").checked = verify;
        document.getElementById("sub").disabled = !verify;
        document.getElementById("username").disabled = verify;
        document.getElementById("password").disabled = verify;
    }
