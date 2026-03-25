## 🧠 Finalidad de la app

Es un **proceso ETL de limpieza y estandarización de datos de estudiantes**, enfocado en mejorar la **calidad e integridad de la información**.

---

## ⚙️ ¿Qué hace?

1. **Carga datos**

   * Lee archivos `.csv` desde `data/`

2. **Estandariza estructura**

   * Limpia nombres de columnas (mayúsculas, sin espacios)
   * Normaliza valores nulos (`"", NULL, nan → NaN`)

3. **Completa información faltante**

   * Usa reglas de negocio:

     * Por estudiante (NUI)
     * Por institución
   * Rellena datos vacíos usando registros existentes del mismo grupo
     *(ffill + bfill)*

4. **Genera métricas**

   * Cuenta cuántos valores fueron completados por cada campo

5. **Exporta resultados**

   * Guarda dataset limpio en:

     * CSV
     * Parquet

---

## 🎯 Resultado

Obtienes un dataset:

* Más completo
* Consistente
* Listo para análisis, reportes o toma de decisiones

---

## 🏛️ En contexto de tu rol

Esto aporta directamente a:

* **Estandarización de datos**
* **Depuración y calidad**
* **Preparación para analítica o tableros**

---

