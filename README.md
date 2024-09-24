# MDW - Metodologias y Desarrollo Web 2024

### Alumnos:
- Alejo Nardon
- Pablo Hernandez

### Actividad 3
▶️ Objetivo:

Diseñar e implementar un pipeline automatizado en Jenkins que gestione el proceso completo de desarrollo de software, desde la validación de requerimientos hasta el despliegue continuo, utilizando el ecosistema Odoo como referencia.

▶️ Instrucciones:
1. Validación de requerimientos: Configurar un sistema de control de versiones como Git para gestionar los requisitos del proyecto. Crear script que lea los requisitos desde un archivo en el repositorio y verifique que estos están actualizados y completos antes de realizar cualquier cambio de código.
2. Integración continua: Configurar Jenkins para conectarse al repositorio. Implementar un trabajo en Jenkis que ejecute tareas de pre-compilación como verificación de estilo de código y análisis estático.
3. Pruebas: Desarrollar scripts de pruebas unitarias y de integración que se ejecuten automáticamente cada vez que se realiza un commit. Configurar Jenkins para que ejecute estos scripts de prueba y reporte los resultados garantizando que se despliega código sin errores.
4. Despliegue continuo: configurar un proceso que tras la aprobación de las pruebas prepare y despliegue automáticamente la aplicación en un entorno de pruebas y/o producción usando el framework Odoo. Asegurar de incluir pasos de notificación para alertas de despliegue exitoso o fallido

▶️ Requisitos técnicos:
- Usar Jenkins y plugins necesarios para integración con scripts y repositorios de código.
- Scripts de automatización escritos en Bash o Python.
- Documentación detallada de cada etapa del pipeline incluyendo configuración y scripts utilizados.
