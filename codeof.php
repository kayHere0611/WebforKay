<!DOCTYPE html>
<html>
<head>
<title>Check Prime Number</title>
</head>
<body>
<h2>Check Whether a Number is Prime or Not</h2>
<form method="post">
<label for="num">Enter a number:</label>
<input type="number" id="num" name="num" required>
<input type="submit" value="Check">
</form>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$num = $_POST['num'];
if ($num <= 1) {
echo "<p>$num is <strong>not a prime</strong> number.</p>";
} else {
$isPrime = true;
// Check divisibility from 2 to sqrt($num)
for ($i = 2; $i <= sqrt($num); $i++) {
if ($num % $i == 0) {
$isPrime = false;
break;
}
}
if ($isPrime)
echo "<p>$num is a <strong>prime</strong> number.</p>";
else
echo "<p>$num is <strong>not a prime</strong> number.</p>";
}
}
?>
</body>
</html>