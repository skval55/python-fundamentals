def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_freq = {}
    
    phrase = phrase.lower()
    for char in phrase:
        if char in vowel_freq:
            vowel_freq[char] += 1
        elif char in 'aeiou':
            vowel_freq[char] = 1
    return vowel_freq
