Overview
This project is a basic Django web application that allows users to submit personal information through a form. The data is saved to the database, and users can view the submitted
data on a separate page. The project is styled using HTML and CSS, providing a clean and responsive layout. This README will guide you through the project setup and the tasks implemented.

Features
(1) Form Submission: A user-friendly form for collecting user details such as Name, Date of Birth, Gender, City, Email, and Phone Number.
(2) Dynamic Content: Incorporates dynamic data such as the current date/time on the web page.
(3) Data Storage: Submitted form data is stored in the Django database.
(4) User Data Display: Users can view the list of submitted data in a table format.
(5) Responsive Design: The forms and data pages are fully responsive and styled for better user experience.

How It Works
(1) Form Submission: Users visit the contact form page, fill out the details, and submit the form. The data is sent to the backend where it is stored in the Django database.
(2) Display User Data: After form submission, users can visit the "User Data" page to see all the entries displayed in a table format, fetched directly from the database.
(3) Dynamic Content: The index.html page dynamically displays the current date-time and random Quotes using a Python function in views.py. This enhances the interactivity of the page by 
providing real-time data.
