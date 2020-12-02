<html>
<body>
<?php 
$username = "root"; 
$password = ""; 
$database = "redriver"; 
$mysqli = new mysqli("localhost", $username, $password, $database); 
$query = "SELECT * FROM basin";


echo '
      <table border="1" cellspacing="2" cellpadding="2"> 
      <tr> 
          <td> <font face="Arial">  </font> </td> 
          <td> <font face="Arial">Date</font> </td> 
          <td> <font face="Arial">Percentage full</font> </td> 
          <td> <font face="Arial">Rerservation storage</font> </td> 
          <td> <font face="Arial">Concetage storage </font> </td> 
          <td> <font face="Arial">Concetage capacity</font> </td>
      </tr>';

if ($result = $mysqli->query($query)) {
    while ($row = $result->fetch_assoc()) {
        $field1name = $row["occu"];
        $field2name = $row["date"];
        $field3name = $row["full_per"];
        $field4name = $row["res_sto"];
        $field5name = $row["con_sto"]; 
        $field6name = $row["con_cap"]; 

        echo '<tr> 
                  <td>'.$field1name.'</td> 
                  <td>'.$field2name.'</td> 
                  <td>'.$field3name.'</td> 
                  <td>'.$field4name.'</td> 
                  <td>'.$field5name.'</td> 
                  <td>'.$field6name.'</td> 
 
              </tr>';
    }
    $result->free();
} 
?>
</body>
</html>
