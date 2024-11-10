class Eventsample(object): 
	def __init__(self): 
		self.__eventhandlersample = [] 
	def __iadd__(self, Ehandler): 
		self.__eventhandlersample.append(Ehandler) 
		return self
	def __isub__(self, Ehandler): 
		self.__eventhandlersample.remove(Ehandler) 
		return self

	def __call__(self, *args, **keywargs): 
		for eventhandlersample in self.__eventhandlersample: 
			eventhandlersample(*args, **keywargs) 
				
class MessToDisplay(object): 
	def __init__(self, Mess): 
		self._tele = Mess 
	
	def PrintM(self): 
		print("Simple Message for an Event...")

class sampleclass(object) : 
	
	def __init__(self) : 
		self.OnEH = Eventsample() 
		
	def EHnew(self) : 
		self.OnEH() 
		
	def anotherevent(self,objMeth): 
		self.OnEH += objMeth 
		
	def nexteven(self,objMeth) : 
		self.OnEH -= objMeth 

def Simulation() : 
	newsample = sampleclass() 
	displayamess = MessToDisplay(100) 
	newsample.anotherevent(displayamess.PrintM) 
	newsample.EHnew() 	
if __name__ == "__main__":		 
	Simulation()