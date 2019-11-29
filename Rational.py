class Rational(object):
    """This creates a rational number (fraction)"""

    def __init__(self, numerator=0, denominator=1):
        """Constructor for a rational number with a numerator and denominator"""
        self.__originalNumerator = numerator
        self.__originalDenominator = denominator
        self.__reducedNumerator = ''
        self.__reduceDenominator = ''
        self.__reduce()


    def getOriginal(self):
        """returns a string representation of the original rational number"""
        fraction = str(self.__originalNumerator)+'/'+str(self.__originalDenominator)
        return fraction

    def getDecimal(self):
        """returns a string representatin of the rational number in decimal form"""
        decimal = str(self.__originalNumerator/self.__originalDenominator)
        return decimal

    def __reduce(self):
        """reduces the rational number """
        GCF = self.__getGCF(self.__originalNumerator,self.__originalDenominator)
        self.__reducedNumerator = (self.__originalNumerator//GCF)
        self.reducedDenominator = (self.__originalDenominator//GCF)

    def getRational(self):
        """return a string representation of the reduced rational number"""
        rationalString = str(self.__reducedNumerator)+'/'+str(self.__reducedDenominator)
        return rationalString
    def displayData(self):
        print()
        print(self.getOriginal() + " equals " + self.getDecimal()+ " and ")
        print(self.getOriginal() +" reduces to "+ self.getRational())
        print()

    def __getGCF(self, num1: int, num2: int):
        """returns the greatest common factor of 2 integer values"""
        rem = None
        gcf = None
        while (rem != 0):
            rem = num1 % num2
            if (rem == 0):
                gcf = num2
            else:
                num1 = num2
                num2 = rem
        return gcf;
    @staticmethod
    def multiply(r1,r2):
        """multiplies rational number r1 and r2 to create rational number r3"""
        num3 = (r1.__reducedNumerator * r2.__reducedNumerator)
        den3 = (r1.reducedDenominator * r2.reducedDenominator)
        r3 = Rational(num3,den3)
        return r3
    def subtract(r1,r2):
        """subtracts object r2 from r1 to make object r3"""
        den = (r1.reducedDenominator * r2.reducedDenominator)
        num = (r2.reducedDenominator * r1.__reducedNumerator) - (r1.reducedDenominator * r2.__reducedNumerator)
        r3 = Rational(num,den)
        return r3

    def divide(r1,r2):
        """multiplies r1 by the reciporicle of r2 to make object r3 (same as dividing r1 by r2)"""
        num3 = (r1.__reducedNumerator * r2.reducedDenominator)
        den3 = (r1.reducedDenominator * r2.__reducedNumerator)
        r3 = Rational(num3,den3)
        return r3
    def add(r1,r2):
        """adds rational number r1 to rational number r2 to make object r3"""
        den = (r1.reducedDenominator * r2.reducedDenominator)
        num = (r2.reducedDenominator * r1.__reducedNumerator) + (r1.reducedDenominator * r2.__reducedNumerator)
        r3 = Rational(num,den)
        return r3