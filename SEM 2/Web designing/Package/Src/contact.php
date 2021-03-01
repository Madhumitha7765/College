<?php
    if(isset($_POST['submit']))
    {
	
        $name = $_POST['name']; // Get Name value from HTML Form
        $email_id = $_POST['email']; // Get Email Value
        $mobile_no = $_POST['mobile']; // Get Mobile No
        $msg = $_POST['message']; // Get Message Value
         
        $to = "madhu2k2.in@gmail.com"; // You can change here your Email
        $subject = "'$name' has sent a mail"; // This is your subject
         
        // HTML Message Starts here
        $message ="
        <html>
            <body>
                <table style='width:600px;'>
                    <tbody>
                        <tr>
                            <td style='width:150px'><strong>Name: </strong></td>
                            <td style='width:400px'>$name</td>
                        </tr>
                        <tr>
                            <td style='width:150px'><strong>Email ID: </strong></td>
                            <td style='width:400px'>$email_id</td>
                        </tr>
                        <tr>
                            <td style='width:150px'><strong>Mobile No: </strong></td>
                            <td style='width:400px'>$mobile_no</td>
                        </tr>
                        <tr>
                            <td style='width:150px'><strong>Message: </strong></td>
                            <td style='width:400px'>$msg</td>
                        </tr>
                    </tbody>
                </table>
            </body>
        </html>
        ";
        // HTML Message Ends here
         
        // Always set content-type when sending HTML email
        $headers = "MIME-Version: 1.0" . "\r\n";
        $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
 
        // More headers
        $headers .= 'From: Admin <madhu2k2.in@gmail.com>' . "\r\n"; // Give an email id on which you want get a reply. User will get a mail from this email id
        
         
        if(mail($to,$subject,$message,$headers)){
            // Message if mail has been sent
            echo "<script>
                    alert('Mail has been sent Successfully.');
                </script>";
        }
 
        else{
            // Message if mail has been not sent
            echo "<script>
                   alert('Mail has been sent Successfully.');
                </script>";
        }
    }
?>
<html>
<head>
<link rel="stylesheet" href="contact.css" type="text/css">
</head>
<body >
<center><br><br><br>
<h1><font color="white"><b><u><mark>CONTACT US</mark></b></u></h1></font>
<form role="form" action="<?= $_SERVER['PHP_SELF'] ?>" method="post">
<input name="name" required="required" type="text" placeholder="Enter Your Name" /><br><br><br>
<input name="email" required="required" type="email" placeholder="Email ID"/><br><br><br>
<input name="mobile" required="required" type="text" placeholder="Enter Mobile No"/><br><br><br>
<textarea name="message" placeholder="Enter your query or feedback"></textarea><br><br><br>
<input name="submit" type="submit" value="Send a Mail" />
</form>
</center>
<a href="a.html"><b><u><mark>CLICK HERE TO NAVIGATE TO HOME PAGE...</mark></b></u></a>
</html>
