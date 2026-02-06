<?php
include 'config.php';
include 'calculator.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $expression = $_POST['expression'];
    $precision = $_POST['precision'] ?? 2;
    $result = calculate($expression, $precision);

    $stmt = $conn->prepare("INSERT INTO berekeningen (invoer, resultaat) VALUES (?, ?)");
    $stmt->bind_param("ss", $expression, $result);
    $stmt->execute();

    echo "Opgeslagen: $expression = $result";
}
?>
