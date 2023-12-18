function deleteNote() {
    fetch('/api/notes').then((_res) => {
        console.log(_res)
        //window.location.href = "/";
    });
    
   
}

function showNote(noteId) {
    let note_id = noteId;

    console.log(note_id);
}