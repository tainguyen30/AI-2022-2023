import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

food = ctrl.Antecedent(np.arange(0,11,1), "Food")
service = ctrl.Antecedent(np.arange(0,11,1), "Service")
tip = ctrl.Consequent(np.arange(10,31,1), "Tip")
food["poor"] = fuzz.trimf(food.universe, [0,0,5])
food["average"] = fuzz.trimf(food.universe, [0,5,10])
food["good"] = fuzz.trimf(food.universe, [5,10,10])

service["bad"] = fuzz.trimf(service.universe, [0,0,5])
service["average"] = fuzz.trimf(service.universe, [0,5,10])
service["good"] = fuzz.trimf(service.universe, [5,10,10])

tip["less"] = fuzz.trimf(tip.universe, [10,10,20])
tip["average"] = fuzz.trimf(tip.universe, [10,20,20])
tip["more"] = fuzz.trimf(tip.universe, [20,30,30])


# Rules
rule1_1 = ctrl.Rule(food["poor"] & service["bad"], tip["less"])
rule1_2 = ctrl.Rule(food["poor"] & service["average"], tip["less"])
rule1_3 = ctrl.Rule(food["poor"] & service["good"], tip["less"])

rule2_1 = ctrl.Rule(food["average"] & service["bad"], tip["less"])
rule2_2 = ctrl.Rule(food["average"] & service["average"], tip["average"])
rule2_3 = ctrl.Rule(food["average"] & service["good"], tip["average"])

rule3_1 = ctrl.Rule(food["good"] & service["bad"], tip["less"])
rule3_2 = ctrl.Rule(food["good"] & service["average"], tip["more"])
rule3_3 = ctrl.Rule(food["good"] & service["good"], tip["more"])

# Training
tipping_ctrl = ctrl.ControlSystem([rule1_1, rule1_2, rule1_3, rule2_1, rule2_2, rule2_3, rule3_1, rule3_2, rule3_3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Training input
tipping.input["Food"] = 6.5
tipping.input["Service"] = 9.8

# Training output
tipping.compute()

# View
food["average"].view()
food.view()
service.view()
tip.view()
tip.view(sim=tipping)
print(tipping.output["Tip"])


