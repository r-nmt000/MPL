(function(){
    $('#submit').on('click', function(){
        code = $('#input').val();
        $.get("/mpl/api", {code: code}, function(data){
            $('#output').val(data['output']);
        });
    });
    window.SpeechRecognition = window.SpeechRecognition || webkitSpeechRecognition;
    var Recorder = {
        recognition : null,
        init: function(){
            var o = this;
            o.recognition = new SpeechRecognition();
            o.recognition.lang = 'ja';
            o.recognition.continuous = true;
        },
        recStart: function(){
            var o = this;
            App.status.nowRec = true;
            o.recognition.start();
        },
        recStop: function(){
            var o = this;
            App.status.nowRec = false;
            o.recognition.stop();
        },
        getRecText: function(results, resultIndex){
            var text;
            for(var i = resultIndex; i < results.length; i++){
                var result = results.item(i);
                if(result.final === true || result.isFinal === true){
                    text = result.item(0).transcript;
                }
            }
            return text;
        }
    };
    var View = {
        getResultItem: function(text){
            var el = document.createElement('li');
            el.textContent = text;
            return el;
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
        init: function(){
            var o = this;
            Recorder.init();
            Recorder.recognition.addEventListener('result', function(event){
                var input = o.el.inputArea.val();
                var text = Recorder.getRecText(event.results, event.resultIndex);
                input = input +  ' ' + text;
                o.el.inputArea.val(input);
            });
            o.el.recBtn.on('click', function(){
                if(o.status.nowRec){
                    Recorder.recStop();
                }
                else{
                    Recorder.recStart();
                }
            });
        }
    };
    App.init();
})();