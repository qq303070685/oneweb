KindEditor.ready(function(K) {
	K.create('textarea[id=id_solution]', {
		   resizeType:0,
		   allowFlashUpload:false,
		   allowMediaUpload:false,
		   uploadJson:'/upload/kindeditor',
		   afterBlur:function(){this.sync();} 
		   // #增加这个
        });
});