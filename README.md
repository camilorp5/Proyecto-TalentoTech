# Proyecto Grupo 2
**Introducción**: Dada la gran relevancia de las energías renovables a nivel mundial, Colombia se ha encamindo a construir una relación directa con la energía hídrica, base importante del sistema energético nacional. Este proyecto tiene como principal objetivo analizar el aporte energético de algunas fuentes hídricas ubicadas en diferentes regiones del país entre el año 2019 al 2024. Documentación oficial del proyecto en este [enlace](https://docs.google.com/document/d/1n6q818P3u3SP_zAPgCsf90acUZrU_f-vM8FBaTLnppo/edit?usp=sharing)

## Enlaces importantes
- [**Visualización Streamlit**](https://basepy-3riwstbgnthr7eknrgrefv.streamlit.app/)

## Bases de datos
- BD_oficial
**Descripción**: Esta base de datos cuenta con diferentes registros sobre los aportes energéticos de diferentes fuentes hídricas del país al Sistema Interconectado Nacional. Fue necesario realizar diferentes concatenaciones de varias bases de datos, a conitnuación se presenta la descripción de este proceso

_Fuente_: [Enlace a la base de datos](https://www.datos.gov.co/dataset/Aportes-Hidr-ulicos-Energ-a/wa2n-56u4/about_data)

- FuentesHidricas
**Descripción**: Esta base de datos cuenta con la ubicación en latitud y longitud de cada uno de las fuentes hídricas y su respectivos código de serie. Esta fue construída a partir de diferentes estudios y comparaciones entre los datos presentados.

## Código fuente
- base.py: Código fuente para la visualización realizada en Streamlit.
- Concatenacion.ipynb: Código dónde se realiza la concatenación de las bases de datos anuales y se realiza una exploración básica de los datos.
