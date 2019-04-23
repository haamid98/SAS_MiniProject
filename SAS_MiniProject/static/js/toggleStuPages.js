$(document).ready(function(){
    var btnPg1 = $("#btnPg1");
    var btnPg2 = $("#btnPg2");
    var btnPg3 = $("#btnPg3");
    var btnUpdtProf = $("#btnUpdateProfile");

    var Pg1 = $("#Pg1");
    var Pg2 = $("#Pg2");
    var Pg3 = $("#Pg3");
    var GenProf = $("#ProfilePane");
    var UpdtFrm = $("#UpdateProfileFrm");

    btnUpdtProf.on('click', function(){
        if (GenProf.hasClass('d-flex') && UpdtFrm.hasClass('d-none')){
            UpdtFrm.switchClass("d-none","d-flex", 400, "easeInOutBack")
            UpdtFrm.animate({opacity: "1"}, 600)

            GenProf.switchClass("d-flex","d-none",400,"easeInOutBack");
            GenProf.animate({opacity: "0"}, 600);
        }
    });

    btnPg1.on('click', function(){
        $(this).addClass('active')
        btnPg2.removeClass('active')
        btnPg3.removeClass('active')

        if (Pg1.hasClass('d-flex') && Pg2.hasClass('d-none') && Pg3.hasClass('d-none') ){
            console.log("all is well");
        }else{
            
            Pg1.switchClass("d-none","d-flex",400,"easeInOutBack");
            Pg1.animate({opacity: "1"}, 600);

            Pg2.switchClass("d-flex","d-none",400,"easeInOutBack");
            Pg2.animate({opacity: "0"}, 600);

            Pg3.switchClass("d-flex","d-none",400,"easeInOutBack");
            Pg3.animate({opacity: "0"}, 600);
        }
    });

    btnPg2.on('click', function(){
        $(this).addClass('active')
        btnPg1.removeClass('active')
        btnPg3.removeClass('active')

        if (Pg2.hasClass('d-flex') && Pg1.hasClass('d-none') && Pg3.hasClass('d-none') ){
            console.log("all is well");
        }else{
            
            Pg2.switchClass("d-none","d-flex",400,"easeInOutBack");
            Pg2.animate({opacity: "1"}, 600);

            Pg1.switchClass("d-flex","d-none",400,"easeInOutBack");
            Pg1.animate({opacity: "0"}, 600);

            Pg3.switchClass("d-flex","d-none",400,"easeInOutBack");
            Pg3.animate({opacity: "0"}, 600);
        }
    });

    btnPg3.on('click', function(){
        $(this).addClass('active')
        btnPg1.removeClass('active')
        btnPg2.removeClass('active')

        if (Pg3.hasClass('d-flex') && Pg2.hasClass('d-none') && Pg1.hasClass('d-none') ){
            console.log("all is well");
        }else{
            
            Pg3.switchClass("d-none","d-flex",400,"easeInOutBack");
            Pg3.animate({opacity: "1"}, 600);

            Pg2.switchClass("d-flex","d-none",400,"easeInOutBack");
            Pg2.animate({opacity: "0"}, 600);

            Pg1.switchClass("d-flex","d-none",400,"easeInOutBack");
            Pg1.animate({opacity: "0"}, 600);
        }
    });
});