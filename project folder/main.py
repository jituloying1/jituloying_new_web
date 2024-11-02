import streamlit as st 

#st.title(" hello jitu")
#st.header("python")
#st.subheader("java")
#st.markdown(" i love python")
#st.code("""for i in range(1,5,1):
#        print("hello jiru "
#        """)
#import pandas as pd
#dataset = pd.read_csv("GAVIA_references.csv")
#st.dataframe(dataset)
name=st.text_input("Enter your name ")
fname=st.text_input(" Enter your Father name")
adr=st.text_input("Enter your adress")
classdata=st.selectbox("Enter your class:",(1,2,3,4,5,6))

button = st.button("Done")
if button:
  st.markdown(f"""
              Name:{name}
              Father Name{fname}
              address:{adr}
              class:{classdata}""")