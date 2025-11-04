// app/static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    
    // --- LÓGICA MANUAL PARA CERRAR ALERTAS (PUNTO 1 y 3) ---
    
    // 1. Clic en la "x"
    const closeButtons = document.querySelectorAll('.close-btn');
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            // 'this' es el botón. .parentElement es el div.alert
            this.parentElement.style.display = 'none';
        });
    });

    // 2. Auto-ocultar (después de 5 segundos)
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        // Solo auto-ocultar las de éxito o info (no errores)
        if (alert.classList.contains('alert-success') || alert.classList.contains('alert-info')) {
            setTimeout(() => {
                alert.style.display = 'none';
            }, 5000); // 5 segundos
        }
    });


    // --- LÓGICA PARA VALIDACIÓN DE FORMULARIO (Opcional, pero bueno tenerla) ---
    const passwordForm = document.querySelector('form'); // Asume un solo form por página
    if (passwordForm) {
        passwordForm.addEventListener('submit', function(e) {
            const password = document.getElementById('password');
            const confirmPassword = document.getElementById('confirmar_password');

            // Solo valida si ambos campos existen (ej. en el form de registro)
            if (password && confirmPassword) {
                if (password.value !== "" && password.value !== confirmPassword.value) {
                    e.preventDefault(); // Detiene el envío del formulario
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


    // --- LÓGICA DEL SWITCH "ACTIVO" (PUNTO 4) ---
    // (Esta parte se activará cuando añadas el switch en el Paso 4)
    
    const switches = document.querySelectorAll('input[id^="switch-activo-"]');

    switches.forEach(sw => {
        sw.addEventListener('change', function(event) {
            
            const usuarioId = this.dataset.userid;
            const estaActivando = this.checked;
            const label = document.querySelector(`label[for="switch-activo-${usuarioId}"]`);

            const confirmacion = confirm(
                `¿Estás seguro de que deseas ${estaActivando ? 'ACTIVAR' : 'DESACTIVAR'} a este usuario?`
            );

            if (confirmacion) {
                // fetch() ES JavaScript nativo, no es una librería. Es 100% manual.
                fetch(`/admin/usuarios/toggle-activo/${usuarioId}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Si el servidor confirma, actualizamos el texto
                        label.textContent = data.nuevo_estado ? 'Activo' : 'Inactivo';
                    } else {
                        // Si falla, revertimos el switch
                        alert('Error: ' (data.message || 'No se pudo cambiar el estado.'));
                        event.target.checked = !estaActivando;
                    }
                })
                .catch(error => {
                    alert('Error de conexión. Inténtalo de nuevo.');
                    event.target.checked = !estaActivando;
                });

            } else {
                // Si el usuario cancela, revertimos el switch
                event.target.checked = !estaActivando;
            }
        });
    });

});