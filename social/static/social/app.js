$(function () {

    const REFRESH_POOL_INTERVAL = 20000;
    const TWEET_INTERVAL = 6500;
    const ANIMATIONS_IN = "bounceInDown bounceInLeft bounceInRight bounceInUp  slideInDown slideInLeft slideInRight slideInUp".split(" ");
    const ANIMATIONS_OUT = "bounceOutDown bounceOutLeft bounceOutRight bounceOutUp slideOutDown slideOutLeft slideOutRight slideOutUp".split(" ");

    var messages = [];
    const $text = $('#text');
    const $image = $('#image');
    const $video = $('#video');
    const $media = $('#media');
    const $tweet = $('#tweet');
    const $authorPicture = $('#authorPicture');
    const $authorName = $('#authorName');
    const feedId = $('body').data('feed-id');

    function refreshPool() {
        $.get("/feed/"+feedId+".json").then(function (response) {
            var promoted = response.data.promoted;
            var published = response.data.published;
            if (messages.length === 0) setTimeout(loadNextMessage, 500);
            messages = promoted.concat(published).concat(promoted);
        });
    }

    refreshPool();
    setInterval(refreshPool, REFRESH_POOL_INTERVAL);

    function loadNextMessage() {
        var message = _.sample(messages);
        var animation_out = _.sample(ANIMATIONS_OUT);
        $tweet.addClass('animated ' + animation_out);
        $tweet.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function () {
            $tweet.removeClass('animated ' + animation_out);
            var nextTimeToLoad = TWEET_INTERVAL;

            $text.html(message.text);
            $tweet.removeClass('no-media');
            $media.removeClass('video');
            $video[0].loop = false;
            $video[0].autoplay = false;
            $video.find('source').remove();

            $authorName.html(message.authorName + " (" + message.authorUsername + ")");
            $authorPicture.attr('src', message.authorPicture);

            if (message.image !== "") {
                $image.attr('src', message.image);
            } else if (message.video !== "") {
                addSourceToVideo($video[0], message.video, 'video/mp4');
                $video[0].play();
                if (message.videoIsGif) {
                    $video[0].loop = true;
                } else {
                    nextTimeToLoad = 0;
                    $video.one('ended', function () {
                        loadNextMessage()
                    });
                }
                if (!$media.hasClass('video')) $media.addClass('video');
            } else {
                if (!$tweet.hasClass('no-media')) $tweet.addClass('no-media');
            }

            var animation_in = _.sample(ANIMATIONS_IN);
            $tweet.addClass('animated ' + animation_in);
            $tweet.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function () {
                $tweet.removeClass('animated ' + animation_in);
                if (nextTimeToLoad > 0)
                    setTimeout(loadNextMessage, nextTimeToLoad);
            });
        });
    }

    function addSourceToVideo(element, src, type) {
        var source = document.createElement('source');

        source.src = src;
        source.type = type;

        element.appendChild(source);
    }
});