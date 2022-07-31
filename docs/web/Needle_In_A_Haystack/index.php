<?php
  require __DIR__."/../vendor/autoload.php";

  include('connect.php');
  include('view.html');

  $warrior = $_GET['warrior'];

  $result = $db->query("SELECT * FROM details 
    WHERE warrior = '$warrior' AND warrior <> 'Arya Stark'");

  while($row = $result->fetch(PDO::FETCH_ASSOC)) {
?>

<style>
  table, th, td {
    border: 1px solid white;
    border-collapse: collapse;
  }
</style>
<table style="position: relative; top: 150px; left: 550px; color: white; text-align: center;">
  <tr>
    <th>Weapon</th>
    <th>Warrior</th>
  </tr>
  <tr>
    <td><?php echo $row['weapon'];?></td>
    <td><?php echo $row['warrior'];?></td>
  </tr>
</table>
<?php
  }
?>