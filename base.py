import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

base_of = pd.read_csv("BD_oficial.csv")

# Crear pestañas
tab1, tab2, tab3, tab4, tab5= st.tabs(["Descripción", "Base de datos", "Limpieza", "Visualización por región", "Visualización por tiempo"])


# Contenido de la primera pestaña
with tab1: 
    st.title("Proyecto Grupo 2")
    st.markdown(f'''**Breve descripción:** Dada la gran relevancia de las energías renovables 
                a nivel mundial, Colombia se ha encamindo a construir una relación directa con la energía hídrica,
                base importante del sistema energético nacional.  Este proyecto tiene como principal objetivo analizar 
                el aporte energético de algunas fuentes hídricas ubicadas en  diferentes regiones del país entre el año 
                2019 al 2024. \nDocumentación oficial del proyecto en este [enlace](https://docs.google.com/document/d/1n6q818P3u3SP_zAPgCsf90acUZrU_f-vM8FBaTLnppo/edit?usp=sharing)
                ''')

# Contenido de la segunda pestaña
with tab2:
    st.subheader("Base de datos")
    st.markdown(f'''**Descripción:** Esta base de datos cuenta con diferentes registros sobre los aportes energéticos
                de diferentes fuentes hídricas del país al Sistema Interconectado Nacional. Fue necesario realizar diferentes concatenaciones de varias bases de datos,
                a conitnuación se presenta la descripción de este proceso
                \n**Fuente:** [Enlace a la base de datos](https://www.datos.gov.co/dataset/Aportes-Hidr-ulicos-Energ-a/wa2n-56u4/about_data)   
                ''')
    st.write(base_of)

    st.subheader("Concatenación")
    codigo = '''input_path_file = '/content/drive/MyDrive/Programación/Talento tech/Proyecto/Metan las BD/' ## Carpeta con las bases a concatenar
    output_path_file = '/content/drive/MyDrive/Programación/Talento tech/Proyecto/' ## Carpeta dónde extraer la base de datos concatenada

    excel_file_list = os.listdir(input_path_file)
    excel_file_list.sort() ## Organizar las bases de datos del menor año al mayor
    excel_file_list
    df_of = pd.DataFrame()

    for i in excel_file_list:
      df = pd.read_csv(input_path_file + i)
      df_of = pd.concat([df_of, df], ignore_index = True)

    df_of'''
    st.markdown("""El proceso de concatenación de bases de datos tuvo cómo base los siguientes pasos:
                \n1. **Escogencia de los datos:** Para obtener una buena visualización de los datos, y lograr el análisis adecuado de estos, hemos escogido los días primero de cada mes a lo largo de los años 2019 al 2024.
                \n2. **Descarga:** Se ha escogido una fuente de Datos Abiertos, sin embargo, fue necesario descargar cada dia en un csv por separado. Fuente: https://www.simem.co/datadetail/2bff145f-a233-4644-b5eb-74188dfba51c
                \n3. **Concatenación:** Realizamos una concatenación anual y luego otra sobre las bases de datos de cada año (para evitar sobrecarga del collab omitimos la primera concatenación).
                \n4. **Continuación:** Posteriormente procedemos a hacer uso de funciones de estadística descriptiva, limpieza y visualización de los datos.""")

    st.code(codigo)

    st.subheader("Exploración")
    st.text("Haciendo uso de la estadística descriptiva realizaremos una exploración\ninicial del Dataset")
    st.markdown(f"La cantidad total de registros es: `{len(base_of)}`")
    st.markdown(f"La cantidad total de columnas es: ``")
    st.code("base_of.describe()")
    st.write(base_of.describe())
    st.code("base_of.info()")
    st.dataframe(base_of.info())
    st.markdown(f"A continuación brindamos información útil sobre las columnas de nuestro Dataset")
    df_info = pd.DataFrame({
        "Columnas":["FechaPublicacion", "Fecha", "CodigoDuracion", "CodigoSerieHidrologica", "RegionHidrologica", "AportesHidricosEnergia", "PromedioAcumuladoEnergia", "MediaHistoricaEnergia", "AportesHidricosEnergiaPSS95"],
        "Descripción": ["Fecha de publicación del dato en el SIMEM",
                        "Fecha de representación de la información",
                        "Código de duración de la variable en formato ISO8601",
                        "Código único para identificar una serie hidrologica o un río del Sistema Interconectado Nacional",
                        "Zona geográfica en la cual se agrupan elementos con características hidrológicas similares",
                        "Aporte hídrico asociado con un recurso de generación despachado centralmente en kWh",
                        "Aportes hidricos promedio para lo que va corrido del mes en kWh",
                        "Promedio mensual multianual de la serie hidrológica aprobada por Acuerdo CNO en kWh",
                        "Hidrología al 95% (en kWh)"],
        "Tipo": ["Fecha", "Fecha", "Texto", "Texto", "Texto", "Decimal", "Decimal", "Decimal", "Decimal"]})
    st.write(df_info)
    
# Contenido de la tercera pestaña
with tab3:
    st.subheader("Limpieza")
    st.markdown("Procederemos a realizar la limpieza de los datos, primero conozcamos sobre los datos nulos dentro del DataFrame")

    st.write(base_of.isnull().sum())
    st.markdown(f"La cantidad total de registros antes de la limpueza es: `{len(base_of)}`")
    st.markdown("Analicemos el siguiente filtro, se pueden notar registros que a pesar de tener el mismo Codigo cuentan con una region Nula.")
    st.write(base_of[base_of["CodigoSerieHidrologica"]=="ALICBOGO"])
    st.markdown("Hemos cambiado los valores nulos por la region correspondiente.")
    base_of.loc[base_of['CodigoSerieHidrologica'] == 'ALICBOGO', 'RegionHidrologica'] = 'Centro'
    st.write(base_of[base_of["CodigoSerieHidrologica"]=="ALICBOGO"])
    st.markdown("Debido a que el Dataset cuenta con gran cantidad de datos podemos eliminar aquellos datos nulos que no aportan al estudio.")

    base_of.dropna(inplace=True)
    st.write(base_of)
    st.markdown(f"La cantidad total de registros después de la limpueza es: `{len(base_of)}`\n Comprobemos que no queden valores nulos, así: ")
    st.code("base_of.isnull().sum()")
    st.write(base_of.isnull().sum())
    
# Contenido de la cuarta pestaña
with tab4:

    st.header("Visualización por región")
    st.markdown('''Podriamos empezar comparando la suma total de aportes hídricos que ha hecho cada región hidrológica
                entre los años de estudio (2017-2024)''')
    
    fig1, ax1 = plt.subplots()
    base_of.groupby('RegionHidrologica')['AportesHidricosEnergia'].sum().plot(kind='bar', ax=ax1)
    ax1.set_ylabel("Aportes Hídricos (kWh)")
    ax1.set_title("Aportes Hídricos por Región Hidrológica")
    st.pyplot(fig1)

    st.markdown('''Notemos la diferencia entre los aportes totales realizados al promedio de aportes realizados
                por región hidrológica.''')
    
    df_region = base_of.iloc[:, [4, 5, 6, 7, 8]].groupby("RegionHidrologica").mean().loc[:, "AportesHidricosEnergia": "AportesHidricosEnergiaPSS95"]
    st.write(df_region)
    st.bar_chart(df_region["AportesHidricosEnergia"])

    st.markdown('''Esta diferencia se puede presentar por la cantidad de registros existentes por Región. Para
                poder comprobar esto realizamos un conteo ''')
    

    df_conteo = base_of[["RegionHidrologica", "AportesHidricosEnergia"]]
    conteo_regiones = df_conteo['RegionHidrologica'].value_counts()
    st.write(conteo_regiones)
    st.bar_chart(conteo_regiones, x_label="Regiones", y_label="Conteo")


    ## Graficar mapa
    df_fuentes = pd.read_csv("FuentesHidricas.csv")
    df_group = base_of[["CodigoSerieHidrologica","AportesHidricosEnergia","PromedioAcumuladoEnergia","MediaHistoricaEnergia","AportesHidricosEnergiaPSS95"]].groupby("CodigoSerieHidrologica").mean().loc[:, "AportesHidricosEnergia": "AportesHidricosEnergiaPSS95"]
    st.markdown('''Además podemos analizar el aporte por fuente hidrologica y realizar una comparación visual en el mapa de Colombia
                Primero agrupamos los datos por la columna "CodigoSerieHidrologica" así:''')
    st.write(df_group)
    df_join = df_group.join(df_fuentes.set_index('CodigoSerieHidrologica'), on='CodigoSerieHidrologica')
    st.markdown('''Luego, a través de un análisis detallado hemos creado el siguiente Dataset dónde se encuentra
                la locación en latitudes y longitudes de cada Fuente Hídrica asociada a un Códio de Serie''')
    
    ver_df = st.toggle('Ver DataFrame (fuentes)', value=False)
    if ver_df:
        st.write(df_fuentes)

    ver_df_dos = st.toggle('Ver DataFrame (join)', value=False)
    if ver_df_dos:
        st.write(df_join)
    
    df_total=df_join[["FuentesHidricas","AportesHidricosEnergia","Latitud","Longitud"]]
    df_total["size"]=(df_join["AportesHidricosEnergia"]/1000)+100
    st.write(df_total)

    with st.container(border=True):
        st.header("Mapa Aporte por Fuente")
        st.map(df_total, latitude='Latitud', longitude='Longitud', size= "size")

    ## Gráfico Aportes por Fuente Hídrica
    base_departamentos = base_of[["CodigoSerieHidrologica","RegionHidrologica"]]
    df_totales = df_total.join(base_departamentos.set_index('CodigoSerieHidrologica'), on='CodigoSerieHidrologica')
    lista_departamento=df_totales['RegionHidrologica'].sort_values().unique().tolist()
    lista_departamento.insert(0, 'Todos')
    option=st.selectbox(
        'Seleccione una región',
        lista_departamento
    )
    if option == 'Todos':
        df_filtro=df_totales.groupby(['FuentesHidricas']).AportesHidricosEnergia.mean()
    else:
        df_filtro=df_totales[df_totales['RegionHidrologica']==option].groupby(['FuentesHidricas']).AportesHidricosEnergia.mean()

    fig, ax = plt.subplots()
    ax.barh(df_filtro.index, df_filtro.values, color='skyblue')
    ax.set_ylabel('Fuentes Hídricas')
    ax.set_xlabel('Aportes Hídricos a la Energía')
    plt.xticks(rotation=90)
    with st.container(border=True):
        st.header('Aportes por Fuente Hídrica')
        st.pyplot(fig)

with tab5:
    # Gráfico 3: Serie temporal de los aportes hídricos
    st.subheader("Serie temporal de Aportes Hídricos:")
    base_of['Fecha'] = pd.to_datetime(base_of['Fecha'])  # Para asegurarse de que la columna Fecha esté en formato datetime
    fig3, ax3 = plt.subplots()
    base_of.groupby('Fecha')['AportesHidricosEnergia'].sum().plot(ax=ax3)
    ax3.set_xlabel("Fecha")
    ax3.set_ylabel("Aportes Hídricos (kWh)")
    st.pyplot(fig3)

    # Gráfico 3: Serie temporal de los aportes hídricos 2023-2024
    st.subheader("Gráfico Filtrado Temporal")
    base_of['Fecha'] = pd.to_datetime(base_of['Fecha'])
    
    lista_año_inicio=base_of['Fecha'].sort_values().unique().tolist()
    lista_año_inicio.insert(0, 'Todos')
    option_inicio=st.selectbox(
        'Seleccione una fecha inicial',
        lista_año_inicio,
        key="key_inicio"
    )

    lista_año_final=base_of['Fecha'].sort_values().unique().tolist()
    lista_año_final.insert(0, 'Todos')
    option_final=st.selectbox(
        'Seleccione una fecha final',
        lista_año_final,
        key="key_final"
    )

        # Verificar y convertir fechas si no son "Todos"
    if option_inicio != "Todos":
        option_inicio = pd.to_datetime(option_inicio)
    if option_final != "Todos":
        option_final = pd.to_datetime(option_final)

    # Aplicar el filtro considerando si alguna opción es "Todos"
    if option_inicio != "Todos" and option_final != "Todos":
        base_filtrada_2023 = base_of[(base_of['Fecha'] > option_inicio) & (base_of['Fecha'] < option_final)]
    elif option_inicio != "Todos":
        base_filtrada_2023 = base_of[base_of['Fecha'] > option_inicio]
    elif option_final != "Todos":
        base_filtrada_2023 = base_of[base_of['Fecha'] < option_final]
    else:
        base_filtrada_2023 = base_of 

    fig4, ax4 = plt.subplots()
    base_filtrada_2023.groupby('Fecha')['AportesHidricosEnergia'].sum().plot(ax=ax4)
    ax4.set_xlabel("Fecha")
    ax4.set_ylabel("Aportes Hídricos (kWh)")
    st.pyplot(fig4)