import pytest
from main import calculate_patient_risk

def test_standard_case():
    # A 50 year old with 80 bpm should have risk: 50 + 40 = 90
    result = calculate_patient_risk(50, 80)
    assert result == 90

def test_young_patient():
    # A 20 year old with 60 bpm should have risk: 20 + 30 = 50
    result = calculate_patient_risk(20, 60)
    assert result == 50
