from datetime import datetime

from sqlalchemy import null
from sim import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(admin_id):
    return Tadmin.query.get(int(admin_id))

# awal table admin


class Tadmin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(6), nullable=False)
    password = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return f"Tprofil('{self.nama}', '{self.username}', '{self.password}')"
# akhir table admin

# awal table demografi


class DataDemog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tahun = db.Column(db.String(5), nullable=False)
    jumlah_l = db.Column(db.String(5), nullable=False)
    jumlah_p = db.Column(db.String(5), nullable=False)
    laju_pertumbuhan = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"DataDomog('{self.tahun}','{self.jumlah_l}','{self.jumlah_p}','{self.laju_pertumbuhan}')"
# akhir table demografi

# awal table profil


class Tprofil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_desa = db.Column(db.Text, nullable=False)
    visi_misi = db.Column(db.Text, nullable=False)
    alamat = db.Column(db.Text, nullable=False)
    sejarah = db.Column(db.Text, nullable=False)
    peraturan = db.Column(db.Text, nullable=False)
    geografis = db.Column(db.Text, nullable=False)
    peta = db.Column(db.BLOB, nullable=False)
    kontak = db.Column(db.Text, nullable=False)
    logo = db.Column(db.BLOB, nullable=False)

    def __repr__(self):
        return f"Tprofil('{self.nama_desa}','{self.visi_misi}','{self.alamat}','{self.sejarah}','{self.peraturan}','{self.geografis}','{self.peta}','{self.kontak}','{self.logo}'"
# akhir table profil

# awal table penduduk


@login_manager.user_loader
def load_user(penduduk_id):
    return Tpenduduk.query.get(int(penduduk_id))


class Tpenduduk(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nik = db.Column(db.String(25), nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    tgl_lahir = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    alamat = db.Column(db.String(50), nullable=False)
    tlp = db.Column(db.String(12), nullable=False)
    surat = db.relationship('Tsurat_ket', backref='penduduk', lazy=True)

    def __repr__(self):
        return f"Tpenduduk('{self.nik}','{self.nama}','{self.tgl_lahir}','{self.email}','{self.password}','{self.alamat}', '{self.tlp}')"
# akhir table penduduk


class Tpendidikan(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    tahun = db.Column(db.Text, nullable=False)
    tdk_sd = db.Column(db.Text, nullable=False)
    tamat_sd = db.Column(db.Text, nullable=False)
    tamat_smp = db.Column(db.Text, nullable=False)
    tamat_sma = db.Column(db.Text, nullable=False)
    tamat_s1 = db.Column(db.Text, nullable=False)
    tamat_s2 = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Tpendidikan('{self.tahun}','{self.tdk_sd}','{self.tamat_sd}','{self.tamat_smp}','{self.tamat_sma}','{self.tamat_s1}', '{self.tamat_s2}')"
# akhir table penduduk
# akhir table penduduk


class Tputus_sekolah(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    tahun = db.Column(db.Text, nullable=False)
    sd = db.Column(db.Text, nullable=False)
    smp = db.Column(db.Text, nullable=False)
    sma = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Tputus_sekolah('{self.tahun}','{self.sd}','{self.smp}','{self.sma}')"
# akhir table penduduk


class Tprasarana(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.Text, nullable=False)
    lokasi = db.Column(db.Text, nullable=False)
    status = db.Column(db.Text, nullable=False)
    tahun_berdiri = db.Column(db.Text, nullable=False)
    kategori = db.Column(db.Text, nullable=False)
    foto = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Tprasarana('{self.nama}','{self.lokasi}','{self.status}','{self.tahun_berdiri}','{self.kategori}','{self.foto}')"

# awal table surat keterangan


class Tsurat_ket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kategori = db.Column(db.String(50), nullable=False)
    keterangan = db.Column(db.String(300), nullable=False)
    tgl_post = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    penduduk_id = db.Column(db.Integer, db.ForeignKey('tpenduduk.id'))

    def __repr__(self):
        return f"Tsurat_ket('{self.kategori}', '{self.keterangan}', '{self.tgl_post}')"


class Twisata_kuliner(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.Text, nullable=False)
    lokasi = db.Column(db.Text, nullable=False)
    kategori = db.Column(db.Text, nullable=False)
    status = db.Column(db.Text, nullable=False)
    nama_pemilik = db.Column(db.Text, nullable=False)
    deskripsi = db.Column(db.Text, nullable=False)
    gambar = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Twisata_kuliner('{self.nama}','{self.lokasi}','{self.kategori}','{self.status}','{self.nama_pemilik}','{self.deskripsi_jualan}','{self.gambar}')"


class Tkabar_desa(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.Text, nullable=False)
    kategori = db.Column(db.Text, nullable=False)
    deskripsi = db.Column(db.Text, nullable=False)
    tgl = db.Column(db.Text, nullable=False)
    gambar = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Tkabar_desa('{self.judul}','{self.kategori}','{self.deskripsi}','{self.tgl}','{self.gambar}')"
