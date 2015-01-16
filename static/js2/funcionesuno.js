var id=-1;

function inicializar(){
	
	var login=document.getElementById("loginbtn");
    login.addEventListener("click", logingetfunction, false);
    
	}
    
function logingetfunction(){

var request=new XMLHttpRequest();
    request.open("GET", "../xml/usuarios.xml", true);
    request.addEventListener("load", loginresponsefunction, false);
    request.send();
    console.log("ENVIADO");
    

}
function loginresponsefunction(response){
     var uname=document.getElementById("exampleInputEmail1").value;
    var clave=document.getElementById("exampleInputPassword1").value;
    console.log("c "+ uname+"p "+clave);
    
    var docxml= response.target.responseXML;
    console.log(response);
    var listausuarios=docxml.getElementsByTagName("usuario");
    
    console.log(uname+" "+clave);
    for(i=0; i<listausuarios.length; i++){
        usuario=listausuarios[i];
        nombreactual=usuario.getElementsByTagName("correo")[0].innerHTML;
        claveactual=usuario.getElementsByTagName("clave")[0].innerHTML;
        id=usuario.getElementsByTagName("id")[0].innerHTML;
        
        
        if(nombreactual==uname && clave==claveactual){
            
            console.log("login");
            
            
            document.location.href="../USUARIO_profile.html?id="+id;
            //document.location.href="../USUARIO_profile.html";
            
            break;
            
            
        }
        //document.location.href="../USUARIO_profile.html";
            
        if(nombreactual==uname) console.log("nombres iguales");
        if(clave==claveactual) console.log("claves iguales");
        
        
        
       
    }
    if(id==-1){
    console.log("login failed incorrecto username o pwd");
    alert("login failed incorrecto username o pwd");
    
    }
}

window.addEventListener("load", inicializar, false);
