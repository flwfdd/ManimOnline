<?php
//echo file_get_contents("http://127.0.0.1:2333/?".$_SERVER['QUERY_STRING']);
$s=http_build_query($_POST);
$options = array(
	'http' => array(
	  'method' => 'POST',
	  'header' => 'Content-type:application/x-www-form-urlencoded',
	  'content' => $s,
	  'timeout' => 15 * 60
)
);
$context = stream_context_create($options);
$result = file_get_contents("http://127.0.0.1:2333", false, $context);
echo $result;
?>
