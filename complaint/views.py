from django.shortcuts import render
from rest_framework.views import APIView,Response
from .models import User

# Create your views here.
# class RegesterUSer(APIView):
#     def post(self,request): 
#        try:    
#             count=User.objects.all().filter(email=request.data['email']).count() 
#             if count==0:
#                 User.objects.create(
#                 name=request.data['name'],
#                 email=request.data['email'],
#                 password=request.data['password'],
#                 image=request.FILES.get('image'),
#                 ).save()
#                 isCreated= (User.objects.all().filter(email=request.data['email']).count()==0)
#                 if not isCreated:
#                     return Response({"code":"200","message":"Registration succesfully"})
#                 else:
#                     return Response({"code":"200","message":"Registration failed !"})              
#             else:
#                 return Response({"code":"200","message":"user allready exist"})            
#        except Exception as e:
#            return Response({"error":e})



# add by anil 
class RegisterUser(APIView):
    def post(self, request):
        try:
            # Check if the user already exists
            count = User.objects.filter(email=request.data['email']).count()
            if count == 0:
                # Create a new user
                User.objects.create(
                    full_name=request.data['full_name'],
                    email=request.data['email'],
                    mobile_number=request.data['mobile_number'],
                    gender=request.data['gender'],
                    state=request.data['state'],
                    district=request.data['district'],
                    city=request.data['city'],
                    address=request.data['address'],
                    pin_code=request.data['pin_code'],
                    password=request.data['password'],
                    image=request.FILES.get('image')
                ).save()

                # Check if the user was successfully created
                isCreated = User.objects.filter(email=request.data['email']).count() == 1
                if isCreated:
                    return Response({"code": "200", "message": "Registration successful"})
                else:
                    return Response({"code": "200", "message": "Registration failed"})
            else:
                return Response({"code": "200", "message": "User already exists"})
        except Exception as e:
            return Response({"error": str(e)})
# and by anil 


class LoginUser(APIView):
    def post(self,request):
        try:
            count = User.objects.all().filter(email=request.data['email']).count()
            if(count==1):
                count2=User.objects.all().filter(password=request.data['password'],email=request.data['email']).count()
                if count2==1:
                    user=User.objects.all().filter(password=request.data['password'],email=request.data['email']).values()
                    return Response({"code":"200","message":"Login succesfully","User detials": user})
                else:
                    return Response({"code":"400","message":"Given password is incorrect"})
            else:
                return Response({"code":"401","message":"User not registered"})
        except Exception as e:
            Response({"Exception ":e})





class DeleteUser(APIView):
    def delete(self,request):
        try:
            User.objects.all().filter(id=request.data['id'],email=request.data['email']).delete()
            isDeleted=(User.objects.all().filter(id=request.data['id']).count!=0)
            if isDeleted:
                return Response({"code":"200","message":"User succesfully deleted"})
            else:
                return Response({"code":"500","message":"Something went wrong account is not deleted."})    
        except Exception as e:
            print("error",e)

class UpdatePassword(APIView):
    def post(self, request):
        try:            
            user=User.objects.all().filter(id=request.data['id'],email=request.data['email']).values()
            if not user:
                return Response({"code":"404","message":"User not found",})
            User.objects.all().filter(id=request.data['id'],email=request.data['email']).update(password=request.data['password'])
            return Response({"code":"200","message":"Password succesfully changed"})
        except Exception as e:
            print('error ',e)
            return Response({"code":"500","message":"Some thing went wrong"})


# class UpdateProfileImage(APIView):
#     def post(self, request):
#         try:            
#             user=User.objects.all().filter(id=request.data['id'],email=request.data['email']).values()
#             if not user:
#                 return Response({"code":"404","message":"User not found",})
#             User.objects.all().filter(id=request.data['id'],email=request.data['email']).update(image=request.FILES.get('image'))
#             user =User.objects.all().filter(id=request.data['id'],email=request.data['email']).values()
#             return Response({"code":"200","message":"Profile succesfully changed","userDetails":user})
#         except Exception as e:
#             print('error ',e)
#             return Response({"code":"500","message":"Some thing went wrong"})


class UpdateProfileImage(APIView):
    def post(self, request):
        try:

            try:
                user = User.objects.get(id=request.data['id'], email=request.data['email'])
            except User.DoesNotExist:
                return Response({"code": "404", "message": "User not found"})

            if 'image' in request.FILES:
                user.image = request.FILES['image']
                user.save()
                user1 = User.objects.all().filter(id=request.data['id'], email=request.data['email']).values()
                return Response({"code": "200", "message": "Profile successfully changed", "userDetails": user1})
            else:
                return Response({"code": "400", "message": "Image file is missing"})
        
        except Exception as e:
            print('error', e)
            return Response({"code": "500", "message": "Something went wrong"})