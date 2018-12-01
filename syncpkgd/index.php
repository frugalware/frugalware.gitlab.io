<?
$hostname = explode(".", $_SERVER['SERVER_NAME']);
header("Location: https://www.frugalware.org/buildlogs/" . $hostname[0]);
?>
