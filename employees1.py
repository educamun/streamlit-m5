import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

DATE_COLUMN = 'released'
DATA_URL = ('Employees.csv')

import codecs

# Crea titulo de la aplicación
st.title("Deserción Laboral")
st.header("Hackathon HackerEarth 2020")
st.write("""
Análisis de datos para el fenómeno de deserción laboral
que tanto afecta en la actualidad a las empresas y organizaciones
""")

@st.cache
def load_data(nrows):
    doc = codecs.open('Employees.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

def filter_data_by_EmpID(EmpID):
    filtered_data_EmpID = data[data['Employee_ID'].str.upper().str.contains(EmpID)]
    return filtered_data_EmpID

def filter_data_by_Hometown(CdNtl):
    filtered_data_Hometown = data[data['Hometown'].str.upper().str.contains(CdNtl)]
    return filtered_data_Hometown

def filter_data_by_Unit(Unidad):
    filtered_data_Unit = data[data['Unit'].str.upper() == Unidad]
    return filtered_data_Unit

def filter_data_by_EdLvl(EdLvl):
    filtered_data_EdLvl = data[data['Education_Level'] == EdLvl]
    return filtered_data_EdLvl   

def filter_data_by_HometownFull(FullCdNtl):
    filtered_data_HometownFull = data[data['Hometown'] == FullCdNtl]
    return filtered_data_HometownFull

def filter_data_by_UnitFull(FullUnidad):
    filtered_data_UnitFull = data[data['Unit'] == FullUnidad]
    return filtered_data_UnitFull

data_load_state = st.text('Loading cicle nyc data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")

# Creamos sidebar
sidebar = st.sidebar
# Agregamos title y texto en sidebar
if st.sidebar.checkbox('Mostrar todo el dataframe'):
    st.subheader('Todos los empleados')
    st.write(data)

tituloEmpID = st.sidebar.text_input('Numero de empleado:')
btnBuscarEmpID = st.sidebar.button('Buscar empleado')	

if (btnBuscarEmpID):
    data_emp = filter_data_by_EmpID(tituloEmpID.upper())
    count_row = data_emp.shape[0]  # Gives number of rows
    st.write(f"Total de EmpID mostrados : {count_row}")
    st.write(data_emp)	

tituloHometown = st.sidebar.text_input('Hometown :')
btnBuscarCdNtl = st.sidebar.button('Buscar Hometown')	

if (btnBuscarCdNtl):
   data_emp = filter_data_by_Hometown(tituloHometown.upper())
   count_row = data_emp.shape[0]  # Gives number of rows
   st.write(f"Total Ciudades Mostradas : {count_row}")
   st.write(data_emp)	

tituloUnit = st.sidebar.text_input('Unit :')
btnBuscarUnit = st.sidebar.button('Buscar Unit')	

if (btnBuscarUnit):
   data_emp = filter_data_by_Unit(tituloUnit.upper())
   count_row = data_emp.shape[0]  # Gives number of rows
   st.write(f"Total de Unidades Mostradas : {count_row}")
   st.write(data_emp)	

# Creamos selectbox
# Nivel Educativo
selected_EdLvl= st.sidebar.selectbox("Seleccionar Nivel Educativo", data['Education_Level'].unique())
btnFilterbyEdLvl = st.sidebar.button('Filtrar Nivel Educativo')

if (btnFilterbyEdLvl):
   filterbyEdLvl = filter_data_by_EdLvl(selected_EdLvl)
   count_row = filterbyEdLvl.shape[0]  # Gives number of rows
   st.write(f"Frecuencia : {count_row}")
   st.dataframe(filterbyEdLvl)

#Ciudad
selected_CdNtl= st.sidebar.selectbox("Seleccionar Ciudad", data['Hometown'].unique())
btnFilterbyCdNtl = st.sidebar.button('Filtrar por Ciudad')	 

if (btnFilterbyCdNtl):
   filterbyCdNtl = filter_data_by_HometownFull(selected_CdNtl)
   count_row = filterbyCdNtl.shape[0]  # Gives number of rows
   st.write(f"Total de empleados : {count_row}")
   st.dataframe(filterbyCdNtl)

selected_Unit = st.sidebar.selectbox("Seleccionar Unidad", data['Unit'].unique())
btnFilterbyUnit= st.sidebar.button('Buscar Unidad')	

if (btnFilterbyUnit):
   filterbyUnit = filter_data_by_UnitFull(selected_Unit)
   count_row = filterbyUnit.shape[0]  # Gives number of rows
   st.write(f"Total de empleados : {count_row}")
   st.dataframe(filterbyUnit)

#Histograma
fig, ax = plt.subplots()
ax.hist(data.Age)
st.header("Histograma por Edad")
st.pyplot(fig)

fig1, ax = plt.subplots()
ax.hist(data.Hometown)
st.header("Frecuencia por Ciudad")
st.pyplot(fig1)

fig2, ax = plt.subplots()
ax.hist(data.Age)
st.header("Frecuencia por Edad")
st.pyplot(fig2)