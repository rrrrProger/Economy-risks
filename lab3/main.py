import sys

class Risk_Class:
    def __init__(self, CO2_emissions):
        #in tons
        self.CO2_emissions = CO2_emissions
        #in procents
        self.probability_influence_values = [0.05, 0.5, 1.0, 5.0, 20.0]
        self.probability_incedent_values  = [0.5, 1.0, 10.0, 20.0, 50.0]
        self.risk_low_limit = 0.01
        self.risk_high_limit = 0.15
        self.incedents = ["Meter crash or failure", "Inaccurate data pass to programm", "Computer or server is broken", "Electricity blackout", "Incorrect data reading or displaying"]
        self.type_risks = ["Data miss or inaccuracy", "Inaccurate risk calculation", "Data programm miss", "Data programm miss", "Inaccurate risk calculation"]
        self.probability_influence_risks = [[1, 4], [2, 1], [2 ,2], [1, 2], [1, 5]]

    def calculate_matrix_risks(self):
        self.matrix_risks = [[round(self.probability_influence_values[column] * self.probability_incedent_values[row] * self.CO2_emissions * 0.01 * 0.01, 2) for column in range(len(self.probability_influence_values))] for row in range(len(self.probability_incedent_values))]

    def print_matrix_risks(self):
        string = "Print matrix risks"
        print(f"{string :^60}")
        for row in range(len(self.probability_incedent_values)):
            string = str(self.probability_incedent_values[row])
            print('Probability : ', end="")
            print(f'{string :^5}', end=" ")
            for col in range(len(self.probability_influence_values)):
                print(f'{str(self.matrix_risks[row][col]) :^10}', end=" ")
            print("")
    def get_risk_level(self, probability, influence):
        risk = self.matrix_risks[probability - 1][influence - 1]
        string = ""
        if risk <= self.risk_low_limit * self.CO2_emissions * 0.01:
            string = "Low"
        elif (risk > self.risk_low_limit * self.CO2_emissions * 0.01 and risk < self.risk_high_limit * self.CO2_emissions * 0.01):
            string = "Medium"
        else:
            string = "High"
        print('risk is ', risk, " ", string)
        return risk
    def display_risks_values(self):


#CO2 emmissions in tons
risk = Risk_Class(23259)

#print matrix of risks
risk.calculate_matrix_risks()
risk.print_matrix_risks()
risk.get_risk_level(3,4)
