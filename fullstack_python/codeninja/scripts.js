function sendWpp(){
    window.open('https://api.whatsapp.com/send?phone=5491123204371&text=Hola! Me gustaría saber más sobre codeninja');
};

function enviarMail(){
//  Username: "equipo.codeninja@gmail.com",
//  Password: "Prueba!123",
    var parametros = {
      nombre : document.getElementById("name").value,
      email  : document.getElementById("email").value,
      mensaje: document.getElementById("consulta").value
    };
  
    const serviceID = "service_twz2pvn";
    const templateID = "template_8ahv74z";
  
    emailjs.send(serviceID, templateID, parametros)
           .then((res) =>{
                document.getElementById("name").value = "";
                document.getElementById("email").value = "";
                document.getElementById("consulta").value = "";
                parrafo.innerHTML = "Consulta enviada";
                })
  }

