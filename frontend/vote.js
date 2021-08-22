"use strict";

function add_like(e) {
    likescount++;
    likes.innerHTML = likescount;
    setTimeout(function (e) {
        likescount = 0;
        likes.innerHTML = likescount;

    }, 2500)
}

function add_dislike(e) {
    dislikescount++;
    dislikes.innerHTML = dislikescount;
}

let likescount = 0;
let dislikescount = 0;
like.addEventListener('click', add_like);
dislike.addEventListener('click', add_dislike);
setTimeout(function (e) {
    like.removeEventListener('click', add_like);
    like.addEventListener('click', function (e) {
        likescount -= 10;
        likes.innerHTML = likescount;
    })
}, 15000)
