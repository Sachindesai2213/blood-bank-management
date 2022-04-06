from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from main.models import *
# Create your views here.


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        print(request.user)
        response = Response()
        username = request.data['username']
        password = request.data['password']
        username_exists = User.objects.filter(username=username).exists()
        status = 'Invalid Username'
        if username_exists:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # payload = jwt_payload_handler(user)
                # token = jwt_encode_handler(payload)
                # response.set_cookie(key='token', value=token, httponly=True)
                status = 'Successful'
                # is_mfa_user = EmployeeCompany.objects.filter(user_id=request.user.id).last().is_mfa_user
                # if not is_mfa_user:
                request.session['username'] = user.username
                request.session['user_id'] = user.id
                response.data = {
                    'status': status,
                }
            else:
                status = 'Incorrect Password'
                response.data = {
                    'status': status,
                }
        return response


@api_view(['POST', 'PUT'])
def signup_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.data['username'], first_name=request.data['first_name'],last_name=request.data['last_name'], email=request.data['email'], password=request.data['password'])
        user_data = UserPersonalInfo(
            user = user,
            age = request.data['age'],
            blood_type_id = request.data['blood_group'],
            contact = request.data['contact'],
        )
        user_data.save()
        return Response()
    elif request.method == 'PUT':
        user_id = request.user.id
        user_data = UserPersonalInfo.objects.get(user_id=user_id)
        # user_data.age = request.data['age']
        user_data.blood_type_id = request.data['blood_type_id']
        user_data.contact = request.data['contact']
        # user_data.is_active_donar = request.data['is_active_donar']
        user_data.save()
        user = User.objects.get(id=user_id)
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.email = request.data['email']
        user.save()
        return Response()        


@api_view(['POST'])
def requirement_view(request):
    if request.method == 'POST':
        requirement = Requirement(
            user_id = request.user.id,
            blood_type_id = request.data['blood_type_id'],
            quantity = request.data['quantity'],
            location = request.data['location'],
            description = request.data['description'],
        )
        requirement.save()
        user_requirements = list(Requirement.objects.filter(user=request.user).values('location', 'blood_type__abbr', 'quantity', 'description', 'date_time', 'requirement_fulfilled'))
        for requirement in user_requirements:
            requirement['date_time'] = requirement['date_time'].strftime('%d-%m-%Y %H:%M')
            requirement['requirement_fulfilled'] = 'Yes' if requirement['requirement_fulfilled'] else 'No'
        data = {
            'user_requirements': user_requirements,
        }
        return Response(data)


@api_view(['POST'])
def requirement_donors_view(request):
    if request.method == 'POST':
        requirement_donors = RequirementDonors(
            requirement_id = request.data['requirement_id'],
            donor_id = request.user.id,
        )
        requirement_donors.save()
        return Response()

@api_view(['PATCH'])
def requirement_donor_view(request, id):
    if request.method == 'PATCH':
        requirement_donor = RequirementDonors.objects.get(id=id)
        requirement_donor.acceptance_status = True
        requirement_donor.save(update_fields=['acceptance_status'])
        return Response()