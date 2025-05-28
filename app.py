from flask import Flask, request, render_template
import random

app = Flask(__name__)

roasts = [
    "Si {username} yang katanya mau LRP dari tahun lalu tapi kok sampai sekarang masih aktif? Belum siap kehilangan temen virtual atau emang masih belum nemu kegiatan di real life?",
    "Kamu, iya kamu {username} yang suka on tengah malem cuma buat diving mention tab atau upchar. Aslinya emang karena gabut atau emang karena gak ada yang ucapin good night?",
    "{username}? Stop nambah akun melulu, cabang kamu udah banyak. Mau ngalahin cabang Mie Gacoan?",
    "{username} udahan jadi RP loyo, itu kasihan mention tab masih numpuk kayak tumpukan baju yang gak dilaundry selama 2 minggu.",
    "Ganti bio/layout tiap minggu, tapi perasaan malah masih stuck di masa lalu. {username}, waktunya buat upgrade perasaan juga biar gak ngestuck di situ-situ aja.",
    "Posting new tweet mulu, tapi mention sebelumnya gak pernah dibalas. {username} suka banget numpuk mention, nanti pas mau diving mentab malah pusing sendiri karena numpuk.",
    "{username} yang doyan banget mention temen lain di tweet, aura kesepian kamu langsung kelihatan. Padahal temennya juga belum tentu balas.",
    "Eh kamu, {username} yang tiap hari lihat kemesraan orang lain di timeline. Udah waktunya giliran kamu yang pamer kemesraan biar gak jadi nyamuk timeline.",
    "Suka nyabang akun baru berkedok new life, akhirnya ketauan juga karena vibes dan typing masih sama kayak sebelumnya. Mau nyabang berapa banyak akun lagi, {username}?",
    "Ngaku deh, {username} tuh akun yang paling sering “online” tapi paling males bales chat di DM. Padahal temenmu udah geram banget lihat kamu on tapi gak balas DM.",
    "Si {username} yang bilangnya mau upchar, mau upchar, tapi sampai sekarang belum upchar. Emang ketikan gak bisa dipercaya.",
    "{username} paling langganan jadi last bubble di group DM. Kalau ada trophy harian pasti kamu tiap hari dapet.",
    "Hey {username}, udah waktunya menyentuh rumput."
]

# Halaman awal redirect ke /follow
@app.route('/')
def landing():
    return render_template('follow.html')

# Halaman follow dengan countdown 25 detik
@app.route('/follow')
def follow_page():
    return render_template('follow.html')

# Halaman input username & hasil roast
@app.route('/input', methods=['GET', 'POST'])
def home():
    roast = None
    if request.method == 'POST':
        username = request.form['username'].strip('@ ')
        roast = random.choice(roasts).format(username=username)
    return render_template('index.html', roast=roast)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
