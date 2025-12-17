<?php
class Play {
    private $playerName;
    private $games; // array van Game-objecten
    private $currentGuess;
    private $status;
    private $wrong;

    public function __construct() {
        $this->games = [];       // geen GameList nodig
        $this->status = 'start';
        $this->wrong = 0;
        $this->currentGuess = [];
    }

    // spelernaam instellen
    public function setPlayerName($name) {
        $this->playerName = $name;
    }

    // reset alles voor een nieuwe game
    public function reset() {
        $this->games = [];
        $this->status = 'start';
        $this->wrong = 0;
        $this->currentGuess = [];
    }

    // voeg een game toe
    public function addGame(Game $game) {
        $this->games[] = $game;
    }

    // alle vorige games ophalen
    public function getPreviousGames() {
        return $this->games;
    }

    // huidige score berekenen
    public function getScore() {
        $score = 0;
        foreach($this->games as $game) {
            $score += $game->getWrongAnswers();
        }
        return $score;
    }

    // voeg een gok toe
    public function addGuess($iceholes, $polarbears, $penguins) {
        $this->currentGuess = [
            'iceholes' => $iceholes,
            'polarbears' => $polarbears,
            'penguins' => $penguins
        ];
        $this->wrong++;
        $this->status = 'wrong';
    }

    // check of de gok correct is (voorbeeld)
    public function checkScore() {
        if(empty($this->games)) return 'Geen game gestart';
        $lastGame = end($this->games);

        $answer = $lastGame->getAnswer();
        if ($this->currentGuess['iceholes'] == $answer[0] &&
            $this->currentGuess['polarbears'] == $answer[1] &&
            $this->currentGuess['penguins'] == $answer[2]) {
            $this->status = 'correct';
            return 'Goed geraden!';
        } else {
            $this->status = 'wrong';
            return 'helaas fout';
        }
    }

    // voorbeeld hint (kan aangepast worden)
    public function getHint() {
        return "Probeer het nog eens!";
    }

    // teken huidige game (voorbeeld)
    public function draw() {
        echo "<p>Huidige status: {$this->status}</p>";
    }

    // antwoord van de laatste game ophalen
    public function getAnswer() {
        if(empty($this->games)) return [];
        $lastGame = end($this->games);
        return $lastGame->getAnswer();
    }
}
?>
