<?php include 'calculator.php'; ?>
<?php include 'config.php'; ?>

<!DOCTYPE html>
<html>
<head>
    <title>Uitgebreide Rekenmachine</title>
</head>
<body>
    <h2>Rekenmachine</h2>
    <form method="post" action="index.php">
        <input type="text" name="expression" placeholder="Bijv. 2 + 3 * sqrt(9)" required>
        <input type="number" name="precision" min="0" max="10" value="2"> decimalen
        <button type="submit">Bereken</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $expression = $_POST['expression'];
        $precision = $_POST['precision'];

        $result = calculate($expression, $precision);
        echo "<p><strong>Resultaat:</strong> $result</p>";

        // Sla op in de database
        $stmt = $conn->prepare("INSERT INTO berekeningen (invoer, resultaat) VALUES (?, ?)");
        $stmt->bind_param("ss", $expression, $result);
        $stmt->execute();
        $stmt->close();
    }
    ?>

    <a href="history.php">Bekijk opgeslagen berekeningen</a>
</body>
</html>
