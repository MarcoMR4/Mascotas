$("#selectFiltro").change(function (e) {
  e.preventDefault();
  if ($("#selectFiltro").val() == "tamaño") {
    var opciones = `
    <option selected value="0">Cualquier tamaño</option>
    <option value="Pequeño">Pequeño</option>
    <option value="Mediano">Mediano</option>
    <option value="Grande">Grande</option>
    `;
    $("#selectOpcionFiltro").prop('disabled', false);
    $("#selectOpcionFiltro").html(opciones);
    $("#btnCancelar").show();
  }
  else if ($("#selectFiltro").val() == "edad") {
    var opciones = `
    <option selected value="0">Cualquier edad</option>
    <option value="Cachorro">Cachorro</option>
    <option value="Joven">Joven</option>
    <option value="Adulto">Adulto</option>
    <option value="Anciano">Anciano</option>
    `;
    $("#selectOpcionFiltro").prop('disabled', false);
    $("#selectOpcionFiltro").html(opciones);
    $("#btnCancelar").show();
  }
  else if ($("#selectFiltro").val() == "genero") {
    var opciones = `
    <option selected value="0">Cualquier genero</option>
    <option value="Macho">Macho</option>
    <option value="Hembra">Hembra</option>
    `;
    $("#selectOpcionFiltro").prop('disabled', false);
    $("#selectOpcionFiltro").html(opciones);
    $("#btnCancelar").show();
  }
  else if ($("#selectFiltro").val() == "tipoAnimal") {
    var opciones = `
    <option selected value="0">Cualquier raza</option>
    <option value="Perro">Perro</option>
    <option value="Gato">Gato</option>
    <option value="Otro">Otro</option>
    `;
    $("#selectOpcionFiltro").prop('disabled', false);
    $("#selectOpcionFiltro").html(opciones);
    $("#btnCancelar").show();
  }
  else if ($("#selectFiltro").val() == "estatus") {
    var opciones = `
    <option selected value="0">Cualquier estado</option>
    <option value="En adopcion">En adopción</option>
    <option value="En proceso">En proceso</option>
    <option value="Adoptado">Adoptado</option>
    `;
    $("#selectOpcionFiltro").prop('disabled', false);
    $("#selectOpcionFiltro").html(opciones);
    $("#btnCancelar").show();
  }
  else if ($("#selectFiltro").val() == 0) {
    var opciones = ``;
    $("#selectOpcionFiltro").html(opciones);
    $("#selectOpcionFiltro").prop('disabled', true);
    if (misMas == 0) {
      $("#btnCancelar").click();
    }
    else {
      misMascotas();
    }
    $("#btnCancelar").hide();
  }
});

