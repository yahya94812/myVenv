# from mySampleLib import SimpleMaths #importing a class if it is not in any package
# #    file(module name)  className
# a=SimpleMaths(1,0)
# a.addition()
# a.subtraction()


import samplePackage.mySampleLib as msl #importing whole module
#        packageName.file(module) name
#it import whole module (require to use file(module) name or alias before the class name using (.) for object initialization) we can use it for using multiple classes from a module
b=msl.SimpleMaths(1,1)
b.addition()
b.subtraction()
#we also use normal functions from the lib
msl.sampleFunction(2,2)


from samplePackage.mySampleLib import *
#    file(module) name
#it import all the classes no need for using module name {warning : name conflict may arise}
c=SimpleMaths(1,2)
c.addition()
c.subtraction()


