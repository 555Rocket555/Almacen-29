document.addEventListener('DOMContentLoaded', function() {
        
    
    const closeButtons = document.querySelectorAll('.close-btn');
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.parentElement.style.display = 'none';
        });
    });

    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {

        if (alert.classList.contains('alert-success') || alert.classList.contains('alert-info')) {
            setTimeout(() => {
                alert.style.display = 'none';
            }, 5000); // 5 segundos
        }
    });


    const passwordForm = document.querySelector('form');
    if (passwordForm) {
        passwordForm.addEventListener('submit', function(e) {
            const password = document.getElementById('password');
            const confirmPassword = document.getElementById('confirmar_password');

            if (password && confirmPassword) {
                if (password.value !== "" && password.value !== confirmPassword.value) {
                    e.preventDefault(); 
                    alert('Las contraseñas no coinciden. Por favor verifica.');
                    confirmPassword.focus();
                }

                if (password.value !== "" && password.value.length < 6) {
                    e.preventDefault();
                    alert('La contraseña debe tener al menos 6 caracteres.');
                    password.focus();
                }
            }
        });
    }


    
    const switchesUsuarios = document.querySelectorAll('input[id^="switch-activo-"]');

    switchesUsuarios.forEach(sw => {
        sw.addEventListener('change', function(event) {
            
            const usuarioId = this.dataset.userid;
            const estaActivando = this.checked;
            const label = document.querySelector(`label[for="switch-activo-${usuarioId}"]`);

            const confirmacion = confirm(
                `¿Estás seguro de que deseas ${estaActivando ? 'ACTIVAR' : 'DESACTIVAR'} a este usuario?`
            );

            if (confirmacion) {
                fetch(`/admin/usuarios/toggle-activo/${usuarioId}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        label.textContent = data.nuevo_estado ? 'Activo' : 'Inactivo';
                    } else {
                        
                        alert('Error: ' + (data.message || 'No se pudo cambiar el estado.'));
                        event.target.checked = !estaActivando;
                    }
                })
                .catch(error => {
                    alert('Error de conexión. Inténtalo de nuevo.');
                    event.target.checked = !estaActivando;
                });

            } else {
                event.target.checked = !estaActivando;
            }
        });
    });

    const switchesProductos = document.querySelectorAll('input[id^="switch-disponible-"]');
    
    switchesProductos.forEach(sw => {
        sw.addEventListener('change', function(event) {
            
            const productoId = this.dataset.productid; 
            const estaActivando = this.checked; 
            const label = document.querySelector(`label[for="switch-disponible-${productoId}"]`);

            const confirmacion = confirm(
                `¿Estás seguro de que deseas marcar este producto como ${estaActivando ? 'DISPONIBLE' : 'AGOTADO'}?`
            );

            if (confirmacion) {
                
                fetch(`/admin/productos/toggle-disponible/${productoId}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        
                        label.textContent = data.nuevo_estado_texto;
                    } else {
                        alert('Error: ' + (data.message || 'No se pudo cambiar el estado.'));
                        event.target.checked = !estaActivando;
                    }
                })
                .catch(error => {
                    alert('Error de conexión. Inténtalo de nuevo.');
                    event.target.checked = !estaActivando; 
                });

            } else {
            
                event.target.checked = !estaActivando;
            }
        });
    });

});