package ru.pr1blagirev;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class CalculatorTest {
    private final Calculator calculator = new Calculator();

    @Test
    void sumShouldReturnCorrectResult() {
        assertEquals(7, calculator.sum(3, 4));
    }

    @Test
    void multiplyShouldReturnCorrectResult() {
        assertEquals(12, calculator.multiply(3, 4));
    }
}
