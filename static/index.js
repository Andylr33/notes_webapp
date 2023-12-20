function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId})
    }).then((_res) => {
        window.location.href = "/";
    });
}


var listItems = document.querySelectorAll("li"); // this returns an array of each li
listItems.forEach(function(item) {
    item.onmouseout = function(e) {
        fetch('/edit-note', {
            method: 'POST',
            body: JSON.stringify({ noteId: this.id, note_data: this.innerText})
        }).then((_res) => {
            window.location.href = "/";
        });
       //console.log("The id is: ", this.id); // this returns onmouseout li's id
    }
  });
  