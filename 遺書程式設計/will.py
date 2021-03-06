# 遺書的軟體開發side project
# 開發緣由:
# 藝人小鬼,酒駕遭撞及其他意外事件死亡的人,
# 還有我自己的身體狀況,所以想開發這個程式功能

# 功能:
# 死亡後自動寄遺書email到指定對象的信箱,告知後事辦理及想說的話
# EX:我想告知家人想說的話及後事如何辦理,還有保險業務員的聯絡方式,電腦的帳號密碼...等

# 邏輯:
# 寄信人User = U在死亡後,自動將遺書寄到 收件人Love = L的信箱,
# 但系統該如何判定死亡? 台灣有什麼系統是可以幫助判定死亡的?
# 1.自然人憑證?未來如果台灣數位資訊進步,假設人死亡時,自然人憑證會發出訊息證明死亡,中央系統收到訊號即驗證死亡,將信寄出
# 2.定期檢驗機制1 EX:每個月寄確認信到信箱,若超過一週沒點回應就將信送出?
# 3.定期檢驗機制2 EX:每季寄信到信箱通知有沒有要更新及延長或取消遺書功能

# 介面:
# 創建使用(寄信)者→設定收件者(可不只一個)→內容或附件(同上可不只一個)
# →檢驗機制(定期發送檢驗連結至U信箱)
# →超過三個月沒點檢驗信表示死亡→寄出信件
#  →有點檢驗信→表示活著→不寄出信件