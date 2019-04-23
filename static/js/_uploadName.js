$('#ProfPic').on('change',function(){
    //get the file name
    var fileName = $(this).val();
    fileName = fileName.split('\\');
    // console.log(fileName)
    //replace the "Choose a file" label
    $(this).next('.custom-file-label').html(fileName[2]);
})
$('#Cert').on('change',function(){
    //get the file name
    var fileName = $(this).val();
    fileName = fileName.split('\\');
    //replace the "Choose a file" label
    $(this).next('.custom-file-label').html(fileName[2]);
})
$('#Transcript').on('change',function(){
    //get the file name
    var fileName = $(this).val();
    fileName = fileName.split('\\');
    //replace the "Choose a file" label
    $(this).next('.custom-file-label').html(fileName[2]);
})