let log_arr = []

log("Local Flask server has been started")

let file 


function get_img(event){
    file_in = document.querySelector('#fileselect');    
    if(event.target.files.length == 0){ return;}
    file = event.target.files[0];
    let url =URL.createObjectURL(file);
    document.querySelector('#imgtag').src = url;

    log("GET http://127.0.0.1:5000/test images/"+file.name)
    log("image file has been selected")
}

function clear_img(){
    if (file){
        document.querySelector('#imgtag').src='';
        log("selected image"+' ['+ file.name +'] '+"has been cleared") }
    else{
        document.querySelector('#imgtag').src='';
        log("No image has been selected to clear !!!") }
}


function  copy_text(){
    let copytext = document.querySelector("#textarea1");
    copytext.select();
    navigator.clipboard.writeText(copytext.value)

    log("Extracted text has been copied")
}

function log(text){
        let log_box = document.querySelector('#log-box')
        let timestamp = new Date().toLocaleTimeString([],{hour12:false})
    
        let log_txt = '['+ timestamp +']  '+"server.py  $: "+ text +"\n"
        log_arr.push(log_txt)
        log_box.textContent += '['+ timestamp +']  '+"server.py  $: "+ text +"\n" 
        log_box.scrollTop = log_box.scrollHeight
    }


function ex_log(){

setTimeout(
    function(){log("fetching image");},2000
    )
setTimeout(
    function(){log("denoizing image");},11000
)
setTimeout(
    function(){log("binarizing image");},15000
)
setTimeout(
    function(){log("tokenzing binary values");},20000
)
setTimeout(
    function(){log("recognizing features");},25000
)
setTimeout(
    function(){log("extracted successfully");},32000
)

}



function f_size(){
    let len =document.querySelector('#textarea1').value.length
    if(len >= 1 && len <=3 ){
        
        document.querySelector('#textarea1').style = "font-size:1000%; text-align:center; padding-top:10%; "
    } 
    else{
        document.querySelector('#textarea1').style = "font-size:130%;  text-align:none; padding-top:5%;"
    }
}

