from tkinter.tix import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
# from flask_wtf import FileField, FileAllowed

from sim.models import Tpenduduk


class penduduk_F(FlaskForm):
    nik = StringField('NIK', validators=[
                      DataRequired(), Length(min=10, max=15)])
    nama = StringField('NAMA', validators=[DataRequired()])
    tgl_lahir = StringField('TGL LAHIR', validators=[DataRequired(), Email()])
    email = StringField('EMAIL', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8, max=20)])
    konf_pass = PasswordField('Konfirmasi Password', validators=[
                              DataRequired(), EqualTo('password')])
    alamat = TextAreaField('Alamat')
    tlp = StringField('TLP', validators=[DataRequired()])
    submit = SubmitField('Tambah')

    def validate_nik(self, nik):
        ceknik = Tpenduduk.query.filter_by(nik=Form.nik.data).first()
        if ceknik:
            raise ValidationError('NPM Sudah Terdaftar, Gunakan NPM Yang Lain')

    # cek email
    def validate_email(self, email):
        cekemail = Tpenduduk.query.filter_by(email=Form.email.data).first()
        if cekemail:
            raise ValidationError(
                'Email Sudah Terdaftar, Gunakan Email Yang Lain')


class login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class admin_F(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8, max=20)])
    konf_pass = PasswordField('Konfirmasi Password', validators=[
                              DataRequired(), EqualTo('password')])
    submit = SubmitField('Login')


class profil_F(FlaskForm):
    nama_desa = TextAreaField('nama_desa')
    visi_misi = TextAreaField('visi_misi')
    alamat = TextAreaField('alamat')
    sejarah = TextAreaField('sejarah')
    peraturan = TextAreaField('peraturan')
    geografis = TextAreaField('geografis')
    peta = TextAreaField('peta')
    kontak = TextAreaField('kontak')
    logo = TextAreaField('logo')
    submit = SubmitField('post')


class DataDemog_F(FlaskForm):
    tahun = StringField('Tahun', validators=[DataRequired()])
    jumlah_l = StringField('JUMLAH Laki-Laki', validators=[DataRequired()])
    jumlah_p = StringField('JUMLAH Perempuan', validators=[DataRequired()])
    laju_pertumbuhan = StringField(
        'Laju Pertumbuhan', validators=[DataRequired()])
    submit = SubmitField('post')


class surat_F(FlaskForm):
    kategori = SelectField(u'Kategori Pengaduan', choices=[('TidakMampu', 'Keterangan Tidak Mampu'), (
        'BelumMenika', 'Keterangan Belum Menika')], validators=[DataRequired()])
    keterangan = TextAreaField('Keterangan', validators=[DataRequired()])
    submit = SubmitField('Kirim')


class kabar_desa_F(FlaskForm):
    judul = TextAreaField('Judul', validators=[DataRequired])
    kategori = SelectField(u'Kategori Desa', choices=[('Berita', 'Berita Desa'), (
        'agenda', 'Agenda Desa')], validators=[DataRequired()])
    descripsi = TextAreaField('Descripsi', validators=[DataRequired])
    tgl = TextAreaField('Tanggal', validators=[DataRequired])
    # gambar = ('Gambar')
    submit = SubmitField('kirim')


class putus_sekolah_F(FlaskForm):
    tahun = TextAreaField('Tahun', validators=[DataRequired])
    sd = TextAreaField('SD', validators=[DataRequired])
    smp = TextAreaField('SMP', validators=[DataRequired])
    sma = TextAreaField('SMA', validators=[DataRequired])
    submit = SubmitField('kirim')


class pendidikan_F(FlaskForm):
    tahun = TextAreaField('Tahun', validators=[DataRequired])
    tdk_sd = TextAreaField('Tidak SD', validators=[DataRequired])
    tamat_sd = TextAreaField('Tamat SD', validators=[DataRequired])
    tamat_smp = TextAreaField('Tamat SMP', validators=[DataRequired])
    tamat_sma = TextAreaField('Tamat SMA', validators=[DataRequired])
    tamat_s1 = TextAreaField('Tamat S1', validators=[DataRequired])
    tamat_s2 = TextAreaField('Tamat S2', validators=[DataRequired])
    submit = SubmitField('kirim')


class prasarana_F(FlaskForm):
    nama = TextAreaField('Nama', validators=[DataRequired])
    lokasi = TextAreaField('Lokasi', validators=[DataRequired])
    status = TextAreaField('Status/Luar', validators=[DataRequired])
    tahun_berdiri = TextAreaField('Tahun Berdiri', validators=[DataRequired])
    kategori = SelectField(u'Kategori Pendidikan', choices=[('PendidikanSD', 'Pendidikan SD'), (
        'PendidikanSMP', 'Pendidikan SMP'), ('PendidikanSMA', 'Pendidikan SMA'), ('RumahIbadah', 'Rumah Ibadah'), ('SaranaOlahraga', 'Sarana Olahraga'), ('SaranaKesehatan', 'Sarana Kesehatam')], validators=[DataRequired()])
    keterangan = TextAreaField('Keterangan', validators=[DataRequired()])
    foto = TextAreaField('Foto', validators=[DataRequired])
    submit = SubmitField('Kirim')


class wisatawan_kuliner_F(FlaskForm):
    nama = TextAreaField('Nama', validators=[DataRequired])
    lokasi = TextAreaField('Lokasi', validators=[DataRequired])
    kategori = SelectField(u'Kategori Kuliner', choices=[('Kuliner', 'Kuliner'), (
        'WisataPantai', 'Wisata Pantai'), ('WisataSejarah', 'Wisata Sejarah')], validators=[DataRequired()])
    status = SelectField(u'Status', choices=[('Kuliner', 'Kuliner'), (
        'WisataPantai', 'Wisata Pantai'), ('WisataSejarah', 'Wisata Sejarah')], validators=[DataRequired()])
    nama_pemilik = TextAreaField('Nama Pemilik', validators=[DataRequired])
    descripsi_jualan = TextAreaField(
        'Descripsi Jualan', validators=[DataRequired])
    # gamabr = BLOB('Gambar', validators=[DataRequired()])
    submit = SubmitField('Kirim')
