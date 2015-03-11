// Ask the browser for permission to show notifications
// Taken from https://developer.mozilla.org/en-US/docs/Web/API/Notification/Using_Web_Notifications
window.addEventListener('load', function () {
    Notification.requestPermission(function (status) {
        // This allows to use Notification.permission with Chrome/Safari
        if (Notification.permission !== status) {
            Notification.permission = status;
        }
    });
});


// Create an instance of vanilla dragon
var dragon = new VanillaDragon({onopen: onOpen, onchannelmessage: onChannelMessage});


// New channel message received
function onChannelMessage(channels, datos) {
    // Add the notification
    console.log(datos);
    if (datos.action === "created") {
        addNotification((datos.data));
    }
}


// SwampDragon connection open
function onOpen() {
    // Once the connection is open, subscribe to notifications
    dragon.subscribe('notifications', 'notificaciones');
    
}


// Add new notifications
function addNotification(notification) {
    // If we have permission to show browser notifications
    // we can show the notification
    if (window.Notification && Notification.permission === "granted") {
        new Notification(notification.message);
    }

}

function notifRec(name){
    new Notification('Mensaje Enviado Exitosamente',name);
    console.log(Notification.user);
    if(Notification.user.username == name){
        window.addEventListener('load',function(){
            new Notification('Ha recibido un nuevo mensaje',name);
        });
    }
}


