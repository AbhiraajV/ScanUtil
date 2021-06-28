<?php
echo "WELCOME" ;
echo "RECIEVED" ;
$file = $_FILES['file'];
print_r($file);
$fileName = $_FILES['file']['name'];
$filetemp=$_FILES['file'];
$ext = explode('.',$fileName);
$fileext=strtolower(end($ext));
$fileNameNew = uniqid('',true).".".$fileext;
$fileDestination = 'uploads/'.$fileNameNew;
move_uploaded_file($filetemp, $fileDestination);
header("Location: index.php?uploadsuccess");
echo "SUCCESS" ;