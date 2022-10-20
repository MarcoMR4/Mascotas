$(document).ready(function () {
    $("#notificacionEnProceso").hide();
    $(".procesoSolicitudes").hide();

    $(".btnEnEspera").click(function (e) {
        $("#notificacionRecientes").hide();
        $(".nuevasSolicitudes").hide();
        $("#notificacionEnProceso").show();
        $(".procesoSolicitudes").show();
    });

    $(".btnRecientes").click(function (e) {
        $("#notificacionRecientes").show();
        $(".nuevasSolicitudes").show();
        $("#notificacionEnProceso").hide();
        $(".procesoSolicitudes").hide();
    });
});