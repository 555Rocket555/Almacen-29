// app/static/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    // Auto-ocultar alerts después de 4 segundos
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 4000);
    });

    // Validación de contraseñas en registro
    const passwordForm = document.querySelector('form');
    if (passwordForm) {
        passwordForm.addEventListener('submit', function(e) {
            const password = document.getElementById('password');
            const confirmPassword = document.getElementById('confirmar_password');

            if (password && confirmPassword) {
                if (password.value !== confirmPassword.value) {
                    e.preventDefault();
                    alert('Las contraseñas no coinciden. Por favor verifica.');
                    confirmPassword.focus();
                }

                if (password.value.length < 6) {
                    e.preventDefault();
                    alert('La contraseña debe tener al menos 6 caracteres.');
                    password.focus();
                }
            }
        });
    }
});
