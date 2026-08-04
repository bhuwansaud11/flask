# import streamlit as st
# st.sidebar.title("This is the sidebar")
# st.sidebar.write("you can write anything here")
# side_bar=st.sidebar.text_input("Enter the name : ")

# tab1, tab2, tab3=st.tabs(["Tab1","Tab2","Tab3"])
# with tab1:
#     st.write("This is tab1")

# with tab2:
#     st.write("This is tab2")

# with tab3:
#     st.write("this is tab3")

# col1, col2, col3=st.columns(3)
# with col1:
#     st.header("Column 1")
#     st.write("this is col1")

# with col2:
#     st.header("Column 2")
#     st.write("this is col2")

# with col3:
#     st.header("COlumn 3")
#     st.write("This is col3")

# with st.container(border=True):
#     st.write("This is a container")

# placeholder = st.empty()
# placeholder.write("This is an empty placeholder")

# if st.button("Update placeholder"):
#     placeholder.write("This content is updated")

# with st.expander("Expand for more info"):
#     st.write("This is an additional informations")

# if side_bar:
#     st.write(f"You entered this in the sidebar: {side_bar}")


# import streamlit as st
# if "slider" not in st.session_state:
#     st.session_state.slider=25

# min_value=st.slider("set min value",0,50,25)

# st.session_state.slider=st.slider("Slider",min_value,100, st.session_state.slider)

import streamlit as st