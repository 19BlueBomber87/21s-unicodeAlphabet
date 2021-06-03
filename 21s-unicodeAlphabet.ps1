New-Item -ItemType file unicodeAlphabet-PS.txt
function create_unicodeAlphabet {
    foreach($i in 0..65994){
        $uniPoint = [char]$i
        Write-Output $uniPoint | Out-File -Append -NoNewline unicodeAlphabet-PS.txt
    }

}
create_unicodeAlphabet
$showOutput = Read-Host View unicode Alphabet?
if ($showOutput -eq "yes"){
    notepad.exe unicodeAlphabet-PS.txt
}
else{
    Write-Verbose -Message "<@:D" -Verbose *>&1
}
