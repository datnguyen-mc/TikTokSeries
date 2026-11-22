# Source of truth for the POMPEII film narration (Vietnamese) – Stickman tập 17.
# Builds chNN/script.json with display|spoken tokens (same format as 10-the-chien-2 / 16-titanic).
# Run:  python3 script_src.py            -> writes ./chNN/script.json + ./chapters.json, prints syllables/chapter
import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

CH = [
 ("00", "mo-dau", "POMPEII", "79", [
  "Năm 79, có một thành phố La Mã đang sống một ngày hoàn toàn bình thường.",
  "Chợ đông người, lò bánh mì đỏ lửa, trên tường còn mới sơn khẩu hiệu tranh cử.",
  "Chưa đầy hai ngày sau, tất cả biến mất dưới lớp tro đá dày nhiều mét, và bị lãng quên gần một nghìn bảy trăm năm.",
  "Đây là câu chuyện về Pompeii, kể bằng những người que.",
 ]),
 ("01", "thanh-pho", "THÀNH PHỐ DƯỚI CHÂN NÚI", "Trước năm 79", [
  "Pompeii nằm bên vịnh Naples, miền nam nước Ý, cách đỉnh núi Vesuvius chưa đầy mười cây số.",
  "Đó là một thành phố cảng sầm uất, với hơn mười nghìn dân.",
  "Người ta trồng nho làm rượu vang, làm nước mắm cá garum, rồi chở đi bán khắp Địa Trung Hải.",
  "Cả thành phố có khoảng tám mươi quầy bán đồ ăn nóng, gần giống quán ăn nhanh bây giờ.",
  "Có nhà tắm công cộng, nhà hát, và một đấu trường bằng đá chứa được khoảng hai mươi nghìn người.",
  "Trên tường khắp phố là chữ: quảng cáo, khẩu hiệu bầu cử, lời tỏ tình, cả những câu chửi nhau.",
  "Có người còn viết: Hỡi bức tường, ta ngạc nhiên là ngươi chưa sập, khi phải gánh từng ấy chữ nhảm nhí.",
  "Còn ngọn núi phía sau thành phố thì phủ đầy vườn nho xanh mướt.",
  "Gần như không ai biết, đó là một ngọn núi lửa đang ngủ.",
 ]),
 ("02", "con-rung", "NHỮNG CƠN RUNG", "62 – 79", [
  "Ngày 5/2 năm 62, một trận động đất lớn rung chuyển cả vùng Campania.",
  "Đền thờ nứt toác, tượng đồng vỡ, nhiều ngôi nhà ở Pompeii sụp đổ.",
  "Nhà triết học Seneca ghi lại một chuyện lạ: cả một đàn sáu trăm con cừu chết bất thường sau trận động đất.",
  "Người Pompeii không bỏ đi. Họ dọn dẹp, và xây lại.",
  "Mười bảy năm sau, nhiều công trình vẫn còn sửa dở. Thợ vẫn đang trát tường, vẽ lại những bức bích họa.",
  "Đất vẫn thỉnh thoảng rung. Trong những ngày cuối, các cơn rung dày hơn.",
  "Nhưng ở vùng này, động đất là chuyện thường. Không ai thấy lo.",
  "Họ không biết rằng sâu bên dưới, một khối đá nóng chảy khổng lồ đang dâng lên.",
  "Ngày nay, nhiều nhà khoa học cho rằng trận động đất năm 62 có thể là lời cảnh báo đầu tiên của Vesuvius.",
 ]),
 ("03", "dam-may", "ĐÁM MÂY HÌNH CÂY THÔNG", "Năm 79 · ngày thứ nhất", [
  "Năm 79. Bên kia vịnh, ở căn cứ hải quân Misenum, có một cậu bé mười bảy tuổi tên là Pliny. Người đời sau gọi cậu là Pliny Trẻ.",
  "Đầu giờ chiều hôm đó, mẹ cậu gọi người cậu ruột ra xem một đám mây rất lạ, đang bốc lên từ phía núi.",
  "Pliny tả nó giống một cây thông khổng lồ: một thân cột vươn thẳng lên trời, rồi xòe tán ra ở trên cao.",
  "Đó là cột tro và đá bọt, phụt lên cao hơn ba mươi cây số, gấp gần bốn lần đỉnh Everest.",
  "Vesuvius đã thức dậy.",
  "Khoảng hai mươi lăm năm sau, Pliny kể lại tất cả trong hai lá thư gửi nhà sử học Tacitus.",
  "Đó là lời kể duy nhất của một nhân chứng còn lại đến ngày nay. Kiểu phun trào này về sau được đặt theo tên ông: phun trào kiểu Plinian.",
  "Theo lá thư, hôm đó là ngày 24/8. Hãy nhớ con số này.",
 ]),
 ("04", "mua-da", "TRỜI TỐI GIỮA BAN NGÀY", "Ngày thứ nhất · buổi chiều", [
  "Gió thổi về hướng đông nam, đẩy cả đám mây tro trút thẳng xuống Pompeii.",
  "Trời tối sầm giữa buổi chiều. Từ trên cao, đá bọt trắng xám, nhẹ và xốp, rơi xuống như mưa đá.",
  "Từng viên đá bọt nhẹ đến mức có thể nổi trên mặt nước. Nhưng khi chất thành đống, chúng nặng như đá thật.",
  "Mỗi giờ, lớp đá bọt dày thêm khoảng mười lăm phân. Người ta phải thắp đèn giữa ban ngày.",
  "Người dân phải chọn: chạy, hay ở lại?",
  "Phần lớn đã chạy, mang theo những gì có thể: tiền, đồ trang sức, và cả chìa khóa nhà, như thể họ sẽ sớm quay về.",
  "Những người khác đóng cửa, trốn trong nhà, chờ cơn mưa đá qua đi.",
  "Nhưng nó không qua. Suốt khoảng mười bảy tiếng, đá bọt cứ rơi, chất đống trên mái nhà.",
  "Lớp đá dày gần ba mét. Từng mái nhà bắt đầu sập xuống vì quá nặng.",
  "Và đá bọt, vẫn chưa phải là thứ đáng sợ nhất.",
 ]),
 ("05", "do-doc", "CHUYẾN TÀU CỦA ĐÔ ĐỐC", "Ngày thứ nhất", [
  "Cậu ruột của Pliny Trẻ là Pliny Già, đô đốc chỉ huy hạm đội La Mã ở Misenum, và là một nhà khoa học nổi tiếng.",
  "Ông muốn đi thuyền đến gần để quan sát. Ông rủ cháu đi cùng, nhưng cậu xin ở nhà làm bài.",
  "Vừa bước ra cửa, ông nhận được tin cầu cứu của bà Rectina, có biệt thự ngay dưới chân núi. Lối thoát duy nhất là đường biển.",
  "Chuyến đi khoa học lập tức thành chuyến cứu nạn. Ông cho hạ thủy những chiến thuyền lớn, lao thẳng về phía mọi người đang bỏ chạy.",
  "Tro nóng và đá bọt rơi xuống boong. Gần bờ, đá trôi bịt kín lối vào. Người lái tàu khuyên quay lại.",
  "Ông đáp: vận may đứng về phía người dũng cảm. Hướng về Stabiae!",
  "Ở Stabiae, ông vẫn tắm rửa, ăn tối, rồi đi ngủ, để trấn an những người đang hoảng loạn.",
  "Rạng sáng hôm sau, trời vẫn tối đen. Ông ra bãi biển tìm đường thoát, nhưng sóng vẫn quá dữ.",
  "Ông gục xuống trên bờ cát, và không bao giờ đứng dậy nữa. Khi trời sáng trở lại, người ta tìm thấy ông nằm đó, trông như đang ngủ.",
 ]),
 ("06", "herculaneum", "NỬA ĐÊM Ở HERCULANEUM", "Đêm ngày thứ nhất", [
  "Phía tây ngọn núi là Herculaneum, một thị trấn ven biển của giới nhà giàu, khoảng năm nghìn dân.",
  "Gió thổi tro sang hướng khác, nên suốt buổi chiều, nơi này gần như không có đá rơi.",
  "Nhiều người đã kịp chạy. Hàng trăm người khác dồn ra bãi biển, chen vào những hầm đá cất thuyền, chờ tàu đến cứu.",
  "Đêm đó, cột tro khổng lồ bắt đầu đổ sụp.",
  "Một đám mây khí nóng, tro và đá, nóng hàng trăm độ, lao xuống sườn núi nhanh hơn ô tô trên đường cao tốc.",
  "Các nhà khoa học gọi nó là dòng chảy hỏa thành vụn. Không ai có thể chạy kịp.",
  "Những năm 1980, các nhà khảo cổ đào đến bãi biển cổ, và tìm thấy hài cốt của hơn ba trăm người trong các hầm thuyền.",
  "Gần đó, họ còn gặp một trường hợp có một không hai: mô não của một chàng trai đã biến thành thủy tinh, vì bị nung trên năm trăm độ rồi nguội đi cực nhanh.",
  "Herculaneum bị vùi sâu tới hơn hai mươi mét.",
 ]),
 ("07", "buoi-sang", "BUỔI SÁNG CUỐI CÙNG", "Ngày thứ hai", [
  "Rạng sáng ngày thứ hai, Pompeii vẫn chìm trong bóng tối.",
  "Những người còn ở lại bắt đầu tìm đường ra đi, bước trên lớp đá bọt cao gần ba mét.",
  "Ngay sau 7 giờ sáng, một dòng chảy hỏa thành vụn tràn qua tường thành.",
  "Chỉ trong vài phút, cả thành phố chìm trong tro nóng. Khoảng một nửa số nạn nhân ở Pompeii được tìm thấy trong chính lớp tro này, ngay giữa đường phố.",
  "Bên kia vịnh, Pliny Trẻ và mẹ cũng phải chạy giữa đám đông hoảng loạn.",
  "Cậu viết: bóng tối không giống đêm không trăng, mà như trong một căn phòng kín vừa tắt đèn.",
  "Phụ nữ khóc, trẻ con gào, đàn ông gọi tên nhau. Nhiều người tin rằng các vị thần đã bỏ đi, và đây là đêm cuối cùng của thế giới.",
  "Hai mẹ con sống sót. Đến tối ngày thứ hai, sau khoảng ba mươi hai giờ, núi lửa mới chịu im lặng.",
  "Pompeii, Herculaneum, Stabiae, Oplontis, tất cả đã biến mất.",
 ]),
 ("08", "lang-quen", "THÀNH PHỐ BỊ LÃNG QUÊN", "79 – 1763", [
  "Hoàng đế Titus cử người đến cứu trợ, lấy tài sản của những người chết không người thừa kế để giúp người sống.",
  "Nhưng Pompeii không bao giờ được xây lại. Người sống sót tản về Naples, Cumae, Puteoli.",
  "Năm 2025, các nhà khảo cổ còn phát hiện: một số người nghèo đã quay lại, sống tạm trên tầng hai của những ngôi nhà còn nhô lên khỏi lớp tro.",
  "Đến thế kỷ thứ năm, nơi này bị bỏ hoang hẳn. Cỏ mọc lên. Cả cái tên Pompeii cũng bị quên.",
  "Dân quanh vùng chỉ gọi quả đồi ấy là La Civita, nghĩa là thành phố.",
  "Cuối thế kỷ mười sáu, người ta đào một con kênh xuyên thẳng qua Pompeii, thấy cả tường và chữ khắc, nhưng không ai để tâm.",
  "Năm 1631, Vesuvius lại phun trào, giết hàng nghìn người.",
  "Năm 1738, vua Naples cho đào Herculaneum để tìm tượng cổ. Năm 1748, đến lượt Pompeii.",
  "Năm 1763, một tấm bia đá được tìm thấy, ghi rõ tên Pompeii.",
 ]),
 ("09", "khoang-trong", "NHỮNG KHOẢNG TRỐNG TRONG TRO", "1863", [
  "Suốt hơn một thế kỷ, người ta đào Pompeii chủ yếu để săn tượng và tranh quý.",
  "Năm 1863, nhà khảo cổ Giuseppe Fiorelli để ý một điều lạ: trong lớp tro đã đông cứng có những khoảng rỗng.",
  "Tro nóng đã bao kín các nạn nhân. Theo thời gian, thân thể phân hủy, để lại một cái khuôn rỗng mang đúng hình dáng của họ.",
  "Fiorelli đổ thạch cao lỏng vào khuôn, chờ khô, rồi cẩn thận gỡ lớp tro.",
  "Hiện ra là những con người trong khoảnh khắc cuối cùng. Người co mình, người che mặt, người nằm cạnh nhau.",
  "Có cả một chú chó vẫn đeo vòng cổ, bị xích trước cửa nhà.",
  "Đến nay đã có hơn một trăm tượng thạch cao như thế. Bằng cách đó, người ta còn đúc lại được cửa gỗ, đồ đạc, cả rễ cây trong vườn.",
  "Fiorelli cũng chia thành phố thành từng khu, từng dãy nhà, đánh số từng cánh cửa. Cách đánh số ấy vẫn được dùng đến hôm nay.",
  "Từ đây, Pompeii không còn là kho báu. Nó trở thành cánh cửa nhìn vào đời sống thường ngày của người La Mã.",
 ]),
 ("10", "bi-mat-moi", "NHỮNG BÍ MẬT MỚI", "2018 – 2024", [
  "Còn nhớ ngày 24/8 trong lá thư của Pliny chứ?",
  "Năm 2018, các nhà khảo cổ tìm thấy một dòng chữ viết bằng than trên tường một ngôi nhà, ghi một ngày tương ứng với 17/10.",
  "Than rất dễ phai. Nhiều khả năng nó được viết chỉ ít ngày trước thảm họa.",
  "Thêm vào đó là lựu, sung, quả óc chó của mùa thu, lò sưởi than trong nhà, và rượu mới ủ trong vò.",
  "Nhiều nhà nghiên cứu giờ tin núi lửa phun vào cuối tháng 10, chứ không phải tháng 8. Nhưng tranh cãi vẫn chưa khép lại.",
  "Năm 2024, các nhà khoa học lấy được ADN từ xương bên trong một số tượng thạch cao.",
  "Người lớn đeo vòng tay vàng ôm đứa trẻ, từng được gọi là hai mẹ con, hóa ra là một người đàn ông, không cùng huyết thống với đứa bé.",
  "Hai người ôm nhau, từng được kể là hai chị em, thì có ít nhất một người là nam.",
  "ADN còn cho thấy nhiều người Pompeii có tổ tiên từ phía đông Địa Trung Hải. Một thành phố đa dạng hơn ta tưởng rất nhiều.",
 ]),
 ("11", "thu-vien", "THƯ VIỆN HÓA THAN", "1752 – 2026", [
  "Ở Herculaneum có một biệt thự bên biển, có thể từng thuộc về bố vợ của Julius Caesar.",
  "Giữa thế kỷ mười tám, người ta tìm thấy ở đây khoảng một nghìn tám trăm cuộn và mảnh giấy cói, cháy đen như than.",
  "Đó là thư viện duy nhất từ thời cổ đại còn lại đến ngày nay. Nhưng chỉ cần chạm vào là giấy vỡ vụn.",
  "Năm 2023, cuộc thi Vesuvius Challenge chụp cắt lớp các cuộn giấy, rồi mời cả thế giới dùng trí tuệ nhân tạo để đọc.",
  "Tháng 10 năm đó, một sinh viên hai mươi mốt tuổi đọc được từ đầu tiên trong một cuộn giấy chưa từng được mở: màu tím.",
  "Đầu năm 2024, ba người trẻ giành giải bảy trăm nghìn đô la, khi đọc được hơn hai nghìn ký tự bàn về lạc thú.",
  "Năm 2025, lần đầu tiên người ta đọc được cả tên sách: Bàn về các thói xấu, của triết gia Philodemus.",
  "Đến giữa năm 2026, riêng cuộn ấy đã đọc được hơn bảy mươi cột chữ.",
  "Còn hàng trăm cuộn chưa ai đọc. Biết đâu trong đó là những tác phẩm đã thất truyền hai nghìn năm.",
 ]),
 ("12", "van-thuc", "NÚI LỬA VẪN THỨC", "1943 – nay", [
  "Đêm 24/8/1943, đúng ngày sách sử từng ghi là ngày Pompeii bị hủy diệt, máy bay Đồng minh ném bom xuống khu di tích.",
  "Trong hai tháng, hơn một trăm sáu mươi quả bom rơi trúng thành phố cổ.",
  "Tháng 3 năm 1944, Vesuvius phun trào lần gần nhất. Tro nóng và đá rơi xuống một sân bay quân sự Mỹ dưới chân núi, phá hủy khoảng tám mươi máy bay ném bom.",
  "Từ đó đến nay, núi lửa im lặng. Nhưng nó chưa hề tắt.",
  "Ngày nay, khoảng bảy trăm nghìn người sống trong vùng đỏ quanh Vesuvius. Nếu có báo động, tất cả phải được sơ tán trong vòng ba ngày.",
  "Không xa đó, mặt đất vùng núi lửa Campi Flegrei đang từ từ nâng lên. Tháng 7 năm 2026, một trận động đất bốn phẩy bảy độ, mạnh nhất trong bốn mươi năm, làm rung chuyển Naples.",
  "Còn Pompeii, mỗi năm đón hơn bốn triệu du khách, đông đến mức phải giới hạn hai mươi nghìn người mỗi ngày.",
  "Và gần một phần ba thành phố vẫn còn nằm dưới lớp tro, chờ đến lượt được kể chuyện.",
 ]),
 ("13", "ket", "HẾT", "", [
  "Pompeii không chỉ là câu chuyện về một thảm họa. Đó là một ngày bình thường của con người, được giữ lại suốt gần hai nghìn năm.",
  "Nếu sống ở Pompeii hôm đó, khi trời bắt đầu mưa đá bọt, bạn sẽ chạy, hay ở lại? Bình luận cho mình biết nhé.",
 ]),
]

# Phiên âm cho giọng đọc tiếng Việt (chỉnh lại nếu TTS đọc chưa tự nhiên)
NAMES = {
 "Pompeii": "pôm pê i", "Vesuvius": "vê du vi út", "Naples": "na pô li", "Campania": "cam pa ni a",
 "garum": "ga rum", "Seneca": "xê nê ca", "Misenum": "mi xê num", "Pliny": "pli ni", "Everest": "ê vơ rét",
 "Tacitus": "ta xi tút", "Plinian": "pli ni an", "Rectina": "réc ti na", "Stabiae": "xta bi a",
 "Herculaneum": "héc cu la nê um", "Oplontis": "ô plôn tít", "Titus": "ti tút", "Cumae": "cu mê",
 "Puteoli": "pu tê ô li", "Civita": "chi vi ta", "Giuseppe": "giu dép pê", "Fiorelli": "phi ô ren li",
 "ADN": "a đê en", "Julius": "giu li út", "Caesar": "xê da", "Challenge": "chá lần giơ",
 "Philodemus": "phi lô đê mút", "Campi": "cam pi", "Flegrei": "phlê grây",
}
D = "không một hai ba bốn năm sáu bảy tám chín".split()
def n2(n, full=False):
    t, u = divmod(n, 10)
    if t == 0: return ("lẻ " + D[u]) if full and u else D[u]
    s = "mười" if t == 1 else D[t] + " mươi"
    if u == 0: return s
    if u == 1 and t > 1: return s + " mốt"
    if u == 5: return s + " lăm"
    if u == 4 and t > 1: return s + " tư"
    return s + " " + D[u]
def n3(n, full=False):
    h, r = divmod(n, 100)
    if h == 0 and not full: return n2(r)
    s = D[h] + " trăm"
    return s if r == 0 else s + " " + n2(r, True)
def num(n):
    if n < 1000: return n3(n)
    th, r = divmod(n, 1000)
    s = n3(th) + " nghìn"
    return s if r == 0 else s + " " + n3(r, True)
def spoken(tok):
    core = re.sub(r"^[\"“(]+|[.,:;!?\"”)]+$", "", tok)
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{4})", core)
    if m: return f"{num(int(m[1]))} tháng {num(int(m[2]))} năm {num(int(m[3]))}"
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})", core)
    if m: return f"{num(int(m[1]))} tháng {num(int(m[2]))}"
    if re.fullmatch(r"\d+", core): return num(int(core))
    if core in NAMES: return NAMES[core]
    return None
def tokens(line):
    out = []
    for tok in line.split():
        sp = spoken(tok)
        out.append(tok if sp is None else tok + "|" + sp.replace(" ", "_"))
    return " ".join(out)

if __name__ == "__main__":
    meta, total = [], 0
    for no, slug, title, years, lines in CH:
        d = os.path.join(ROOT, f"ch{no}"); os.makedirs(d, exist_ok=True)
        segs = [{"id": f"s{i+1:02d}", "scene": f"c{no}_{i+1}", "lines": [tokens(l)]} for i, l in enumerate(lines)]
        json.dump(segs, open(os.path.join(d, "script.json"), "w"), ensure_ascii=False, indent=1)
        syl = sum(len(spoken(t).split()) if spoken(t) else 1 for l in lines for t in l.split())
        total += syl
        meta.append({"no": no, "slug": slug, "title": title, "years": years, "syl": syl})
        print(no, title, syl, "syl ~", round(syl / 3.7), "s")
    json.dump(meta, open(os.path.join(ROOT, "chapters.json"), "w"), ensure_ascii=False, indent=1)
    print("TOTAL", total, "syl ~", round(total / 3.7 / 60, 1), "min (chưa tính thẻ chương / pad)")
