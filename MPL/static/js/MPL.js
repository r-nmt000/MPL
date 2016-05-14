(function () {
    $('#submit').on('click', function () {
        var code = $('#input').val();
        var str = $('#submit').text();
        $('#submit').text('');
        $('#submit').prepend('<i></i>');
        $('#submit i').toggleClass('fa fa-circle-o-notch faa-spin animated');
        setTimeout(function () {
            $.get("/api", {code: code}, function (data) {
                $('#output').val(data['output']);
            });
            $('#submit').text('');
            $('#submit').prepend('<i></i>' + str);

        }, 1000);
    });

    $(document).ready(function () {
        var hsize = $(window).height();
        if (parseInt($("#main").css("height").slice(0,parseInt($("#main").css("height")))) < hsize) {
            $("#main").css("height", hsize + "px");
        }
        if (parseInt($("#how-to-use").css("height").slice(0,parseInt($("#how-to-use").css("height")))) < hsize) {
            $("#how-to-use").css("height", hsize + "px");
        }
        if (parseInt($("#hello-world").css("height").slice(0,parseInt($("#hello-world").css("height")))) < hsize) {
            $("#hello-world").css("height", hsize + "px");
        }
    });


    window.SpeechRecognition = window.SpeechRecognition || webkitSpeechRecognition;
    var Recorder = {
        recognition: null,
        init: function () {
            var o = this;
            o.recognition = new SpeechRecognition();
            o.recognition.lang = 'ja';
            o.recognition.continuous = true;
        },
        recStart: function () {
            var o = this;
            App.status.nowRec = true;
            $('#microphone').toggleClass('faa-flash animated faa-slow');
            o.recognition.start();
        },
        recStop: function () {
            var o = this;
            App.status.nowRec = false;
            $('#microphone').toggleClass('faa-flash animated faa-slow');
            o.recognition.stop();
        },
        getRecText: function (results, resultIndex) {
            var text;
            for (var i = resultIndex; i < results.length; i++) {
                var result = results.item(i);
                if (result.final === true || result.isFinal === true) {
                    text = result.item(0).transcript;
                }
            }
            return text;
        }
    };
    var App = {
        el: {
            recBtn: $('#microphone'),
            inputArea: $('#input')
        },
        status: {
            nowRec: false,
            recorderText: ''
        },
        init: function () {
            var o = this;
            Recorder.init();
            Recorder.recognition.addEventListener('result', function (event) {
                var input = o.el.inputArea.val();
                var text = Recorder.getRecText(event.results, event.resultIndex);
                input = input + ' ' + text;
                o.el.inputArea.val(input);
            });
            o.el.recBtn.on('click', function () {
                if (o.status.nowRec) {
                    Recorder.recStop();
                }
                else {
                    Recorder.recStart();
                }
            });
        }
    };
    App.init();
})();