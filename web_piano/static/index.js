var sounds = {
    "gb7": new Audio("/static/audio/Gb7.wav"),
    "a0": new Audio("/static/audio/A0.wav"),
    "a4": new Audio("/static/audio/A4.wav"),
    "b4": new Audio("/static/audio/B4.wav"),
    "c4": new Audio("/static/audio/C4.wav"),
    "e4": new Audio("/static/audio/E4.wav"),
    "d4": new Audio("/static/audio/D4.wav"),
    "f4": new Audio("/static/audio/F4.wav"),
    "g4": new Audio("/static/audio/G4.wav"),
};
function PlayNote(sound_name){
    sounds[sound_name].play();
};
function PlaySymphony(){
    "a4".play();
    setTimeout: 1000
    "b4".play();
}