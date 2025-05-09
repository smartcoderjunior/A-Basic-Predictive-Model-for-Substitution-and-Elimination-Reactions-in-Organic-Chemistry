"""A Basic Predictive Model for Substitution and Elimination Reactions in Organic Chemistry."""

def predict_mechanism(molecule: dict[str, str]) -> str:
    """Input details about molecule and determine mechanism through a series of if-then statements."""
    
    if molecule["good leaving group"] == "False":    #Is the halide ion able to leave on its own?(Weaker base = better leaving group)
        return "No Reaction"
    
    if molecule["bulky base"] == "True":
        return "E2"
        #Check for bulky bases
    
    if molecule["alkyl halide"] == "primary" and molecule["nucleophile"] == "good": 
        return "SN2"
        #Basic criteria for SN2 reaction
    
    if molecule["alkyl halide"] == "secondary" and molecule["base strength"] == "strong": 
        return "E2"
    elif molecule["alkyl halide"] == "secondary" and molecule["base strength"] == "weak" and molecule["nucleophile"] == "good":
        return "SN2"
    #SN2 versus E2 on secondary alkyl halides (Is the base strong enough to remove a proton?)
    
    if molecule["alkyl halide"] == "tertiary": #Can support a carbocation
        if molecule["base strength"] == "strong": 
            return "E2"
        elif molecule["base strength"] == "weak":
            if molecule["temperature"] == "heated":
                return "E1"
            else: 
                return "SN1"

one_bromopentane = {
    "alkyl halide": "primary", 
    "bulky base" : "False", 
    "nucleophile": "good",
    "base strength": "weak", 
    "temperature": "heated", 
    "good leaving group": "True"
}

print(predict_mechanism(one_bromopentane))

    

    



