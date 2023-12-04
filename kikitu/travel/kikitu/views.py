from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail
from.models import *
from django.contrib import messages




def index(request):
    destinations = Destination.objects.all()
    populars = Popular.objects.all()
    experiences = Gallery.objects.all()
    reviews = Review.objects.all()
    context = {'destinations': destinations, 'experiences': experiences, 'reviews':reviews, 'populars': populars}
    
    return render(request, 'index.html', context)



def about(request):
    faqs = FAQ.objects.all()
    context = {'faqs': faqs}
    return render(request, 'about.html',context)


def booking_terms(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        place = request.POST.get('place')
        guest_number = request.POST.get('guest-number')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        arriving_date = request.POST.get('arriving-date')
        leaving_date = request.POST.get('leaving-date')

        # Form validation (add your validation logic here)
        if not name or not email:
            messages.error(request, 'Name and email are required.')
            return render(request, 'bookingterms.html', {})

        # Sending an email to the website email address from the contact form on the website
        subject = 'New Booking Inquiry'
        message = f'Name: {name}\nEmail: {email}\nPhone number: {number}\nDestination: {place}\nGuest Number: {guest_number}\nAdults: {adults}\nChildren: {children}\nArrival Date: {arriving_date}\nDeparture Date: {leaving_date}'
        from_email = 'info@kikituadventures.com'  # Replace with your email
        to_email = ['info@kikituadventures.com']  # Replace with your email or a list of emails

        send_mail(subject, message, from_email, to_email, fail_silently=False)

        # Sending a confirmation email to the user
        subject_user = 'Tour Booking Confirmation - Get Ready for an Incredible Adventure!'

        message_user =(
            f"Hi {name},\n\n"
            "We are thrilled to inform you that your tour booking with Kikitu Adventures has been successfully confirmed!\n\n"
            f"You are set to embark on an unforgettable journey and explore the wonders of {place}. Our team has received your booking details and we are excited to have you join us.\n\n"
            "Here is a summary of your booking:\n\n"
            f"• Name:             {name}\n"
            f"• Destination:      {place}\n"
            f"• Arrival Date:     {arriving_date}\n"
            f"• Departure Date:   {leaving_date}\n"
            f"• Number of Participants: {guest_number}\n"
            f"    - Adults:       {adults}\n"
            f"    - Children:     {children}\n\n"
            "Be assured that our expert guides and carefully curated itinerary will ensure an amazing experience filled with cultural immersion and breathtaking sights.\n\n"
            "If you have any specific preferences or requirements, please do not hesitate to reach out to our friendly customer support team. We will be more than happy to assist you and make your tour experience even more memorable.\n\n"
            "We can't wait to welcome you on board and create lifelong memories together. Get ready for an incredible adventure!\n\n"
            "Safe travels and see you soon!\n\n"
            "Kind regards,\n"
            "Kikitu Adventures.\n\n"
            "In case of any enquiries kindly feel free to contact us.\n"
            "Email: info@kikituadventures.com\n"
            "Call, Text or WhatsApp: +25475989462."
        )

        send_mail(subject_user, message_user, from_email, [email], fail_silently=False)

        messages.success(request, 'Your booking request has been submitted successfully!')
        return redirect('index')  # Adjust the URL name for your confirmation page

    return render(request, 'bookingterms.html', {})



def travelinfo(request, package_id):
    destination = get_object_or_404(Destination, pk=package_id)
    return render(request, 'Travelinfo.html', {'destination': destination})


def popularinfo(request, package_id):
    popular = get_object_or_404(Popular, pk=package_id)
    return render(request, 'popularinfo.html', {'popular': popular})



