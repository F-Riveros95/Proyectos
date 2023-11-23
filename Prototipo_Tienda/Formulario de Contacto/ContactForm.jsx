const ContactForm = () => {
    function validarFormulario() {
        var nombre = document.getElementById("nombre").value;
        var apellido = document.getElementById("apellido").value;
        var email = document.getElementById("email").value;
        var motivo = document.getElementById("motivo").value;

        if (nombre === "" || apellido === "" || email === ""|| mensaje ==="") {
            document.getElementById("mensaje").textContent = "Por favor completa todos los campos.";
            return false;
        }
        else {
            alert("Le contactaremos luego <3")
        }
        return false;
    }

    return (
        
        <div className="contenedor">
        <h2>Formulario de Contacto</h2>
        <h2>Rellene con su información y la razón por la que quiere contactarnos.</h2>
        <h2>Una vez leída su petición, nos contactaremos con usted.</h2>
        <form id="forma" name="forma" method="post">
          <div className="elemento">
            <label htmlFor="nombres">Nombre:</label>
            <input type="text" id="nombre" name="nombres" required />
          </div>
          <div className="elemento">
            <label htmlFor="apellidos">Apellido:</label>
            <input type="text" id="apellido" name="apellidos" required />
          </div>
          <div className="elemento">
            <label htmlFor="email">Email:</label>
            <input type="email" id="email" name="email" required />
          </div>
          <div className="elemento">
            <label htmlFor="motivo">Deje su mensaje:</label>
            <input type="text" id="motivo" name="mensaje" required />
          </div>
          <button onClick={this.validarFormulario}>Enviar</button>
          <p id="mensaje"></p>
        </form>
      </div>
    )
}

export default ContactForm;



