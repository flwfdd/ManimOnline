<?php
echo file_get_contents("http://127.0.0.1:2333/?".$_SERVER['QUERY_STRING']);
?>