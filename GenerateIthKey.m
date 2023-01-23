function ithKey = GenerateIthKey(key, keyPosition)

    binkey = HexadecimalToBinary(key)


    % Dropping Parity bits
    ParityDropping = ParityDrop();
    % result = Permute(binkey, ParityDropping, 56);
    [LeftKey, RightKey] = Split(binkey);
    
    % SplitingKey
    shiftTable = ShiftTable();
    specificKey = '';
    
    % For 16 Rounds generate key
    for i = 1:16
        combinedKey = '';        
        LeftKey = ShiftLeft(LeftKey, shiftTable(i));
        RightKey = ShiftLeft(RightKey, shiftTable(i));
        combinedKey = strcat(LeftKey, RightKey); 
        RoundKey = Permute(combinedKey, KeyCompressionTable, 48);
        if i == keyPosition
            specificKey = RoundKey;
        end
        %BinaryToHexadecimal(RoundKey)         
    end
    ithKey = specificKey;
end