
<?php
require("sendgrid-php/sendgrid-php.php");
$host="localhost";
$username="root";
$password="v3wxvph751";
$databasename="ionicanddjango";

$connect=mysql_connect($host,$username,$password);
$db=mysql_select_db($databasename);

if(isset($_POST['submit_form']))
{
 $name=$_POST["name"];
 $email=$_POST["email"];
$error = 0; 
 // check name only contains letters and whitespace
	if (!preg_match("/^[a-zA-Z ]*$/",$name)) {
		$nameError = "Name: Only letters and white space allowed";
		$error = 1;	
		echo $nameError;
			echo "<script>setTimeout(\"location.href = 'https://www.ionicanddjangotutorial.com';\",1500);</script>";
	}

	if (empty($_POST["email"])) {
		$emailError = "Email is required";
				$error = 1;	
		echo $emailError;
			echo "<script>setTimeout(\"location.href = 'https://www.ionicanddjangotutorial.com';\",1500);</script>";
	} else {
		// check if e-mail address syntax is valid or not
		 if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
			$emailError = "Invalid email format";
					$error = 1;
					echo $emailError;		
						echo "<script>setTimeout(\"location.href = 'https://www.ionicanddjangotutorial.com';\",1500);</script>";
		}
	}
	if ($error==0){
		 mysql_query("insert into newsletter values('','$name','$email')");
		// Redirect to home page	
		echo "Thanks for your subscription";
		 // Now we are ready to build our welcome email
    	$to = $email;
    	$subject = "Hi " . $name . ", Welcome to Ionic Django Tutorial!";
    	$body = '
              <h1>Dear ' . $name . ',</h1></br>
              <p>Thank you for joining our site. </p>
              <p>You have subscribed to my newsletter.</p>
              <p>Let me know if you have further questions, I am here to help.</p>
              <p>Enjoy the rest of your day!</p>
              <p>Kind Regards,</p>
              <p>Christophe</p>
    ';
		   $email = new \SendGrid\Mail\Mail();
$email->setFrom("contact@ionicanddjangotutorial.com", "IonicAndDjango");
$email->setSubject($subject);
$email->addTo($to, $name);
$email->addContent(
    "text/html", $body
);
        $sendgrid = new \SendGrid("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");
try {
    $response = $sendgrid->send($email);
} catch (Exception $e) {
    echo 'Caught exception: '. $e->getMessage() ."\n";
}

    echo "<script>setTimeout(\"location.href = 'https://www.ionicanddjangotutorial.com';\",1500);</script>";
	}
	mysql_close($connect);
}
?>