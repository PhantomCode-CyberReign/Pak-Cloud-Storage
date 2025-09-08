import os
path = os.path.join(app.config['UPLOAD_FOLDER'], stored_name)
f.save(path)
size = os.path.getsize(path)
token = uuid.uuid4().hex
file_rec = File(filename=orig_name, stored_name=stored_name, user_id=user.id, token=token, size=size)
db.session.add(file_rec)
db.session.commit()
flash('File uploaded', 'success')
return redirect(url_for('dashboard'))


files = File.query.filter_by(user_id=user.id).order_by(File.created_at.desc()).all()
return render_template('dashboard.html', user=user, files=files)


# ----- Download by user -----
@app.route('/file/<int:file_id>/download')
def download_file(file_id):
f = File.query.get_or_404(file_id)
if 'user_id' not in session or session['user_id'] != f.user_id:
abort(403)
return send_from_directory(app.config['UPLOAD_FOLDER'], f.stored_name, as_attachment=True, download_name=f.filename)


# ----- Public share link -----
@app.route('/s/<token>')
def share_download(token):
f = File.query.filter_by(token=token).first_or_404()
return render_template('share_download.html', file=f)


@app.route('/s/<token>/get')
def share_get(token):
f = File.query.filter_by(token=token).first_or_404()
return send_from_directory(app.config['UPLOAD_FOLDER'], f.stored_name, as_attachment=True, download_name=f.filename)


# ----- Delete -----
@app.route('/file/<int:file_id>/delete', methods=['POST'])
def delete_file(file_id):
f = File.query.get_or_404(file_id)
if 'user_id' not in session or session['user_id'] != f.user_id:
abort(403)
try:
os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f.stored_name))
except Exception:
pass
db.session.delete(f)
db.session.commit()
flash('File deleted', 'info')
return redirect(url_for('dashboard'))


# ---------- Run ----------
if __name__ == '__main__':
app.run(debug=True)