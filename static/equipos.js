async function equipos(){
  const equipos = (await axios.get('/consultar-equipos')).data
  equipos.equipos.forEach((equipo) => {
    document.querySelector('#equipos').innerHTML += `
      <div class="small large-3 columns">
        <div class="product-image">
            <img src="${equipo.url}" alt="">
        </div>
        <div class="info">
            <div>
                <span class="price">$${equipo.precio}</span>
            </div>
            <div>
                <h3>${equipo.nombre}</h3>
            </div>
            <div>
                <input value="0" type="number" name="${equipo.id}"/>
            </div>
        </div>
      </div>
    `
  }) 
}

equipos()

async function alquilar(event){
  event.preventDefault()
  const direccion = document.querySelector('#direccion').value.trim()
  const inicio = document.querySelector('#inicio').value.trim()
  const fin = document.querySelector('#fin').value.trim()
  if (!direccion) {
    return alert('Debes escribir una direccion')
  }
  if (!inicio) {
      return alert('Debes escribir una fecha de inicio')
  }
  if (!fin) {
    return alert('Debes escribir una fecha de fin')
  }
  const alquilar = {}
  const equipos = document.querySelectorAll('#equipos input')
  for(let i = 0 ; i < equipos.length ; i++){
    const equipo = equipos[i]
    if(equipo.value > 0) {
      alquilar[equipo.name] = equipo.value
    }
  }
  if(Object.keys(alquilar).length == 0){
    return alert('Debes agregar equipos')
  }
  try{
    await axios.post('/alquilar', {
        direccion: direccion,
        inicio: inicio,
        fin: fin,
        alquilar: alquilar,
    }, {
        headers: {
            'X-CSRFToken': window.csrftoken
        }
    });
    alert('Se ha guardado la solicitud de alquiler')
    location.reload()
  } catch(e){
      alert('No se pude crear la orden')
  }
}