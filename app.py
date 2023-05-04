from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list of notes to display
notes = []

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html', notes=notes)

# Route for the create note page
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Add the note to the list
        notes.append(request.form['note'])
        # Redirect to the index page
        return redirect(url_for('index'))
    else:
        return render_template('create.html')

# Route for the edit note page
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        # Update the note in the list
        notes[index] = request.form['note']
        # Redirect to the index page
        return redirect(url_for('index'))
    else:
        # Get the note to edit from the list
        note = notes[index]
        return render_template('edit.html', note=note)

# Route for the delete note page
@app.route('/delete/<int:index>')
def delete(index):
    # Remove the note from the list
    notes.pop(index)
    # Redirect to the index page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
