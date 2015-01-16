function cargarPerfil(){
	var request=new XMLHttpRequest();
	request.open("GET","../xml/perfil.xml", true);
	request.addEventListener("load", mostrarPerfil, false);
	request.send();
}
	
function mostrarPerfil(response){
	var docxml=response.target.responseXML;
	console.log(response);
	var perfil=docxml.getElementsByTagName("perfil");
	var url = document.URL;
    var res = url.split("=");
    var id= res[res.length-1];
    console.log(id);

    var links=document.getElementsByClassName("link");

    for (i = 0; i < links.length; i++) {
         links[i].setAttribute("href",links[i].getAttribute("href")+"? id="+id);
        
    }


    var divNombreEmpresa=document.getElementById("nombreEmpresa");
    var divTextoInfor=document.getElementById("textoInfor");
     var divInformacion=document.getElementById("infor");
      var divDescripcion=document.getElementById("descripcion");
       var divMision=document.getElementById("mision");
       var divInforPers=document.getElementById("inforPersonal");
       var divActividad = document.getElementById("actividad");
       var divContacto = document.getElementById("IDcontacto");
    
    for(i=0; i<perfil.length; i++){
         perfiles=perfil[i];
         var idPerfil = perfiles.getElementsByTagName("id")[0].innerHTML;
         console.log(idPerfil);
         if(idPerfil==id){
         var nombre=perfiles.getElementsByTagName("nombre")[0].innerHTML;
         var informacion=perfiles.getElementsByTagName("informacion")[0].innerHTML;
         var descripcion=perfiles.getElementsByTagName("descripcion")[0].innerHTML;
         var mision=perfiles.getElementsByTagName("mision")[0].innerHTML;
         var actividad=perfiles.getElementsByTagName("actividad")[0].innerHTML;
         
         var persona=perfiles.getElementsByTagName("persona")[0].innerHTML;
         var identificacion=perfiles.getElementsByTagName("ci")[0].innerHTML;
         var institucion=perfiles.getElementsByTagName("institucion")[0].innerHTML;
         var cargo=perfiles.getElementsByTagName("cargo")[0].innerHTML;
         var pais=perfiles.getElementsByTagName("pais")[0].innerHTML;
         var ciudad=perfiles.getElementsByTagName("ciudad")[0].innerHTML;
         var web=perfiles.getElementsByTagName("sitioweb")[0].innerHTML;
         var telefono=perfiles.getElementsByTagName("telefono")[0].innerHTML;
         var fechanac=perfiles.getElementsByTagName("nacimiento")[0].innerHTML;
         var area=perfiles.getElementsByTagName("areasinteres")[0].innerHTML;

         var direccion=perfiles.getElementsByTagName("direccion")[0].innerHTML;
         var webempresa=perfiles.getElementsByTagName("webempresa")[0].innerHTML;
         var telfempresa=perfiles.getElementsByTagName("telfempresa")[0].innerHTML;
         var horario=perfiles.getElementsByTagName("horario")[0].innerHTML;
         var mail=perfiles.getElementsByTagName("correo")[0].innerHTML;
         var foto=perfiles.getElementsByTagName("foto")[0].innerHTML;


         var elementLI=document.createElement("li");
         var elementLI2=document.createElement("li");
          var elementLI3=document.createElement("li");
           var elementLI4=document.createElement("li");
            var elementLI5=document.createElement("li");
             var elementLI6=document.createElement("li");
              var elementLI7=document.createElement("li");
               var elementLI8=document.createElement("li");
                var elementLI9=document.createElement("li");
                 var elementLI10=document.createElement("li");
                 var elementLI11=document.createElement("li");
                 var elementLI12=document.createElement("li");
                 var elementLI13=document.createElement("li");
                 var elementLI14=document.createElement("li");
                 var elementLI15=document.createElement("li");
                 var elementLI16=document.createElement("li");
                 var elementLI17=document.createElement("li");

         elementLI.innerHTML ="Nombre: "+persona;
         divInforPers.appendChild(elementLI);
         elementLI2.innerHTML ="Identificacion: "+identificacion;
         divInforPers.appendChild(elementLI2);
         elementLI3.innerHTML ="Institucion a la que pertenece: "+institucion;
         divInforPers.appendChild(elementLI3);
         elementLI4.innerHTML ="Cargo: "+cargo;
         divInforPers.appendChild(elementLI4);
         elementLI5.innerHTML ="Pais: "+pais;
         divInforPers.appendChild(elementLI5);
          elementLI6.innerHTML ="Ciudad: "+ciudad;
         divInforPers.appendChild(elementLI6);
          elementLI7.innerHTML ="Sitio Web: "+web;
         divInforPers.appendChild(elementLI7);
          elementLI8.innerHTML ="Telefono: "+telefono;
         divInforPers.appendChild(elementLI8);
          elementLI9.innerHTML ="Fecha de Nacimiento: "+fechanac;
         divInforPers.appendChild(elementLI9);
          elementLI10.innerHTML ="Area de interes: "+area;
         divInforPers.appendChild(elementLI10);

         document.getElementById("imagenPersona").setAttribute("src",foto);
         document.getElementById("nombreBienvenida").innerHTML ="Bienvenido " +persona;
         
         elementLI15.innerHTML ="RUC: "+identificacion+'001';
         divContacto.appendChild(elementLI15);
         elementLI16.innerHTML ="Razon Social: "+nombre;
         divContacto.appendChild(elementLI16);
         elementLI11.innerHTML ="Direccion empresa: "+direccion;
         divContacto.appendChild(elementLI11);
         elementLI12.innerHTML ="Sitio Web Empresa: "+webempresa;
         divContacto.appendChild(elementLI12);
         elementLI13.innerHTML ="Telefono Empresa: "+telfempresa;
         divContacto.appendChild(elementLI13);
         elementLI14.innerHTML ="Horario de atencion: "+horario;
         divContacto.appendChild(elementLI14);
         elementLI17.innerHTML = "E-mail: " + mail;
         divContacto.appendChild(elementLI17);

         divActividad.innerHTML = actividad;
        divNombreEmpresa.innerHTML =nombre;
        divInformacion.innerHTML =informacion;
        divDescripcion.innerHTML =descripcion;
        divMision.innerHTML =mision;
        }
    }
    
    
}


window.addEventListener("load", cargarPerfil, false);