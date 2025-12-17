<?php
use PHPUnit\Framework\TestCase;
use App\Classes\Calculator;

require_once __DIR__ . '/../src/Classes/Calculator.php';

class CalculatorTest extends TestCase
{
    private $calculator;

    protected function setUp(): void
    {
        $this->calculator = new Calculator();
    }

    // ADD tests
    public function testAddPositiveNumbers()
    {
        $this->assertEquals(5, $this->calculator->add(2, 3));
    }

    public function testAddNegativeNumbers()
    {
        $this->assertEquals(-5, $this->calculator->add(-2, -3));
    }

    public function testAddZero()
    {
        $this->assertEquals(3, $this->calculator->add(3, 0));
    }

    // SUBTRACT tests
    public function testSubtractPositiveNumbers()
    {
        $this->assertEquals(2, $this->calculator->subtract(5, 3));
    }

    public function testSubtractNegativeNumbers()
    {
        $this->assertEquals(1, $this->calculator->subtract(-2, -3));
    }

    public function testSubtractZero()
    {
        $this->assertEquals(3, $this->calculator->subtract(3, 0));
    }

    // MULTIPLY tests
    public function testMultiplyPositiveNumbers()
    {
        $this->assertEquals(6, $this->calculator->multiply(2, 3));
    }

    public function testMultiplyNegativeNumbers()
    {
        $this->assertEquals(6, $this->calculator->multiply(-2, -3));
    }

    public function testMultiplyWithZero()
    {
        $this->assertEquals(0, $this->calculator->multiply(5, 0));
    }

    // DIVIDE tests
    public function testDividePositiveNumbers()
    {
        $this->assertEquals(2, $this->calculator->divide(6, 3));
    }

    public function testDivideNegativeNumbers()
    {
        $this->assertEquals(2, $this->calculator->divide(-6, -3));
    }

    public function testDivideByZero()
    {
        $this->expectException(Exception::class);
        $this->calculator->divide(5, 0);
    }
}
