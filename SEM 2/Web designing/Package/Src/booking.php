<html>    
    <head>    
        <title>Registration Form</title> 
		<link rel="stylesheet" href="css/booking.css" type="text/css">
    </head>    
    <body>    
	       <link href = "css/registration.css" type = "text/css" rel = "stylesheet" />    
        <h2>BOOK YOUR HOTEL!</h2>    
        <form method="post" enctype = "multipart/form-data" >    
            <div class = "container">    
                <div class = "form_group">    
                    <label>First Name:</label>    
                    <input type = "text" name = "fname" value = "" required/>    
                </div>  
					<div class = "form_group">    
                    <label>last Name:</label>    
                    <input type = "text" name = "lname" value = "" required/>    
                </div>  
               
				<div class = "form_group">    
                    <label>Gender:</label>    
                    <input type = "radio" name = "sex" value = "male" required/>Male
					<input type = "radio" name = "sex" value = "female" required/>Female
                </div>
					<div class = "form_group">    
                    <label>phone:</label>    
                    <input type = "text" name = "number" value = "" required/>    
                </div>
				<div class = "form_group">    
                    <label>Email:</label>    
                    <input type = "email" name = "mail" value = "" required/>    
                </div>
				<div class = "form_group">    
                    <label>Arrival date:</label>    
                    <input type = "date" name = "date1" value = "" required/>    
                </div>  
				<div class = "form_group">    
                    <label>Departure date:</label>    
                    <input type = "date" name = "date2" value = "" required/>    
                </div>
				<div class = "form_group">    
                    <label>Number Of adults:</label>    
                    <input type = "number" name = "adults" value = "" required/>    
                </div> 
				<div class = "form_group">    
                    <label>Number Of children:</label>    
                    <input type = "number" name = "child" value = "" required/>    
                </div> 
				<div class = "form_group">    
                    <label>City:</label>    
                    <input type = "text" name = "city1" value = "" required/>    
                </div>
				<div class = "form_group">    
                    <label>Country:</label>    
                    <input type = "text" name = "country1" value = "" required/>    
                </div>
				<div class = "form_group">    
                    <label>Room type:</label>    
                    <input type = "radio" name = "room" value = "compact" required/>Compact
					<input type = "radio" name = "room" value = "family" required/>Family
					 <input type = "radio" name = "room" value = "airconditioned" required/>Air-Conditioned
					<input type = "radio" name = "room" value = "deluxe" required/>Deluxe
					 <input type = "radio" name = "room" value = "superdeluxe" required/>Superdeluxe
                </div>
				<div class = "form_group">    
                    <input type ="submit" name = "submit" value = "Book">    
                </div>
				
            </div>    
        </form>    
		<?php
			if(isset($_POST["submit"]) )
			{
				$servername = "localhost";
				$username = "root";
				$password = "";
				$dbname = "test1";
				// Create connection
				$conn = mysqli_connect($servername,$username,$password,$dbname);
				// Check connection
				if (!$conn) 
				{
					die("Connection failed: " . mysqli_connect_error());
				}
				$sql = "INSERT INTO tt(fname,lname,gender,phone,mailid,arrivaldate,departuredate,adults,children,city,country,roomtype) VALUES ('$_POST[fname]','$_POST[lname]','$_POST[sex]','$_POST[number]','$_POST[mail]','$_POST[date1]','$_POST[date2]','$_POST[adults]','$_POST[child]','$_POST[city1]','$_POST[country1]','$_POST[room]')";
				if (!mysqli_query($conn, $sql))
				{
					echo "Error: " . $sql . "<br>" . mysqli_error($conn);
				}
				mysqli_close($conn);
			}
		?>
    </body>    
</html> 