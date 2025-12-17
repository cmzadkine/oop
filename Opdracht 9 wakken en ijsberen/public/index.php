<?php
session_start();

// Includes
include(__DIR__ . '/../src/Cube.php');
include(__DIR__ . '/../src/Game.php');
include(__DIR__ . '/../src/Turn.php');
include(__DIR__ . '/../src/Play.php');

// Als er al een Play-object in sessie zit, gebruik dat
if(isset($_SESSION['play']) && $_SESSION['play'] instanceof Play){
    $play = $_SESSION['play'];
} else {
    $play = new Play();
    $_SESSION['play'] = $play;
}

// Nieuwe game starten
if(isset($_POST['newGame'])){
    $play->reset();
    $_SESSION['play'] = $play;
}

// Spelernaam instellen
if(isset($_POST['newPlay']) && !empty($_POST['name'])){
    $play->setPlayerName($_POST['name']);
    $_SESSION['play'] = $play;
}

// Nieuw Game-object aanmaken met dobbelstenen
if(isset($_POST['cubes']) && is_numeric($_POST['cubes'])){
    $game = new Game((int)$_POST['cubes']);
    $play->addGame($game);
    $_SESSION['play'] = $play;
}

// Guess invullen
if(isset($_POST['guess']) && is_numeric($_POST['iceholes']) && is_numeric($_POST['polarbears']) && is_numeric($_POST['penguins'])){
    $play->addGuess($_POST['iceholes'], $_POST['polarbears'], $_POST['penguins']);
    $_SESSION['play'] = $play;
}

// Antwoord opvragen
if(isset($_POST['answer'])){
    $play->draw();
}

?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Wakken, Ijsberen en Pinguins</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-5">
    <h1>Wakken, Ijsberen en Pinguins</h1>

    <!-- Start new game -->
    <form method="post">
        <button type="submit" name="newGame" class="btn btn-primary mb-3">Start New Game</button>
    </form>

    <?php if(!isset($play->playerName)): ?>
        <!-- Naam speler invullen -->
        <form method="post" class="mb-3">
            <label>Naam Speler</label>
            <input type="text" name="name" class="form-control mb-2" required>
            <button type="submit" name="newPlay" class="btn btn-success">Play</button>
        </form>
    <?php elseif(!isset($play->currentGame)): ?>
        <!-- Aantal dobbelstenen invullen -->
        <form method="post" class="mb-3">
            <label>Aantal dobbelstenen</label>
            <input type="number" name="cubes" min="3" max="8" class="form-control mb-2" required>
            <button type="submit" class="btn btn-success">Gooi Dobbelstenen</button>
        </form>
    <?php else: ?>
        <!-- Spel lopen: guess en answer -->
        <form method="post" class="mb-3">
            <div class="mb-2">
                <label>Raad Wakken</label>
                <input type="number" name="iceholes" class="form-control" required>
            </div>
            <div class="mb-2">
                <label>Raad Ijsberen</label>
                <input type="number" name="polarbears" class="form-control" required>
            </div>
            <div class="mb-2">
                <label>Raad Pinguins</label>
                <input type="number" name="penguins" class="form-control" required>
            </div>
            <button type="submit" name="guess" class="btn btn-primary">Raad</button>
            <button type="submit" name="answer" class="btn btn-secondary">Geef oplossing</button>
        </form>
    <?php endif; ?>

    <!-- Vorige Games -->
    <h3>Vorige Games</h3>
    <table class="table table-striped">
        <thead>
            <tr>
                <th>Aantal beurten</th>
                <th>Fout geraden</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach($play->getPreviousGames() as $game): ?>
            <tr>
                <td><?= $game->getGameTurns(); ?></td>
                <td><?= $game->getWrongAnswers(); ?></td>
            </tr>
            <?php endforeach; ?>
        </tbody>
    </table>

    <!-- Huidige score -->
    <?php if(isset($play->currentGame)): ?>
        <p>Score: <?= $play->getScore(); ?></p>
    <?php endif; ?>
</div>
</body>
</html>
