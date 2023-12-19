function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId})
    }).then((_res) => {
        window.location.href = "/";
    });
}

function showNote(noteId) {
    //let note_id = noteId;

    console.log(noteId);
}