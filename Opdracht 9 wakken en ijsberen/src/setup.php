<?php

$baseDir = __DIR__;

// mappen
$directories = [
    'public',
    'src'
];

// bestanden in src
$files = [
    'src/Cube.php',
    'src/CubeList.php',
    'src/Game.php',
    'src/GameList.php',
    'src/Hint.php',
    'src/HintList.php',
    'src/Turn.php',
    'src/TurnList.php',
    'src/Play.php',
    'public/index.php'
];

// mappen aanmaken
foreach ($directories as $dir) {
    if (!is_dir($baseDir . '/' . $dir)) {
        mkdir($baseDir . '/' . $dir, 0777, true);
        echo "Map aangemaakt: $dir<br>";
    }
}

// bestanden aanmaken
foreach ($files as $file) {
    $path = $baseDir . '/' . $file;
    if (!file_exists($path)) {
        file_put_contents($path, "<?php\n");
        echo "Bestand aangemaakt: $file<br>";
    }
}

echo "<br>✅ Setup klaar. Verwijder setup.php daarna.";
