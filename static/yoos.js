window.onload=function(){
    let but = document.getElementById('gol');
    let obj = document.getElementById('nav_lis');
    but.addEventListener('click',()=>{
        if (obj.style.display != 'none') {
            obj.style.display = 'none';
        }
        else{
            obj.style.display = 'block';
        }
    })
    let x = window.matchMedia('(min-width:663px)')
    function media(x) {
        if (x.matches){
            obj.style.display = 'block';
        }
        else{
            obj.style.display = 'none';
        }
    }
    window.onresize = ()=>{
        media(x)
    }
}

