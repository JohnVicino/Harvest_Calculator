
from datetime import timedelta
from datetime import date

class Plant:
    
    def __init__ (self, plantType, growthDays):
        
        self.plantType = plantType
        self.growthDays = growthDays
        
    #Calculates harvest and creates log. 
    def harvest(self): 
        
        plantedOn = date.today()
        harvestOn = date.today() + timedelta(days= self.growthDays)
        
        #Checks if the plant's type starts with a vowel. Uses appropriate 'a' or 'an'. Plant type becomes lowercase in the sentence.  
        if self.plantType.lower()[0] in 'aeiou':
            f = open('Harvest.txt','a')
            f.write('\n\nYou planted an {} plant on {}:{}.\nIt will be ready for harvest on {}:{}.'.format(self.plantType.lower(), plantedOn.month, plantedOn.day, harvestOn.month, harvestOn.day))
            f.flush()
            f.close()
            print('\nYou planted an {} plant.\nIt will be ready for harvest on {}:{}.\n\nThe planting and harvest date has been saved to Harvest.txt'.format(self.plantType.lower(), harvestOn.month, harvestOn.day))
            
        else: 
            f = open('Harvest_Dates.txt','a')
            f.write('\n\nYou planted a {} plant on {}:{}.\nIt will be ready for harvest on {}:{}.'.format(self.plantType.lower(), plantedOn.month, plantedOn.day, harvestOn.month, harvestOn.day))
            f.flush()
            f.close()
            print('\nYou planted a {} plant.\nIt will be ready for harvest on {}:{}.\n\nThe planting and harvest date has been saved to Harvest.txt'.format(self.plantType.lower(), harvestOn.month, harvestOn.day))
    
            

addMore= True

while addMore == True:
   
    answer = input("Would you like to add a plant?\n")
    
    if answer.lower() == "yes":
        
        plantType= input('What type of plant are you planting?\n')
        growthDays= input('How many days in the growth cycle?\n')   
        
        inputPlant= Plant(plantType, int(growthDays))
        #Sends inputted plant to calculator
        inputPlant.harvest()
        
        
    elif answer.lower() == "no":
        
        print ('\nNo new plants were added. Thank you!')
        
        addMore= False
        
    else:
        
        print("Please enter yes or no.")



