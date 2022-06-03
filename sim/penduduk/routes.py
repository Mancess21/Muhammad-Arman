from pydoc import describe
from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from sim import db, bcrypt
from sim.penduduk.forms import login, profil_F, DataDemog_F, penduduk_F, surat_F, admin_F, kabar_desa_F, pendidikan_F, prasarana_F, putus_sekolah_F, wisatawan_kuliner_F
from sim.models import Tpenduduk, Tprofil, DataDemog, Tsurat_ket, Tadmin, Tpendidikan, Tprasarana, Tputus_sekolah, Tkabar_desa, Twisata_kuliner


Suser = Blueprint('Suser', __name__)


@Suser.route("/")
def home():
    return render_template("home.html")


@Suser.route("/profil")
def profil():
    form = Tprofil.query.all()
    return render_template("profil.html", form=form)


@Suser.route("/data_demografis", methods=['GET', 'POST'])
def data_demog():
    Dataa = DataDemog.query.all()
    return render_template("data_demog.html", Data=Dataa)


@Suser.route("/ketrangan", methods=['GET', 'POST'])
def ketrangan():
    if not current_user.is_authenticated:
        return redirect(url_for('Suser.user'))
    Data = Tsurat_ket.query.filter_by(penduduk_id=current_user.id)
    form = surat_F()
    if request.method == 'POST':
        # tambah data pengaduan
        add = Tsurat_ket(kategori=form.kategori.data,
                         keterangan=form.keterangan.data, penduduk=current_user)
        db.session.add(add)
        db.session.commit()
        flash('Data berhasisl ditambahkan', 'warning')
        return redirect(url_for('Suser.ketrangan'))
    return render_template("surat_ket.html", form=form, Data=Data)


@Suser.route("/registrasi",  methods=['GET', 'POST'])
def daftar2():
    form = penduduk_F()
    if request.method == 'POST':
        pass_hash = bcrypt.generate_password_hash(
            form.password.data).decode('UTF-8')
        data = Tpenduduk(nik=form.nik.data, nama=form.nama.data, tgl_lahir=form.tgl_lahir.data,
                         email=form.email.data, password=pass_hash, alamat=form.alamat.data, tlp=form.tlp.data)
        db.session.add(data)
        db.session.commit()
        flash('Akun berhasil daftar', 'primary')
        return redirect(url_for('Suser.user'))
    return render_template("daftar.html", form=form)


@Suser.route("/user",  methods=['GET', 'POST'])
def user():
    if current_user.is_authenticated:
        return redirect(url_for('Suser.home'))
    form = login()
    if request.method == 'POST':
        ceknik = Tpenduduk.query.filter_by(nik=form.username.data).first()
        if ceknik and bcrypt.check_password_hash(ceknik.password, form.password.data):
            login_user(ceknik)
            flash('selamat Datang Kembali', 'warning')
            return redirect(url_for('Suser.home'))
        else:
            flash('login gagal, periksa username dan Password!', 'danger')
    return render_template("login_user.html", form=form)


@Suser.route("/editpengaduan", methods=['GET', 'POST'])
@login_required
def editpengaduan():
    if request.method == 'POST':
        m_data = Tsurat_ket.query.get(request.form.get('id'))
        m_data.kategori = request.form['kategori']
        m_data.keterangan = request.form['keterangan']
        db.session.commit()
        flash('Data berhasisl diubah', 'warning')
        return redirect(url_for('Suser.ketrangan'))


@Suser.route("/hapus_A/<id>", methods=['GET', 'POST'])
@login_required
def hapus_A(id):
    my = Tsurat_ket.query.get(id)
    db.session.delete(my)
    db.session.commit()
    flash('Data berhasisl dihapus', 'warning')
    return redirect(url_for('Suser.ketrangan'))


@Suser.route("/logout_admin")
def logout_admin():
    logout_user()
    return redirect(url_for('Suser.home'))


@Suser.route("/prasarana")
def prasarana():
    return render_template('Suser.prasarana')


@Suser.route("/wisata_kuliner", methods=['GET', 'POST'])
def kuliner():
    if not current_user.is_authenticated:
        return redirect(url_for('Suser.user'))
    Data = Twisata_kuliner.query.filter_by(penduduk_id=current_user.id)
    form = wisatawan_kuliner_F()
    if request.method == 'POST':
        # tambah data pengaduan
        add = Twisata_kuliner(nama=form.nama.data, lokasi=form.lokasi.data, kategori=form.kategori.data,
                              status=form.status.data, nama_pemilik=form.nama_pemilik.data, descripsi=form.descripsi.data, gambar=form.gamabar.data, penduduk=current_user)
        db.session.add(add)
        db.session.commit()
        flash('Data berhasisl ditambahkan', 'warning')
        return redirect(url_for('Suser.ketrangan'))
    return render_template("surat_ket.html", form=form, Data=Data)
