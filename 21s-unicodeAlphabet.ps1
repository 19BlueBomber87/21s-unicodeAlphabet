New-Item -ItemType file unicodeAlphabet-PS.txt
New-Item -ItemType file unicodeAlphabet-PS-Wrapped.txt
function create_unicodeAlphabet {
    foreach($i in 0..65994){
        $uniPoint = [char]$i
        Write-Output $uniPoint | Out-File -Append -NoNewline unicodeAlphabet-PS.txt
    }

}
$count = 0
function create_unicodeAlphabet {
    foreach($i in 0..65000){
        $uniPoint = [char]$i
        $count ++
        Write-Output $uniPoint | Out-File -Append -NoNewline unicodeAlphabet-PS-Wrapped.txt
        if($count -eq 150){
            $count = 0
            Write-Output `n | Out-File -Append -NoNewline unicodeAlphabet-PS-Wrapped.txt
        }
        
    }

}
create_unicodeAlphabet
# $showOutput = Read-Host View unicode Alphabet?
# if ($showOutput -eq "yes"){
#     notepad.exe unicodeAlphabet-PS.txt
# }
# else{
#     Write-Verbose -Message "<@:D" -Verbose *>&1
# }
# New-Item -ItemType file -path abc123.txt
# Write-Output yahoo`nyahoo | Out-File -Append -NoNewline abc123.txt