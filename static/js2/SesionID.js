//var id="000";
function mantenerID() { 
    var url = document.URL;
    var res = url.split("=");
    var id= res[res.length-1];
  //id= res[res.length-1];
    console.log(id);

    var links=document.getElementsByClassName("link");

    for (i = 0; i < links.length; i++) {
         links[i].setAttribute("href",links[i].getAttribute("href")+"? id="+id);
        
    }
   //setTimeout(cargarNombreReq,1);
}
function cargarNombreReq(){
	//if(id!="000"){
		var request=new XMLHttpRequest();
		request.open("GET","../xml/perfil.xml", true);
	request.addEventListener("load", mostrarNombre, false);
	request.send();
		
		//}
	console.log("cargar");
	}
	
	function mostrarNombre(response){
		var docxml=response.target.responseXML;
	//console.log(response);
	var perfiles=docxml.getElementsByTagName("perfil");
	//console.log(docxml);
	
	  var url = document.URL;
    var res = url.split("=");
    var id= res[res.length-1];
   
    for(i=0; i<perfiles.length; i++){
         perfil=perfiles[i];
         var idPerfil = perfil.getElementsByTagName("id")[0].innerHTML;
         console.log(idPerfil);
         console.log(id);
         if(idPerfil==id){
			 var nombre=perfil.getElementsByTagName("persona")[0].innerHTML;
			 
			 var div=document.getElementById("nombreBienvenida");
			 div.innerText="Bienvenido "+nombre;
			 
			// alert(nombre);
				}
			  }
	
		}
 window.addEventListener("load",mantenerID,false);
