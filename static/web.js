const validateEmail = (email) => {
    return email.match(
      /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    );
  };

async function registro(event){
    event.preventDefault()
    const name = document.querySelector('#name').value.trim()  
    const email = document.querySelector('#email').value.trim()
    const password = document.querySelector('#password').value.trim()
    if(!name){
        return alert('Debes escribir un nombre')
    }
    if (!email || !validateEmail(email)) {
        return alert('Debes escribir email valido')
    }
    if (!password) {
        return alert('Debes escribir una contraseña')
    }
    try{
        await axios.post('/guardar-usuario', {
            name: name,
            email: email,
            password: password,
        }, {
            headers: {
                'X-CSRFToken': window.csrftoken
            }
        });
        alert('Se ha registrado el usuario')
        location.href = '/'
    } catch(e){
        alert('No se ha podido crear el usuario')
    }
}

async function login(event){
    event.preventDefault()
    const email = document.querySelector('#email').value.trim()
    const password = document.querySelector('#password').value.trim()
    if (!email) {
        return alert('Debes escribir email valido')
    }
    if (!password) {
        return alert('Debes escribir una contraseña')
    }
    try{
        await axios.post('/login', {
            email: email,
            password: password,
        }, {
            headers: {
                'X-CSRFToken': window.csrftoken
            }
        });
        location.href = '/principal'
    } catch(e){
        alert('Usuario o contraseña incorrecta')
    }
}
