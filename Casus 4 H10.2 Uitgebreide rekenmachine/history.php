<?php
include 'config.php';
$result = $conn->query("SELECT * FROM berekeningen ORDER BY id DESC");

echo "<h2>Berekeningsgeschiedenis</h2>";
echo "<table border='1'><tr><th>Invoer</th><th>Resultaat</th><th>Datum</th></tr>";

while ($row = $result->fetch_assoc()) {
    echo "<tr><td>{$row['invoer']}</td><td>{$row['resultaat']}</td><td>{$row['tijdstip']}</td></tr>";
}
echo "</table>";
?>
<a href="index.php">Terug</a>
