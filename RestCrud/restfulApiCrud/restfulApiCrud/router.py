from employeeapi.viewsets import EmployeeViewset
from rest_framework import routers

router= routers.DefaultRouter()
router.register('employee',EmployeeViewset)

#get->list(): localhost:port/api/employee
#get->retrive(): localhost:port/api/employee/id
#put->

#get -> list(),retrive 
# put -> ,update,delete 