function selectRoom(roomName) {

    document.getElementById("roomType").value = roomName;

    document.getElementById("booking").scrollIntoView({
        behavior: "smooth"
    });
}