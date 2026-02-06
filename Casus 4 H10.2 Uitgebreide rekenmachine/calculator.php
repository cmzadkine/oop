<?php
function calculate($expression, $precision = 2) {
    $expression = str_replace('^', '**', $expression); // vervang ^ door ** (PHP accepteert dit alleen met eval)
    $expression = preg_replace('/sqrt\((.*?)\)/', 'sqrt($1)', $expression); // sqrt()

    try {
        // Gebruik eval voorzichtig
        $result = eval("return round($expression, $precision);");
        return $result;
    } catch (Throwable $e) {
        return "Fout in berekening.";
    }
}
?>
