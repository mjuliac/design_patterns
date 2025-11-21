from behavior.template_method.template import ITemplate

class Method1(ITemplate):
    def step1(self):
        print("Executing method 1 step 1")

    def step2(self):
        print("Executing method 1 step 2")
    
    
class Method2(ITemplate):
    def step1(self):
        print("Executing method 2 step 1")
    
    def step2(self):
        print("Executing method 2 step 2")