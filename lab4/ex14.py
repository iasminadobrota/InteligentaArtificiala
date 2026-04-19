#Construiți un scor general pentru fiecare jucător pe baza unei
# formule proprii:
# ex:Scor = 0.3 * Overall + 0.3 * Potential + 0.2 * SprintSpeed + 0.2 * Passing

import pandas as pd
data = pd.read_csv("data.csv")

data["Scor"] = (
    0.3 * data["Overall"] +
    0.3 * data["Potential"] +
    0.2 * data["SprintSpeed"] +
    0.2 * data["ShortPassing"]
)

print(data[["Name", "Scor"]].head(10))