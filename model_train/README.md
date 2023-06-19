kitti_pixel_level_semantic klasörü -> 
	içerisinde model eğitimi yapılırken kullanılan
	yardımcı fonksiyonlar, modelin kendisi ve küçük çaplı veri setleri bulunur. 

data_semantics klasörü ->
	değiştirilmemiş asıl resimlerin ve maskelenmiş resimlerin bulunduğu
	klasördür. Bu verile KITTI Vision Benchmark Suite veristesiden çekilmiştir.

fromOtherSource klasörü ->
	önceki çalışmalarım sırasında kullandığım fonksiyonları ve modelleri içerir
	yeni çalışma için yedek niteliğinde veirler de bulundurur

prepared_data klasörü ->
	data_semantics klasöründeki verilerin ihtiyacımıza göre şekillendirildiği
	değiştirildiği ve tekrar kaydedildiği klasördür. Buradaki veriler doğrudan
	model eğitimi için kullanılacak verilerdir.

utils klasöründe -> 
	verisetinin tanımlamalarıni içeren ve tüm klasör yollarını barındıran
	definitions dosyası bulunur. Bu dosyadan tüm ihtiyaç duyulan sabit değerler elde edilir.

image_review dosyası ->
	veriye genel bakış atmak ve ufak denemeler yapmak için kullanılır

kitti_semantic dosyası ->
	baştan sona modeli eğitirken geçen süreci yani verilerin düzenlenmesi, tekrar kaydedilmesi
	modelin oluşturulması gibi adım adım izlediğim yolları ve fonksiyonları içerir

preprocessing dosyası ->
	resimleri model eğitmek için hazır hale getirmek için ön işlemleri yaptığım dosyadır.

test_kitti_semantic ->
	model eğitildikten sonra çalışıp çalışmadığını resimler üzerinde denediğim dosyadır.


 