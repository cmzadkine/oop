<?php

require '../vendor/autoload.php';

use App\Classes\Calculator;

$calc = new Calculator();

echo "Optellen: " . $calc->add(10, 5) . "<br>";
echo "Aftrekken: " . $calc->subtract(10, 5);



