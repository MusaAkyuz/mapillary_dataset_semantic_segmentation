test_images klasörü -> 
	test etmek istediğiniz resimleri ve default olarak gelen birkaç resmi barındıran
	klasördür. 

test_videos klasörü ->
	modeli test etmek için kullanılacak videoları varındıran klasördür.

trained_models klasörü ->
	içerisinden farklı yapılarda modellerle eğitilmiş modelleri barındıran klasördür.

result_frames klasörü ->
	test sırasında elde edilen verilerin kaydedildiği klasördür.

test.model.py 
test_model.ipynb(jupyter dosyası) ->
	modeli test etmek için hazır fonksiyonları içerir.

	get_result_from_video moetodu ->
		içerisine istediğiniz model verilerini, istediğiniz video verisini
		girerek test işlemini başlatabilirsiniz.
		yalnızca modelin giriş türüne göre shape parametresi değiştirilmelidir.
		modelin giriş türü başlığında yazmaktatır.
		örneğin model128x128.h5 modelinde (128, 128, 1) şeklinde shape girilmesi gerekir.
	
	
	get_result_from_images metodu ->
		içerisine istediğiniz model verilerini, istediğiniz video verisini
		girerek test işlemini başlatabilirsiniz.
		yalnızca modelin giriş türüne göre shape parametresi değiştirilmelidir.
		modelin giriş türü başlığında yazmaktatır.
		örneğin model128x128.h5 modelinde (128, 128, 1) şeklinde shape girilmesi gerekir.
	