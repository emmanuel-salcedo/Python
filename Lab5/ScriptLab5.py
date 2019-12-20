# 4.	Create 3 objects and pass the CheckingAccountBalance Class to both objects
# 5.	Call the Methods 10 times between the 3 objects
import ScriptLab5Mod1
Chad = ScriptLab5Mod1.CheckingAccountBalance()
Lucas = ScriptLab5Mod1.CheckingAccountBalance()
Sammy = ScriptLab5Mod1.CheckingAccountBalance()

print('Chad')
Chad.deposit()
Chad.withdrawal()
Chad.withdrawal()
Chad.deposit()
Chad.deposit()

print("Lucas")
Lucas.deposit()
Lucas.withdrawal()

print("Sammy")
Sammy.deposit()
Sammy.withdrawal()
Sammy.withdrawal()




