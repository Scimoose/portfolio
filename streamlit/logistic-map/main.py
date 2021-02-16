import streamlit as st


# to run: streamlit run logistic_map.py
st.write("""

# Population stabilisation with logistic map

""")

# Equation for logistic map is x_n+1 = rx(1-x)

# initial population in 0.00 - 1.00 scale
pop = st.slider('Set population to:', min_value=0.05, max_value=1.0, step=0.01)

# growth rate - input by the user
r = st.slider('Set the growth rate to:', min_value=0.05, max_value=4.0, step=0.05)

# calculate x_n+1
def log_map(initial_population, growth_rate, num_of_iters):
    lst = []
    for i in range(num_of_iters):
        lst.append((initial_population))
        initial_population = growth_rate*initial_population*(1.0-initial_population)
    return lst

try:
    y = log_map(pop, r, 100) # testing purposes
except TypeError:
    y = log_map(0.5, 1, 10)
print(y)

# And a plot of x_n+1 to x
st.line_chart(y)
